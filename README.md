# FLpowerGNN

Leveraging modern AI techniques for electrical load forescasting.

An AI/ML project by Pablo Rodriguez and Shambhu Marasini from the University of Central Florida for
the class term project of EEL 6878: Modeling and Artificial Intelligence (Instructor: Dr. Tong Wu).

## Training and running the models

All the relevant code is contained in the Jupyter Notebooks, you can setup your environment using the following:

```
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cd notebook/
jupyter notebook
```

## Data processing scripts

Preprocessed datasets and other useful files are found in the `data/` folder. The scripts to derive
these from the upstream data sources are found in `data_processsing_scripts/`.

* `01_florida_load.py` for dataset [1]
* `02_florida_distances.py` for dataset [2]

### Upstream Data Sources

> [1] Obika, K., Cole, W., & Rivers, M. (2025). Hourly Electricity Demand Profiles for Each County
> in the Contiguous United States. [Data set]. Open Energy Data Initiative (OEDI). National
> Renewable Energy Laboratory. https://data.openei.org/submissions/8562

> [2] Roth, J. (2010). U.S. Census Bureau County Distance Database. [Data set] National Bureau of
> Economic Research (NBER). https://doi.org/10.60592/afwp-pj35
