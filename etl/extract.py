import pandas as pd
import csv
import glob
import os

path = os.getcwd()
csv_files = glob.glob(os.path.join(path, "*.csv"))

#Function returns count of files and loops through to store each csv as a dataframe
#def store_dataframes():
  #dfs = list()
  #for csvfile in files:
   # fpath = csvfile
    #print("reading file: {}".format(csvfile))
    #df = pd.read_csv(fpath)
    #dfs.append(df)
   # df = pd.read_csv(file, header=0)
   # df.name = file

def dataframes_to_pickle():
  for f in csv_files:
    filename = f.split("\\", 1)[1]
    df = pd.read_csv(f)
    df.to_pickle("./pickle_files/" + filename + '.pkl')


dataframes_to_pickle()