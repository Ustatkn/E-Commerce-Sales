# E-Commerce Sales Analysis (Pandas / NumPy / Matplotlib)

This project analyzes an e-commerce sales dataset using **Pandas**, **NumPy**, and **Matplotlib**.  
It provides a simple **menu-based console application** to explore key sales metrics and visualizations.

---

## Dataset Columns
The dataset contains the following columns:

- InvoiceNo
- StockCode
- Description
- Quantity
- InvoiceDate
- UnitPrice
- CustomerID
- Country

---

## Data Cleaning
Before analysis, the dataset is cleaned with the following steps:

- Transactions with **Quantity < 0** are treated as **refunds**.
- Only valid sales are used for revenue analysis:
  - `Quantity > 0`
  - `UnitPrice > 0`
- Some rows have missing `CustomerID` values.
  - These rows are excluded only from customer-level analyses.

---

## Features (Menu Options)

### Analysis
- Total number of customers and the top customer by total revenue
- Total number of countries and the top country by total revenue
- Monthly order counts and the month with maximum orders
- General dataset statistics (`describe()`)
- Average basket amount
- Percentage distribution of total revenue by customer
- Refund rate (by items)

### Visualizations
- Monthly total revenue bar chart
- Top countries by total revenue bar chart
- Basket amount distribution histogram

---

## Plot Outputs

All generated plots are saved into:

text
outputs/plots/

## Installation

```bash
pip install -r requirements.txt