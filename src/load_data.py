from pyspark.sql import SparkSession

def create_spark_session(app_name="BigDataApp"):
    return SparkSession.builder.appName(app_name).getOrCreate()

def load_data(spark, path):
    return spark.read.csv(path, header=True, inferSchema=True)
