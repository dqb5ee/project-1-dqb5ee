import pandas as pd
import matplotlib.pyplot as plt
import os

# Defining paths
moisture_path = os.path.join('..', 'data', 'processed_fuel_moisture.csv')
fires_path = os.path.join('..', 'data', 'filtered_socal_fires.csv')
output_img = os.path.join('..', 'outputs', 'santa_ana_threshold_viz.png')

def run_correlation():
    # Loading processed data
    moisture = pd.read_csv(moisture_path)
    fires = pd.read_csv(fires_path)

    # Aligning dates for the join
    moisture['month_yr'] = pd.to_datetime(moisture['month_yr']).dt.to_period('M')
    fires['month_yr'] = pd.to_datetime(fires['Alarm Date']).dt.to_period('M')

    # Relational join
    final_data = pd.merge(fires, moisture, on='month_yr', how='left')

    # Plotting
    plt.figure(figsize=(15, 8))
    
    # Baseline
    plt.plot(pd.to_datetime(moisture['month_yr'].dt.to_timestamp()), 
             moisture['percent'], color='#34495e', alpha=0.3, label='Fuel Moisture Trend')
    
    # Plotting 75% threshold
    plt.axhline(y=75, color='#c0392b', linestyle='--', linewidth=2, label='Santa Ana Threshold (75%)')
    plt.fill_between(pd.to_datetime(moisture['month_yr'].dt.to_timestamp()), 
                     40, 75, color='#e74c3c', alpha=0.1, label='Critical Ignition Window')

    # Plotting major fires (>10k acres)
    major = final_data[final_data['GIS Calculated Acres'] >= 10000].dropna(subset=['percent'])
    plt.scatter(pd.to_datetime(major['Alarm Date']), major['percent'], 
                s=major['GIS Calculated Acres']/150, color='#d35400', alpha=0.8, edgecolors='black', zorder=5)

    plt.title("The 'Santa Ana Threshold': Proving the Correlation (2005 - 2019)", fontsize=14, fontweight='bold')
    plt.ylabel('Live Fuel Moisture (%)')
    plt.ylim(40, 140)
    plt.legend()

    # Making sure output directory exists and save
    os.makedirs(os.path.dirname(output_img), exist_ok=True)
    plt.savefig(output_img, dpi=300)
    print(f"Success: Final Model Visualization saved to {output_img}")

if __name__ == "__main__":
    run_correlation()
