import pandas as pd
import csv
import glob
from datetime import datetime

pickle_path = 'pickle_files'
pickle_files = glob.glob(pickle_path + '/*.pkl')

pitstops_df = pd.read_pickle(pickle_path + './pit_stops.csv.pkl')
races_df = pd.read_pickle(pickle_path + './races.csv.pkl')
driver_df = pd.read_pickle(pickle_path + './drivers.csv.pkl')
results_df = pd.read_pickle(pickle_path + './results.csv.pkl')


def clean_data():
    pitstops_df['duration'] = pd.to_numeric(pitstops_df.duration, errors='coerce')
    return pitstops_df

def transformation_1():
    clean_data()

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

    # group data to get average duration and write to csv file
    analysis_df = analysis_df.groupby(['raceId', 'driverId', 'name', 'forename', 'surname'], as_index=False)['duration'].mean()

    analysis_df.to_csv(
        'etl/transform_files/transformation_1.csv', 
        index=False, 
        encoding='utf-8'
    )


def transformation_2():
    driver_df = driver_df
    driver_df['code'] = driver_df['surname'].str.upper()
    driver_df['code'] = driver_df['code'].str.slice(start=0, stop=3)

    driver_df.to_csv(
        'etl/transform_files/transformation_2.csv', 
        index=False, 
        encoding='utf-8'
    )

def transformation_3(season_year):

    season_year = season_year
    merged_df_1 = races_df.merge(results_df, how='inner', on = 'raceId')
    merged_df_2 = merged_df_1.merge(driver_df, how='inner', on = 'driverId')

    selected_year_df = merged_df_2.loc[merged_df_2['year'] == season_year]

 #pseudo logic:
    #a year (int64) is passed through the function which selects the season to run the analysis
    #select min(season_year_race_date) and max(season_year_race_date)
    #create two columns, the driver's DOB subtracted from the min(season_year_date) and the driver's DOB subtracted  from max(season_year_date)
    # for min(season_year_dat) column, select the driver(s) with youngest/oldest age, and do the same for max(season_year_date)
    # return results to csv

    #exception handling should be implemented in the event that the season_year entered is not within the range of years in the file


