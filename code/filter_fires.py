import pandas as pd
import os
import logging

# Simple logging setup
logging.basicConfig(
    filename='/content/drive/MyDrive/DS_data/pipeline.log', 
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def run():
    """
    Unified transformation of point A to point B, with point A being two raw state-wide CSV chunks
    And point B being one unified parquet entity (wildfire_events)
    """
    logging.info("Starting wildfire_events transformation...")
    
    # Using absolute paths for Google Colab/Drive consistency
    base_path = '/content/drive/MyDrive/DS_data/'
    chunks = [
        os.path.join(base_path, 'California_Historic_Fire_Perimeters_1.csv'),
        os.path.join(base_path, 'California_Historic_Fire_Perimeters_2.csv')
    ]

    # Adding proper error handling
    # Making sure the pipeline doesn't attempt to run on non-existent data
    for chunk in chunks:
        if not os.path.exists(chunk):
            logging.error(f"CRITICAL: File missing at {chunk}")
            print(f"Error: Check log file for missing path details.")
            return

    # Processing logic with exception handling
    try:
        # Loading and concatenating raw CSVs into a single df
        df = pd.concat([pd.read_csv(f) for f in chunks], ignore_index=True)
        logging.info(f"Initial load successful. Row count: {len(df)}")

        # Cleaning and standardizing dates for join compatibility
        df['Alarm Date'] = pd.to_datetime(df['Alarm Date'], errors='coerce')
        df = df.dropna(subset=['Alarm Date']) 
        
        # Removing duplicate records based on the unique OBJECTID
        df = df.drop_duplicates(subset=['OBJECTID'])

        # Filtering for fires >= 10,000 acres to define the "Catastrophic" threshold
        df = df[df['GIS Calculated Acres'] >= 10000]
        logging.info(f"Filtered to {len(df)} catastrophic events (>= 10k acres)")

        # Mapping raw column names to formal data dictionary headers (relational normalization)
        mapping = {
            'OBJECTID': 'Fire_ID',
            'Fire Name': 'Fire_Name',
            'Alarm Date': 'Alarm_Date',
            'GIS Calculated Acres': 'GIS_Acres',
            'Unit ID': 'Unit_ID'
        }
        events = df[mapping.keys()].rename(columns=mapping)
        
        # Assigning binary target variable for the Random Forest model
        events['Is_Catastrophic'] = 1

        # Exporting to Parquet for optimized DuckDB querying
        output_path = os.path.join(base_path, 'wildfire_events.parquet')
        events.to_parquet(output_path, index=False)

        logging.info("Parquet entity created successfully.")
        print(f"Entities created successfully.")

    except Exception as e:
        # Catch-all for data-related errors 
        logging.error(f"Unexpected error during transformation: {str(e)}")
        print("Transformation failed. Check pipeline.log for details.")

# Execute the pipeline
run()
