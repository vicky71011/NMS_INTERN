# Sales Data Analyzer

## About the Project

This project analyzes sales data to understand product performance, regional trends, and overall business insights. It also predicts future sales using simple logic.

---

## Goal

* Clean the dataset
* Calculate revenue
* Analyze trends
* Generate insights
* Predict next month sales

---

## Dataset Columns

The dataset contains the following important fields:

* Category → Type of product
* Product_Name → Name of the product
* Order_Date → Date of purchase
* Price → Selling price
* Quantity → Number of units sold
* Region → Sales region
* Profit → Profit from sales
* City, State, Country → Location details
* Segment → Customer segment

---

## Project Structure

src/
│
├── load.py        # Load dataset
├── clean.py       # Clean and preprocess data
├── analysis.py    # Perform analysis
├── visualize.py   # Plot graphs
└── main.py        # Run the project

---

## Data Cleaning

* Converted `Order_Date` to datetime
* Converted `Price` and `Quantity` to numeric
* Removed missing/invalid values
* Extracted:
  * month
  * day

---

## Analysis Done

### Revenue Analysis

* Revenue by product
* Revenue by category
* Revenue by region

---

### Trends

* Monthly revenue
* Region-wise performance over time

---

### Insights

* Top product in each region
* Category growth (month-over-month)
* Best performing region
* Worst performing month

---

## Prediction

Next month sales is predicted using:

* Average growth of last 3 months

---

## Visualization

* Monthly revenue trend (line chart)
* Region-wise revenue trend

---

## How to Run

python main.py

---

## Tools Used

* Python
* Pandas
* Matplotlib

---

## Conclusion

This project helps in understanding sales patterns and making basic predictions using simple data analysis techniques.

---