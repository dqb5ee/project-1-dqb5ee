import pandas as pd
import os

# Configurating
base_path = '/content/drive/MyDrive/DS_data/'
file1 = os.path.join(base_path, 'California_Historic_Fire_Perimeters_1516624541847049096.csv')
file2 = os.path.join(base_path, 'California_Historic_Fire_Perimeters_3836453159319713276.csv')
output_path = os.path.join(base_path, 'filtered_socal_fires.csv')

def filter_fire_data():
    # Loading and merging the two GIS record chunks
    if not os.path.exists(file1) or not os.path.exists(file2):
        print("Error: Fire perimeter source files not found in Drive.")
        return

    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)
    
    # Merging and deduplicating based on the unique OBJECTID to ensure data integrity
    fires = pd.concat([df1, df2]).drop_duplicates(subset=['OBJECTID'])

    # Converting dates to datetime objects for temporal filtering
    fires['Alarm Date'] = pd.to_datetime(fires['Alarm Date'], errors='coerce')
    
    # Defining Southern California Unit IDs (LAC=LA County, VNC=Ventura, etc.)
    socal_units = ['LAC', 'VNC', 'SBC', 'SLU', 'BDU', 'ORC', 'RRU', 'MVU']

    # Applying multi-conditional filter: Study Period + Geography
    fires_clean = fires[(fires['Alarm Date'] >= '2005-01-01') & 
                        (fires['Alarm Date'] <= '2019-06-30') & 
                        (fires['Unit ID'].isin(socal_units))].copy()

    # Saving filtered records
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    fires_clean.to_csv(output_path, index=False)
    
    print(f"Success: {output_path} created with {len(fires_clean)} relevant fire events.")

if __name__ == "__main__":
    filter_fire_data()
