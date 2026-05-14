### Sales Data Analyzer

## Overview
This project analyzes Amazon product data to estimate revenue, identify best-selling products, and understand category performance.

## Dataset
Amazon product dataset including:
- Product name
- Price
- Rating
- Rating count

## Features
- Total revenue estimation
- Best-selling product detection
- Category-wise revenue analysis
- Data visualization

## Insights
- Smartphones contribute the majority of revenue due to high demand and pricing.
- Accessories generate lower revenue despite high usage.
- Rating count can act as a proxy for product popularity.
- Electronics dominate the market compared to peripherals.

## Assumptions
Revenue = discounted_price × rating_count  

## Project Structure
- data/ → dataset
- src/ → source code
- outputs/ → reports & charts

## How to Run
pip install -r requirements.txt
python src/main.py