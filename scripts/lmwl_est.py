"""
lmwl_est.py

Estimating LMWL using Bayesian Linear Regression
SHSH <sandy.herho@email.ucr.edu>
7/29/23
"""

import numpy as np
import pandas as pd
import pymc3 as pm
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
from sklearn.linear_model import LinearRegression

plt.rcParams['figure.figsize'] = [20, 10]
plt.style.use("ggplot")
warnings.filterwarnings("ignore")

# Read data
df = pd.read_csv("../output_data/sta_data/all_sta.csv")
df = df.replace(-999, np.nan).dropna()
pr = df["precipitation"].values.reshape(-1, 1)
o18 = df["o18"]
h2 = df["h2"]

h2_gmwl = 8 * o18 + 10
h2_gmwl.values.reshape(-1, 1)

o18 = o18.values.reshape(-1, 1)
h2 = h2.values.reshape(-1, 1)


# LMWL
## freq.
lin_reg_lmwl = LinearRegression().fit(o18, h2)
print("intercept freq:", lin_reg_lmwl.intercept_)  # intercept
print("slope freq: ", lin_reg_lmwl.coef_)  # slope
h2_predicted = lin_reg_lmwl.predict(o18)

## Bayes
prior = pd.read_csv("../raw_data/lmwl_putmanEtAl19.csv")[["m", "b", "koppen"]]  # 29 stations
prior = prior[prior["koppen"] == "Af"]

mean_slope_prior = prior["m"].mean()  # 8.119
std_slope_prior = prior["m"].std()  # 0.68
mean_inter_prior = prior["b"].mean()  # 12.174
std_inter_prior = prior["b"].std()  # 4.468

with pm.Model() as linReg:
    intercept = pm.Normal("intercept", mu=mean_inter_prior, sd=std_inter_prior)
    slope = pm.Normal("slope", mu=mean_slope_prior, sd=std_slope_prior)
    sd = pm.Uniform("sd", 0, 100)
    mu = pm.Deterministic("mu", intercept + slope * o18)
    y = pm.Normal("y", mu=mu, sd=sd, observed=h2)
    trace_lmwl = pm.sample(10000, tune=2000, cores=6)  # 1e4 steps, throw away the 1st 2e3 steps (burn-in period)


# Plot traceplots for LMWL
plt.figure()
plt.subplot(311)
plt.plot(trace_lmwl["intercept"], color="indianred", alpha=0.85)
plt.ylabel(r"$\beta_0$", fontsize=40)
plt.tick_params(axis="x", which="major", labelsize=12)
plt.tick_params(axis="x", which="minor", labelsize=12)
plt.tick_params(axis="y", which="major", labelsize=12)
plt.tick_params(axis="y", which="minor", labelsize=12)

plt.subplot(312)
plt.plot(trace_lmwl["slope"], color="darkslategrey", alpha=0.85)
plt.ylabel(r"$\beta_1$", fontsize=40)
plt.tick_params(axis="x", which="major", labelsize=12)
plt.tick_params(axis="x", which="minor", labelsize=12)
plt.tick_params(axis="y", which="major", labelsize=12)
plt.tick_params(axis="y", which="minor", labelsize=12)

plt.subplot(313)
plt.plot(trace_lmwl["sd"], color="seagreen", alpha=0.85)
plt.ylabel(r"$\sigma$", fontsize=40)
plt.xlabel("Iterations", fontsize=40)
plt.tick_params(axis="x", which="major", labelsize=12)
plt.tick_params(axis="x", which="minor", labelsize=12)
plt.tick_params(axis="y", which="major", labelsize=12)
plt.tick_params(axis="y", which="minor", labelsize=12)

plt.tight_layout()
plt.savefig("../figs/fig4a.png")

plt.figure()
plt.subplot(311)
plt.hist(trace_lmwl["intercept"], bins=100, color="indianred", alpha=0.85, density=True)
plt.ylabel(r"$\beta_0$", fontsize=40)
plt.tick_params(axis="x", which="major", labelsize=12)
plt.tick_params(axis="x", which="minor", labelsize=12)
plt.tick_params(axis="y", which="major", labelsize=12)
plt.tick_params(axis="y", which="minor", labelsize=12)

plt.subplot(312)
plt.hist(trace_lmwl["slope"], bins=100, color="darkslategrey", alpha=0.85, density=True)
plt.ylabel(r"$\beta_1$", fontsize=40)
plt.tick_params(axis="x", which="major", labelsize=12)
plt.tick_params(axis="x", which="minor", labelsize=12)
plt.tick_params(axis="y", which="major", labelsize=12)
plt.tick_params(axis="y", which="minor", labelsize=12)

plt.subplot(313)
plt.hist(trace_lmwl["sd"], bins=100, color="seagreen", alpha=0.85, density=True)
plt.ylabel(r"$\sigma$", fontsize=40)
plt.xlabel("Posterior distributions [‰, VSMOW]", fontsize=40)
plt.tick_params(axis="x", which="major", labelsize=12)
plt.tick_params(axis="x", which="minor", labelsize=12)
plt.tick_params(axis="y", which="major", labelsize=12)
plt.tick_params(axis="y", which="minor", labelsize=12)

plt.tight_layout()
plt.savefig("../figs/fig4b.png")

intercept = trace_lmwl["intercept"].mean() # mean intercepr
slope = trace_lmwl["slope"].mean() # mean slope
print("LMWL intercept mean: ", round(intercept, 3)) # 3.506
print("LMWL slope mean: ", round(slope, 3)) # 7.298

intercept_std = trace_lmwl["intercept"].std() # std intercepr
slope_std = trace_lmwl["slope"].std() # std slope
print("LMWL intercept std: ", round(intercept_std, 3)) # 1.732
print("LMWL slope std: ", round(slope_std, 3)) # 0.267

plt.figure()
for i in range(0,10000):
    plt.plot(o18, trace_lmwl["intercept"][i] + trace_lmwl["slope"][i]*o18,
             c="lightgreen", alpha=0.5);

plt.plot(o18, h2, "o", color="grey");
plt.plot(o18, intercept + slope * o18, "-", color="green",
         linewidth=2);
plt.plot(o18, h2_gmwl, "-", color="black");
plt.xlabel("$\delta^{18}$O [‰, VSMOW]", fontsize=30);
plt.ylabel("$\delta^{2}$H [‰, VSMOW]", fontsize=30);
plt.tick_params(axis="x", which="major", labelsize=12)
plt.tick_params(axis="x", which="minor", labelsize=12)
plt.tick_params(axis="y", which="major", labelsize=12)
plt.tick_params(axis="y", which="minor", labelsize=12)
plt.savefig("../figs/fig5.png")
