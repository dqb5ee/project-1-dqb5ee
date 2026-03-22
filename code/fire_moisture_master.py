import pandas as pd
import io

# Loading raw data
f1 = pd.read_csv('/content/drive/MyDrive/DS_data/California_Historic_Fire_Perimeters_1516624541847049096.csv')
f2 = pd.read_csv('/content/drive/MyDrive/DS_data/California_Historic_Fire_Perimeters_3836453159319713276.csv')
# Note: You will need to have 'lfmc_observations.csv' in the same folder
lfmc = pd.read_csv('/content/drive/MyDrive/DS_data/lfmc_observations.csv')

# Processing fire perimeters (merging the two parts and removing duplicates)
fires = pd.concat([f1, f2]).drop_duplicates(subset=['OBJECTID'])
fires['Alarm Date'] = pd.to_datetime(fires['Alarm Date'], errors='coerce')

# Filtering for Southern California Units and the 2005-2019 study window
socal_units = ['LAC', 'VNC', 'SBC', 'SLU', 'BDU', 'ORC', 'RRU', 'MVU']
fires_clean = fires[(fires['Alarm Date'] >= '2005-01-01') & 
                    (fires['Alarm Date'] <= '2019-06-30') & 
                    (fires['Unit ID'].isin(socal_units))].copy()

# Processing fuel moisture
lfmc['date'] = pd.to_datetime(lfmc['date'])

# Filtering for same study window
lfmc_sub = lfmc[(lfmc['date'] >= '2005-01-01') & (lfmc['date'] <= '2019-06-30')].copy()

# Creating monthly regional average
lfmc_sub['month_yr'] = lfmc_sub['date'].dt.to_period('M')
moisture_baseline = lfmc_sub.groupby('month_yr')['percent'].mean().reset_index()

# Creating master join (Correlation Model)
fires_clean['month_yr'] = fires_clean['Alarm Date'].dt.to_period('M')
fire_moisture_master = pd.merge(fires_clean, moisture_baseline, on='month_yr', how='left')

# Exporting the result
fire_moisture_master.to_csv('/content/drive/MyDrive/DS_data/fire_moisture_master.csv', index=False)
print("SUCCESS: fire_moisture_master.csv has been generated.")
