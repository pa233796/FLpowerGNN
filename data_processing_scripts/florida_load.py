import pandas as pd

def create_load_csv():
    # Load the dataset
    dset = pd.read_hdf("historic_load_hourly_2016_2023_county.h5")

    # Isolate Florida columns (starting with p12)
    florida_cols = [c for c in dset.columns if str(c).startswith("p12")]

    # Case 1: Timestamp is a regular column in the dataset
    if "timestamp" in dset.columns:
        cols_to_keep = ["timestamp"] + florida_cols
        load = dset[cols_to_keep].copy()
        
        # Rename columns: Keep 'timestamp', remove 'p' from counties
        cleaned_cols = ["timestamp"] + [c[1:] for c in florida_cols]
        load.columns = cleaned_cols
        
        # Save to CSV
        load.to_csv("florida_load.csv", index=False)

    # Case 2: Timestamp is the DataFrame index (most common for this data)
    else:
        load = dset[florida_cols].copy()
        
        # Remove 'p' from county columns
        cleaned_cols = [c[1:] for c in florida_cols]
        load.columns = cleaned_cols
        
        # Save to CSV with index=True so the timestamp index becomes the first column
        load.to_csv("florida_load.csv", index=True)

    print("Saved florida_load.csv!")

if __name__ == "__main__":
    create_load_csv()