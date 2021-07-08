import pandas as pd
import csv
import pyspark as pyspark
import glob as glob
import findspark
findspark.find()
from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local[1]").appName("testApp").getOrCreate()
csv_path = "../data/circuits.csv"
df = spark.read.format("csv").load(csv_path).limit(10)
print(df.collect())

#path = 'sample_data'
#files = glob.glob(path + "/*.csv")


#def extract():
 #   for filename in files:
#      data = pd.read_csv(filename)
        
