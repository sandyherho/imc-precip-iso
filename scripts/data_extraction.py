"""
data_extraction.py

Extracting and cleaning for each station data

SHSH <sandy.herho@email.ucr.edu>
7/27/23
"""

# import libs & settings
import glob
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings("ignore")


# read_data
def first_iso_cleaning(sheet_name):
    file_name = "../raw_data/isotop monthly.xlsx"
    df = pd.read_excel(file_name, sheet_name=sheet_name)
    df = df.drop([df.columns[0], df.columns[1]], axis=1)
    df = df.replace("E", np.nan)
    df = df.replace(-999, np.nan)
    df = df.round(3)
    df = df.drop([60, 61, 62], axis=1)
    df = df.rename(columns={63:60, 64:61, 65:62})
    return df

o18 = first_iso_cleaning("d18(OBS)")
h2 = first_iso_cleaning("dD(OBS)_2")

def d_excess(h2, o18):
    return (h2 - 8*o18)

# save raw clean data
o18.to_csv("../raw_data/raw_clean/o18_clean.csv", index=False)
h2.to_csv("../raw_data/raw_clean/h2_clean.csv", index=False)

d_ex = d_excess(h2, o18)
d_ex.to_csv("../raw_data/raw_clean/d_excess_clean.csv", index=False)

# process sta data
date = pd.date_range(start='9/1/2010', end='10/1/2017', freq="M")


i=1
while i<=62:
    frame = {"date":date, "o18":o18[i], "h2":h2[i]}
    df_join = pd.DataFrame(frame).set_index("date")
    df_join["d_excess"] = d_excess(df_join["h2"], df_join["o18"])
    df_join = df_join.round(3)
    df_join = df_join.replace(np.nan, -999)
    df_join.to_csv("../output_data/sta_data/sta_"+str(i)+".csv")
    i+=1

path = "../output_data/sta_data/"
df = pd.concat(map(pd.read_csv, glob.glob(path + "/*.csv")))
df = df.drop([df.columns[0], df.columns[-1]], axis=1)
df.to_csv(path+"all_sta.csv", index=False)