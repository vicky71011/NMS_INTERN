from load import load
from clean import clean
from analysis import *
from visualize import plot_top_categories

def main():
    df = load("Sales Data Analyzer/data/amazon.csv")    
    df = clean(df)
    df = add_revenue(df)

    print("Total Revenue:", total_revenue(df))

    best = best_selling_product(df)
    print("\nBest Product:")
    print(best['product_name'], best['revenue'])

    categories = top_categories(df)
    print("\nTop Categories:")
    print(categories.head(5))

    print("\nTop 5 Products:")
    print(top_products(df)[['product_name', 'revenue']].head(5))

    plot_top_categories(categories)

if __name__ == "__main__":
    main()