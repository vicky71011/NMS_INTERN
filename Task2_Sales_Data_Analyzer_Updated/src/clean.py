import pandas as pd

def clean(df):
    df['Order_Date'] = pd.to_datetime(df['Order_Date'], errors='coerce')

    df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
    df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')

    df = df.dropna(subset=['Order_Date', 'Price', 'Quantity', 'Product_Name', 'Category', 'Region'])

    df = df[(df['Price'] > 0) & (df['Quantity'] > 0)]

    df['month'] = df['Order_Date'].dt.to_period('M')
    df['day'] = df['Order_Date'].dt.day

    return df