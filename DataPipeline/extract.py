import pandas as pd
import csv
import glob
import os

csv_files = glob.glob('**/*.csv', recursive=True)

def dataframes_to_pickle():
  for f in csv_files:
    filename = f.split("\\", 1)[1]
    df = pd.read_csv(f)
    df.to_pickle("./pickle_files/" + filename + '.pkl')

dataframes_to_pickle()