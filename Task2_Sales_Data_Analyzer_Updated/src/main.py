from load import *
from clean import *
from analysis import *
from visualize import *

def main():
    df = load("Sales_Data_Analyzer_Updated/data/superstore.csv")   

    df = clean(df)
    df = add_revenue(df)


    print("\nRevenue by Product:")
    print(revenue_by_product(df).head(5))

    print("\nRevenue by Category:")
    print(revenue_by_category(df))

    print("\nRevenue by Region:")
    print(revenue_by_region(df))


    monthly = monthly_revenue(df)
    print("\nMonthly Revenue:")
    print(monthly)

 
    print("\nTop Product per Region:")
    print(top_product_per_region(df))

    print("\nCategory Growth:")
    print(category_growth(df).fillna(0))

    print("\nBest Region:", best_region(df))
    print("Worst Month:", worst_month(df))


    prediction = predict_next_month(df)
    print("\nPredicted Next Month Revenue:", prediction)


    region_data = region_trend(df)

    plot_monthly_revenue(monthly)
    plot_region_trend(region_data)


if __name__ == "__main__":
    main()