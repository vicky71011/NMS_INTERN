import pandas as pd


def clean(df):
    df['discounted_price'] = df['discounted_price'].replace('[₹,]', '', regex=True).astype(float)
    df['actual_price'] = df['actual_price'].replace('[₹,]', '', regex=True).astype(float)

    df['rating_count'] = df['rating_count'].replace(',', '', regex=True)
    df['rating_count'] = pd.to_numeric(df['rating_count'], errors='coerce')

    df['rating'] = pd.to_numeric(df['rating'], errors='coerce')

    df = df.dropna(subset=['discounted_price', 'rating_count'])

    return df