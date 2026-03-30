import duckdb
import os
import pandas as pd

def run():
    """
    This function executes the multi-table relational join via DuckDB.
    It serves as the final bridge between environmental baselines and historical fire events to create a unified analytical dataset.
    """
    
    # Defining the data directory for Google Colab
    data_dir = '/content/drive/MyDrive/DS_data/'
    
    # Initializing an in memory DuckDB connection
    con = duckdb.connect()
    
    print("--- Executing Arid Edge Relational Join ---")

    # SQL join logic:
    # Joining "wildfire_events" (fact table) to 'unit_agency' (dimension table) via Unit_ID to normalize administrative naming
    # Joining "wildfire_events" to "moisture_readings" (fact table) via a temporal join
    # This matches Alarm_Date to the regional moisture baseline at a Month-Year level
    query = f"""
        SELECT 
            f.Fire_Name, 
            f.Alarm_Date, 
            f.GIS_Acres, 
            r.LFM_Percent, 
            a.Agency_Name
        FROM read_parquet('{os.path.join(data_dir, "wildfire_events.parquet")}') f
        JOIN read_parquet('{os.path.join(data_dir, "unit_agency.parquet")}') a 
             ON f.Unit_ID = a.Unit_ID
        JOIN read_parquet('{os.path.join(data_dir, "moisture_readings.parquet")}') r 
             ON strftime(f.Alarm_Date, '%Y-%m') = strftime(r.Date, '%Y-%m')
        ORDER BY f.GIS_Acres DESC
    """
    
    # Executing and returning as a dataframe for the Random Forest step
    df_analysis = con.execute(query).df()
    
    print(f"Relational Join Complete. Analytical Dataset contains {len(df_analysis)} matched records.")
    return df_analysis

# Executing the join within the Colab environment
df_analysis = run()
df_analysis.head()    
    # Executing the relational query and convert the result set into a pandas df
    results = con.execute(query).df()
    
    # Exporting the final analytical entity to a parquet file
    # Serves as the end result for the pipeline
    output_path = os.path.join(data_dir, 'final_arid_edge_analysis.parquet')
    results.to_parquet(output_path, index=False)
    
    print("Entity created successfully.")

if __name__ == "__main__":
    run()
