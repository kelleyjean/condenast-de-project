import pandas as pd
import csv
import glob
import os

path = os.getcwd()
csv_files = glob.glob(os.path.join(path, "*.csv"))

def dataframes_to_pickle():
  for f in csv_files:
    filename = f.split("\\", 1)[1]
    df = pd.read_csv(f)
    df.to_pickle("./pickle_files/" + filename + '.pkl')


dataframes_to_pickle()
