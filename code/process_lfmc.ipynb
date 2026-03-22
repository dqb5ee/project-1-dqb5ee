import pandas as pd
import os

# Defining paths
input_path = os.path.join('..', 'data', 'lfmc_observations.csv')
output_path = os.path.join('..', 'data', 'processed_fuel_moisture.csv')

def process_moisture():
    # Loading data
    df = pd.read_csv(input_path)
    df['date'] = pd.to_datetime(df['date'])

    # Filtering for study period (2005 - 2019)
    df = df[(df['date'] >= '2005-01-01') & (df['date'] <= '2019-06-30')]

    # Aggregating to monthly regional average
    df['month_yr'] = df['date'].dt.to_period('M')
    moisture_baseline = df.groupby('month_yr')['percent'].mean().reset_index()

    # Saving processed data
    moisture_baseline.to_csv(output_path, index=False)
    print(f"Success: {output_path} created.")

if __name__ == "__main__":
    process_moisture()
