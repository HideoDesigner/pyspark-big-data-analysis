from load_data import create_spark_session, load_data
from transform import clean_data, aggregate_data

spark = create_spark_session()
df = load_data(spark, "data/sample_data.csv")
df_clean = clean_data(df)
result = aggregate_data(df_clean)

result.show()
