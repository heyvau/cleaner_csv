# pip install ydata_profiling

import os
from pathlib import Path

os.chdir(Path(__file__).parent)

import pandas as pd
from ydata_profiling import ProfileReport

# 1 - read the CSV File

df = pd.read_csv("./files/my_data.csv")

# 2 - create a Profile
profile = ProfileReport(df)

# 3 - save the output Profile
profile.to_file(output_file="./profile.html")