"""
lmwl_est.py

Estimating LMWL using Bayesian Linear Regression
SHSH <sandy.herho@email.ucr.edu>
8/21/23
"""

# import libs
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['figure.dpi'] = 800
plt.style.use("ggplot")

# data wrangling
df = pd.read_csv("../output_data/sta_data/all_sta.csv")
df = df.replace(-999, np.nan).dropna()

o18 = df["o18"].to_numpy()
h2 = df["h2"].to_numpy()

# lmwl-gmwl estimates
h2_gmwl = 8*o18 + 10
h2_lmwl_best = 7.298 * o18 + 3.506
h2_lmwl_upper = (7.298 + 0.534) * o18 + (3.506 + 3.464)
h2_lmwl_lower = (7.298 - 0.534) * o18 + (3.506 - 3.464)

# plot
plt.figure(figsize=(20,10))
plt.scatter(o18, h2, color="grey")
plt.plot(o18, h2_gmwl, color="k", label="GMWL", linewidth=2);
plt.plot(o18, h2_lmwl_best, color="red", linewidth=2, label="LMWL");
plt.plot(o18, h2_lmwl_upper, "--", linewidth=1, color="red");
plt.plot(o18, h2_lmwl_lower, "--", linewidth=1, color="red");
plt.xlabel("$\delta^{18}$O [‰, VSMOW]", fontsize=30);
plt.ylabel("$\delta^{2}$H [‰, VSMOW]", fontsize=30);
plt.tick_params(axis="x", which="major", labelsize=12)
plt.tick_params(axis="x", which="minor", labelsize=12)
plt.tick_params(axis="y", which="major", labelsize=12)
plt.tick_params(axis="y", which="minor", labelsize=12)
plt.legend()
plt.savefig("../figs/fig5.png")