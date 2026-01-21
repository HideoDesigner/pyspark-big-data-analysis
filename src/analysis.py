from spark_session import create_spark_session
from load_data import load_csv
from transform import clean_data, aggregate

spark = create_spark_session()
df = load_csv(spark, "data/sample_data.csv")
df = clean_data(df)
aggregate(df, df.columns[0]).show()
