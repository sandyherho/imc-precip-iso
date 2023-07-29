"""
eda.py

Exploratory data analysis

SHSH <sandy.herho@email.ucr.edu>
7/28/23
"""

# import libs & settings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

plt.rcParams['figure.dpi'] = 500
plt.style.use("fivethirtyeight")
plt.rcParams['figure.figsize'] = [20, 10]
warnings.filterwarnings("ignore")

# open data
date = pd.date_range(start='9/1/2010', end='10/1/2017', freq="M")
pr = pd.read_csv("../raw_data/raw_clean/pr_clean.csv")
o18 = pd.read_csv("../raw_data/raw_clean/o18_clean.csv")
h2 = pd.read_csv("../raw_data/raw_clean/h2_clean.csv")
d_ex = pd.read_csv("../raw_data/raw_clean/d_excess_clean.csv")

# nums of data points
count_sta_data = pd.DataFrame(o18.count().rename("Data Points"))

fig, ax = plt.subplots(figsize=(20, 8));
count_sta_data.plot(kind="bar", ax=ax);
ax.set_xlabel("Station number", fontsize=30);
ax.set_ylabel("Number of data points", fontsize=30);
ax.tick_params(axis="x", which="major", labelsize=12, rotation=45)
ax.tick_params(axis="x", which="minor", labelsize=12, rotation=45)
ax.tick_params(axis="y", which="major", labelsize=12)
ax.tick_params(axis="y", which="minor", labelsize=12)
ax.get_legend().remove()
fig.savefig("../figs/fig2.png")

print("Max. sta.: ", count_sta_data.idxmax()) # pos kemayoran
print("# of max data points: ", count_sta_data.max()) # 47 
print("Min. sta.: ", count_sta_data.idxmin()) # ranomeeto, tambang
print("# of max data points: ", count_sta_data.min()) # 2
print(count_sta_data[count_sta_data >= (50 / 100 * o18.shape[0])].dropna()) # >= 50% : pos kemayoran(1), deli serdang (5), radin inten II (11)
print("median nums: " + str(count_sta_data.median()) + "; or "+ str(count_sta_data.median() / 85 * 100) + "%.") # med: 22, or 25. 882% of total months
count_sta_data.index.name="station_number"
count_sta_data.to_csv("../output_data/descriptive_stats/number_of_data_points.csv")

# median, std
## o18
o18_med = pd.DataFrame(o18.median(axis=0).rename("median"))
o18_med.index.name="station_number"
print("Sta. max. med: " + str(o18_med.idxmax()) + "; Max med: " + str(o18_med.max())) # El Tari (24), -0.062, jum: 3 
print("Sta. min. med: " + str(o18_med.idxmin()) + "; Min med: " + str(o18_med.min())) # Malikulsaleh (53), -9.539, jum: 3
o18_med.to_csv("../output_data/descriptive_stats/o18_median.csv")

o18_std = pd.DataFrame(o18.std(axis=0).rename("std"))
o18_std.index.name="station_number"
print("Sta. max. std: " + str(o18_std.idxmax()) + "; Max std: " + str(o18_std.max())) # Pesawaran (41), -0.062, jum: 8
print("Sta. min. std: " + str(o18_std.idxmin()) + "; Min std: " + str(o18_std.min())) # Ranomeeto (58), -9.539, jum: 2
o18_std.to_csv("../output_data/descriptive_stats/o18_std.csv")

## h2
h2_med = pd.DataFrame(h2.median(axis=0).rename("median"))
h2_med.index.name="station_number"
print("Sta. max. med: " + str(h2_med.idxmax()) + "; Max med: " + str(h2_med.max())) # El Tari (24), 1.597, jum: 3 
print("Sta. min. med: " + str(h2_med.idxmin()) + "; Min med: " + str(h2_med.min())) # Malikulsaleh (53), -9.539, jum: 3
h2_med.to_csv("../output_data/descriptive_stats/h2_median.csv")

h2_std = pd.DataFrame(h2.std(axis=0).rename("std"))
h2_std.index.name="station_number"
print("Sta. max. std: " + str(h2_std.idxmax()) + "; Max std: " + str(h2_std.max())) # Tambang (57), 33.086, jum: 2
print("Sta. min. std: " + str(h2_std.idxmin()) + "; Min std: " + str(h2_std.min())) # Sorong (54), 5.307, jum: 4
h2_std.to_csv("../output_data/descriptive_stats/h2_std.csv")

# boxplots
fig, ax = plt.subplots(figsize=(20, 25));
sns.boxplot(data=o18, orient="h", color="skyblue", ax=ax)
ax.set_xlabel("$\delta^{18}$O [‰, VSMOW]", fontsize=50);
ax.set_ylabel("Station number", fontsize=50);
ax.tick_params(axis="x", which="major", labelsize=20, rotation=45)
ax.tick_params(axis="x", which="minor", labelsize=20, rotation=45)
ax.tick_params(axis="y", which="major", labelsize=20)
ax.tick_params(axis="y", which="minor", labelsize=20)
fig.savefig("../figs/fig3a.png")

fig, ax = plt.subplots(figsize=(20, 25));
sns.boxplot(data=h2, orient="h", color="red", ax=ax)
ax.set_xlabel("$\delta^{2}$H [‰, VSMOW]", fontsize=50);
ax.set_ylabel("Station number", fontsize=50);
ax.tick_params(axis="x", which="major", labelsize=20, rotation=45)
ax.tick_params(axis="x", which="minor", labelsize=20, rotation=45)
ax.tick_params(axis="y", which="major", labelsize=20)
ax.tick_params(axis="y", which="minor", labelsize=20)
fig.savefig("../figs/fig3b.png")