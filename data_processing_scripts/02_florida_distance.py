import pandas as pd

def create_distance_csv():
    dist = pd.read_csv("sf12010countydistancemiles.csv")

    dist["county1"] = dist["county1"].astype(str)
    dist["county2"] = dist["county2"].astype(str)

    # Florida only
    dist = dist[
        dist["county1"].str.startswith("12") &
        dist["county2"].str.startswith("12")
    ].copy()

    # ensure numeric (remove p, keep 12001 format)
    dist["county1"] = dist["county1"].astype(int)
    dist["county2"] = dist["county2"].astype(int)

    dist = dist.rename(columns={"mi_to_county": "distance"})

    dist.to_csv("florida_distance.csv", index=False)

    print("Saved florida_distance.csv")

if __name__ == "__main__":
    create_distance_csv()