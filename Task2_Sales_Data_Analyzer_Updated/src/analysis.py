def add_revenue(df):
    df['revenue'] = df['Price'] * df['Quantity']
    return df


def revenue_by_product(df):
    return df.groupby('Product_Name')['revenue'].sum().sort_values(ascending=False)


def revenue_by_category(df):
    return df.groupby('Category')['revenue'].sum().sort_values(ascending=False)


def revenue_by_region(df):
    return df.groupby('Region')['revenue'].sum().sort_values(ascending=False)


def monthly_revenue(df):
    return df.groupby('month')['revenue'].sum().sort_index()


def region_trend(df):
    return df.groupby(['month', 'Region'])['revenue'].sum().unstack()


def top_product_per_region(df):
    return df.groupby(['Region', 'Product_Name'])['revenue'].sum().reset_index().sort_values(['Region', 'revenue'], ascending=[True, False]).groupby('Region').head(1)


def category_growth(df):
    monthly = df.groupby(['month', 'Category'])['revenue'].sum().unstack()
    return monthly.pct_change()


def best_region(df):
    return revenue_by_region(df).idxmax()


def worst_month(df):
    return monthly_revenue(df).idxmin()


def predict_next_month(df):
    monthly = monthly_revenue(df)

    growth = monthly.pct_change().dropna()

    avg_growth = growth.tail(3).mean()

    last_month = monthly.iloc[-1]

    predicted = last_month * (1 + avg_growth)

    return predicted