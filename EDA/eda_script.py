import pandas as pd
import csv as csv
import glob


#Script that loops through sample CSV data and writes EDA results to .txt file

path = 'sample_data'
files = glob.glob(path + "/*.csv")

def eda():
    try:
        print("Writing sample data exploratory analysis to file 'eda_info.txt'...")
        with open('eda_info.txt', 'w') as f:
            for filename in files:
                f.write(filename + "\n")
                data = pd.read_csv(filename)
                data.info(verbose = True, buf=f)
        print("File successfully written!")
    except:
        print("File not found.")

eda()