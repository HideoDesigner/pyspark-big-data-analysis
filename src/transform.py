def clean_data(df):
    return df.dropna()

def aggregate_data(df):
    return df.groupBy("category").count()
