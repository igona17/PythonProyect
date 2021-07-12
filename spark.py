import sys
from pyspark.sql import *

spark = SparkSession\
    .builder\
    .appName("Simple Application")\
    .master("local[*]")\
    .getOrCreate()

a = sys.stdin.readline()

df = spark \
        .read \
        .option("delimiter", ",") \
        .option("header", "true") \
        .option("inferSchema", "true") \
        .csv(f"{a}")
df.show(df.count(), False)
sys.stdout