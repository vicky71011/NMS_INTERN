def add_revenue(df):
    df['revenue'] = df['discounted_price'] * df['rating_count']
    return df


def total_revenue(df):
    return df['revenue'].sum()


def best_selling_product(df):
    return df.sort_values(by='revenue', ascending=False).iloc[0]


def top_categories(df):
    return df.groupby('category')['revenue'].sum().sort_values(ascending=False)


def top_products(df):
    return df.sort_values(by='revenue', ascending=False)