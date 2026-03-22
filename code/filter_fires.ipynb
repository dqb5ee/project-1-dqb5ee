import pandas as pd
import os

# Defining relative paths for the two chunks of fire data
file1 = os.path.join('..', 'data', 'California_Historic_Fire_Perimeters_1516624541847049096.csv')
file2 = os.path.join('..', 'data', 'California_Historic_Fire_Perimeters_3836453159319713276.csv')
output_path = os.path.join('..', 'data', 'filtered_socal_fires.csv')

def filter_fire_data():
    # Loading and merging
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)
    fires = pd.concat([df1, df2]).drop_duplicates(subset=['OBJECTID'])

    # Converting dates and filtering for SoCal Units (LAC, VNC, SBC, etc.)
    fires['Alarm Date'] = pd.to_datetime(fires['Alarm Date'], errors='coerce')
    socal_units = ['LAC', 'VNC', 'SBC', 'SLU', 'BDU', 'ORC', 'RRU', 'MVU']

    fires_clean = fires[(fires['Alarm Date'] >= '2005-01-01') & 
                        (fires['Alarm Date'] <= '2019-06-30') & 
                        (fires['Unit ID'].isin(socal_units))].copy()

    # Saving filtered records
    fires_clean.to_csv(output_path, index=False)
    print(f"Success: {output_path} created.")

if __name__ == "__main__":
    filter_fire_data()
