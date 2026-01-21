def clean_data(df):
    return df.dropna()

def aggregate(df, column):
    return df.groupBy(column).count()
