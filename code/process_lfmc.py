import pandas as pd
import os
import logging

# Consistency with the wildfire_events log
logging.basicConfig(
    filename='/content/drive/MyDrive/DS_data/pipeline.log', 
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def run():
    """
    Transforms raw LFMC observations into two distinct relational entities: 
    moisture_sites (dimension table) and moisture_readings (fact table).
    """
    logging.info("Starting moisture_observations transformation...")

    # Defining absolute paths for Google Colab/Drive consistency
    base_path = '/content/drive/MyDrive/DS_data/'
    input_file = os.path.join(base_path, 'lfmc_observations.csv')

    # Proper error handling 
    if not os.path.exists(input_file):
        logging.error(f"CRITICAL: Input file missing at {input_file}")
        print(f"Error: Check log file for missing moisture data path.")
        return

    # Processing Logic with Exception Handling
    try:
        # Loading raw CSVs
        df = pd.read_csv(input_file)
        logging.info(f"Initial load of moisture data successful. Row count: {len(df)}")

        # Creating moisture_site entity (dimension table)
        # Isolating static geographic metadata and removing duplicates for relational normalization
        sites = df[['site', 'latitude', 'longitude']].drop_duplicates()
        sites.columns = ['Site_ID', 'Latitude', 'Longitude']
        
        # Saving site metadata as a Parquet file
        sites.to_parquet(os.path.join(base_path, 'moisture_sites.parquet'), index=False)
        logging.info(f"Created moisture_sites entity with {len(sites)} unique stations.")

        # Creating moisture_reading entity (fact table)
        # Standardizing temporal data for DuckDB joins
        readings = df[['site', 'date', 'percent', 'fuel']].copy()
        readings.columns = ['Site_ID', 'Date', 'LFM_Percent', 'Fuel_Type']
        readings['Date'] = pd.to_datetime(readings['Date'], errors='coerce')
        
        # Removing any records with unparseable dates to maintain data integrity
        readings = readings.dropna(subset=['Date'])

        # Filtering for Research Study Period
        # Aligns the moisture baseline with the available fire history data
        readings = readings[(readings['Date'] >= '2005-01-01') & (readings['Date'] <= '2019-06-30')]
        
        # Generating a unique primary key for the reading records
        readings['Reading_ID'] = range(1, len(readings) + 1)

        # Saving standardized readings as an optimized Parquet file
        readings.to_parquet(os.path.join(base_path, 'moisture_readings.parquet'), index=False)
        
        logging.info(f"SUCCESS: moisture_readings entity created with {len(readings)} records.")
        print("Entities created successfully.")

    except Exception as e:
        # Catch-all for data-related errors during the moisture transformation
        logging.error(f"Unexpected error during moisture transformation: {str(e)}")
        print("Moisture transformation failed. Check pipeline.log for details.")

run()
