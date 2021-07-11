import pandas as pd
import csv
import glob
from datetime import datetime

pickle_path = 'pickle_files'
pickle_files = glob.glob(pickle_path + '/*.pkl')

pitstops_df = pd.read_pickle(pickle_path + './pit_stops.csv.pkl')
races_df = pd.read_pickle(pickle_path + './races.csv.pkl')
driver_df = pd.read_pickle(pickle_path + './drivers.csv.pkl')



def transform_data():
    pitstops_df['duration'] = pd.to_numeric(pitstops_df.duration, errors='coerce')
    return pitstops_df

def analyze_data():
    transform_data()

    #merges pitstops and races on raceId to bring in race name
    merged_df_1 = pitstops_df.merge(races_df, how='inner', on = 'raceId')
    merged_df_2 = merged_df_1.merge(driver_df, how='inner', on = 'driverId')
    new_df_cols = merged_df_2.columns.tolist()

    if 'driverId' and 'raceId' and 'forename' and 'surname' and 'name' in new_df_cols:
        print('driverId, raceId, forename, surname, and name exist in new dataframe.')
    else:
        print('One or more columns are missing.')

    if 'duration' in new_df_cols and merged_df_2['duration'].dtype == 'float64':
        print('duration exists in dataframe and datatype is float.')
    else:
        print('duration does not exist in dataframe')

    analysis_df = merged_df_2[['raceId', 'driverId', 'name', 'forename', 'surname', 'duration']]



print(merge_data())


