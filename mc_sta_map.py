"""
mc_sta_map.py

Repair station list data & making map

SHSH <sandy.herho@email.ucr.edu>
7/27/23
"""

# import libs & settings
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pygmt
import warnings

plt.style.use("ggplot")
plt.rcParams['figure.figsize'] = [20, 10]
plt.rcParams['figure.dpi'] = 1200
warnings.filterwarnings("ignore")

# read raw sta data
df = pd.read_excel("./raw_data/st_list.xlsx", sheet_name="Lengkap",
                  index_col="No")

# renaming
df = df.rename(columns={df.columns[0]:"station_name",
                        df.columns[1]:"region",
                        df.columns[2]:"longitude",
                        df.columns[3]:"latitude",
                        df.columns[4]:"elevation"})

df["region"] = df["region"].str.replace("Jawa","Java")
df["region"] = df["region"].str.replace("Kalimantan", "Borneo")

# save csv file
df.to_csv("./processed_data/sta_list.csv")

# plot map
fig = pygmt.Figure()
fig.basemap(region=[93, 143, -20, 20], projection="M15c", frame=True)
fig.coast(land="black", water="skyblue")
fig.plot(x=df["longitude"], y=df["latitude"], style="c0.3c", cmap="white", pen="black")
fig.savefig("./figs/fig1.png")