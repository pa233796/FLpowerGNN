# Extract only the Florida counties (column names like "p12XXX") from the dataset
# 'Hourly Electricity Demand Profiles for Each County in the Contiguous United States'
# (https://data.openei.org/submissions/8562)

import pandas as pd

def main():
    dset = pd.read_hdf('historic_load_hourly_2016_2023_county.h5')
    selection = list(filter( lambda x: x.startswith("p12"), dset.columns ))
    result = dset[selection]
    print(result)
    result.to_hdf('florida_dataset.h5', key="fl")


if __name__ == '__main__':
    main()
