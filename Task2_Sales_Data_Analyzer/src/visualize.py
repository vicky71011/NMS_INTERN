import matplotlib.pyplot as plt

def plot_top_categories(category_sales):
    category_sales.head(5).plot(kind='bar')
    plt.title("Top Categories by Revenue")
    plt.ylabel("Revenue")
    plt.show()