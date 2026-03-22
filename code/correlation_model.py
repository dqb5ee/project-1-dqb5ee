import python as pd
import io
import matplotlib.pyplot as plt

# Configurating
base_path = '/content/drive/MyDrive/DS_data/'
moisture_path = os.path.join(base_path, 'lfmc_observations.csv')
fire_part1 = os.path.join(base_path, 'California_Historic_Fire_Perimeters_1516624541847049096.csv')
fire_part2 = os.path.join(base_path, 'California_Historic_Fire_Perimeters_3836453159319713276.csv')

def run_validation():
    print("Loading datasets from Google Drive...")
    
    # Loading and prepping moisture data
    moisture = pd.read_csv(moisture_path)
    moisture['date'] = pd.to_datetime(moisture['date'])
    # Create monthly average baseline
    moisture['month_yr'] = moisture['date'].dt.to_period('M')
    moisture_baseline = moisture.groupby('month_yr')['percent'].mean().reset_index()

    # Same for fire data
    f1 = pd.read_csv(fire_part1)
    f2 = pd.read_csv(fire_part2)
    fires = pd.concat([f1, f2]).drop_duplicates(subset=['OBJECTID'])
    
    # Cleaning dates and filtering for SoCal Units
    fires['Alarm Date'] = pd.to_datetime(fires['Alarm Date'], errors='coerce')
    fires['month_yr'] = fires['Alarm Date'].dt.to_period('M')
    
    # Relational join
    final_data = pd.merge(fires, moisture_baseline, on='month_yr', how='left')

    # Calculating
    # Filtering for major fires (>10,000 acres)
    major_fires = final_data[final_data['GIS Calculated Acres'] >= 10000].dropna(subset=['percent'])
    
    # Calculating for proof of concept
    avg_moisture = major_fires['percent'].mean()
    pct_below_threshold = (major_fires[major_fires['percent'] <= 75].shape[0] / len(major_fires)) * 100

    print("-" * 30)
    print(f"VALIDATION SUCCESSFUL")
    print(f"Total Major Fires Analyzed: {len(major_fires)}")
    print(f"Average Moisture at Ignition: {avg_moisture:.2f}%")
    print(f"Percentage of Fires below 75% Threshold: {pct_below_threshold:.1f}%")
    print("-" * 30)

if __name__ == "__main__":
    run_validation()
