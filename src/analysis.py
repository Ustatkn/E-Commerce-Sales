import pandas as pd
import numpy as np


df = pd.read_csv("data/sales.csv",encoding="latin-1")
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"],format="%m/%d/%y %H:%M")
df.set_index("InvoiceDate",inplace=True)

total_items_before_filtering = df["Quantity"].abs().sum()
refund_items = -df[df["Quantity"]<0]["Quantity"].sum()                      # I calculated total refunded items.
df = df[(df["Quantity"]>0) & (df["UnitPrice"]>0)]                           # we cleaned data set from refund items and zeros in the unit price section.

df["TotalRevenue"] = df["Quantity"]*df["UnitPrice"]

def total_customer():
    uniqe_customers = df["CustomerID"].nunique()
    customer_revenue = df.groupby("CustomerID")["TotalRevenue"].sum()
    max_revenue_customer = customer_revenue.idxmax()
    max_revenue = customer_revenue.max()
    return f"There are total {uniqe_customers} customers in the dataset.\n\n{max_revenue_customer} customer ID has the maximum revenue which is {max_revenue}"


def total_countries():
    uniqe_countries = df["Country"].nunique()
    total_countries = df.groupby("Country")["TotalRevenue"].sum()
    max_order_country = total_countries.idxmax()
    max_order = total_countries.max()
    return f"There are {uniqe_countries} countries in the data set\n\n{max_order_country} has the most revenue which is {max_order}"

def monthly_orders():
    monthly_orders = df.resample('ME')["InvoiceNo"].nunique()
    max_order_month = monthly_orders.idxmax()
    max_order_month.strftime("%y-%m")
    total_orders = monthly_orders.max()
    return f"These are orders in each months\n{monthly_orders}\n\nMax number of orders is total {total_orders} orders in {max_order_month}"

def math_results():
    return df.describe()

def avrg_basket_amount():
    basket_totals = df.groupby("InvoiceNo")["TotalRevenue"].sum().values
    avrg_basket = (np.mean(basket_totals)).round(2)
    return f"Average basket amount: {avrg_basket}"

def revenue_distribution_percentages():
    df_cust = df.dropna(subset=["CustomerID"]).copy()
    df_cust["CustomerID"] = df_cust["CustomerID"].astype(int)
    total_revenue = df_cust["TotalRevenue"].sum()
    each_customer_revenue = df_cust.groupby("CustomerID")["TotalRevenue"].sum()
    revenue_percentages = ((each_customer_revenue/total_revenue)*100).round(2)
    return f"Percentage distribution of total revenue by customer:\n{revenue_percentages}"

def rate_refund_items():
    rating = ((refund_items/total_items_before_filtering)*100).round(2)
    return f"Refund rate (by items): {rating}%"