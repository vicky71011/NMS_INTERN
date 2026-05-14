import matplotlib.pyplot as plt

def plot_monthly_revenue(monthly):
    monthly.plot(kind='line', marker='o')
    plt.title("Monthly Revenue Trend")
    plt.ylabel("Revenue")
    plt.xticks(rotation=45)
    plt.show()


def plot_region_trend(region_data):
    region_data.plot()
    plt.title("Region-wise Revenue Trend")
    plt.ylabel("Revenue")
    plt.xticks(rotation=45)
    plt.show()