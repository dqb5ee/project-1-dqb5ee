import pandas as pd
import os

def run():
    """
    Unified transformation of point A to point B, with point A being two raw state-wide CSV chunks
    And point B being one unified parquet entity (wildfire_events)
    """
    
    # Relative path for GitHub
    data_dir = os.path.join('..', 'data')
    
    # Defining the specific filenames as they appear in /data folder
    chunks = [
        os.path.join(data_dir, 'California_Historic_Fire_Perimeters_1516624541847049096.csv'),
        os.path.join(data_dir, 'California_Historic_Fire_Perimeters_3836453159319713276.csv')
    ]
    
    # Verification Step
    for chunk in chunks:
        if not os.path.exists(chunk):
            print(f"Error: Could not find {chunk}. Ensure files are in the /data directory.")
            return

    print("--- Merging and Filtering Fire Perimeters ---")

    # Merging & de-duplicating
    # Concatenates both chunks and removes records with identical OBJECTIDs
    df = pd.concat([pd.read_csv(f) for f in chunks], ignore_index=True)
    
    # Standardizing the Date at the SOURCE
    # Removes need for complex SQL parsing later
    df['Alarm Date'] = pd.to_datetime(df['Alarm Date'], errors='coerce')
    df = df.dropna(subset=['Alarm Date']) # Remove any records with unparseable dates
    
    df = df.drop_duplicates(subset=['OBJECTID'])
    
    # Applying research threshold
    # Focus specifically on fires >= 10,000 acres to define "Catastrophic Spread"
    df = df[df['GIS Calculated Acres'] >= 10000]
    
    # Relational normalization
    # Renaming raw headers to match the project's formal Data Dictionary
    mapping = {
        'OBJECTID': 'Fire_ID',
        'Fire Name': 'Fire_Name',
        'Alarm Date': 'Alarm_Date',
        'GIS Calculated Acres': 'GIS_Acres',
        'Unit ID': 'Unit_ID'
    }
    events = df[mapping.keys()].rename(columns=mapping)
    
    # Adding target variable for future modeling
    events['Is_Catastrophic'] = 1
    
    # Saving as an optimized parquet file
    output_path = os.path.join(data_dir, 'wildfire_events.parquet')
    events.to_parquet(output_path, index=False)
    
    print(f"Success: Created {output_path} with {len(events)} records.")

if __name__ == "__main__":
    run()
