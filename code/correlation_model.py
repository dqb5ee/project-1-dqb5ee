import duckdb
import os
import pandas as pd

def run():
    """
    This function executes the multi-table relational join via DuckDB.
    It serves as the final bridge between environmental baselines and historical fire events to create a unified analytical dataset.
    """
    
    # Defining the data directory relative to the /code folder
    data_dir = os.path.join('..', 'data')
    
    # Initialize an in-memory DuckDB connection for high-performance SQL execution
    con = duckdb.connect()
    
    print("--- Executing Arid Edge Relational Join ---")

    # The SQL Join Logic:
    # 1. Joins 'wildfire_events' (Fact Table) to 'unit_agency' (Dimension Table) 
    #    via Unit_ID to normalize administrative naming.
    # 2. Joins 'wildfire_events' to 'moisture_readings' (Fact Table) via a 
    #    Temporal Join, matching the Alarm_Date to the regional moisture baseline 
    #    at a Month-Year grain.
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
    
    # Execute the relational query and convert the result set into a Pandas DataFrame
    results = con.execute(query).df()
    
    # Export the final analytical entity to Parquet
    # This file serves as the 'Point B' result for the entire project pipeline
    output_path = os.path.join(data_dir, 'final_arid_edge_analysis.parquet')
    results.to_parquet(output_path, index=False)
    
    print(f"✅ Success: Final analytical join complete and saved to {output_path}")

if __name__ == "__main__":
    run()
