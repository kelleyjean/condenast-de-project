import pandas as pd
import csv
import glob
import os

path = 'sample_data'
files = glob.glob(path + "/*.csv")

path_1 = os.getcwd()
csv_files = glob.glob(os.path.join(path, "*.csv"))

#Function loops through list of files in sample folder and stores each file as a pandas dataframe
def get_file_count():
    file_list = []
    for filename in files:
      file_list.append(filename)   
    file_count = len(file_list)
    return file_count

#Function returns count of files and loops through to store each csv as a dataframe
def store_dataframes():
  dfs = list()
  for csvfile in files:
    fpath = csvfile
    print("reading file: {}".format(csvfile))
    df = pd.read_csv(fpath)
    dfs.append(df)
   # df = pd.read_csv(file, header=0)
   # df.name = file

def trying():
  for f in csv_files:
    filename = f.split("\\", 1)[1]
    df = pd.read_csv(f)
    df.to_pickle("./pickle_files/" + filename + '.pkl')


trying()