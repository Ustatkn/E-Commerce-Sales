import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/sales.csv",encoding="latin-1")
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"],format="%m/%d/%y %H:%M")
df.set_index("InvoiceDate",inplace=True)

df = df[(df["Quantity"]>0) & (df["UnitPrice"]>0)] 

df["TotalRevenue"] = df["Quantity"]*df["UnitPrice"]

def monthly_sale_bar_graphic():
    monthly_sale = df.resample('ME')["TotalRevenue"].sum()
    monthly_sale.index = monthly_sale.index.strftime("%Y-%m")
    monthly_sale.plot(kind='bar',title='Monthly Sale',xlabel='Months',ylabel='Sales')
    plt.tight_layout()
    plt.savefig("outputs/plots/monthly_sales.png")
    plt.show()

def countries_total_revenue():
    total_country_revenue = df.groupby("Country")["TotalRevenue"].sum().sort_values(ascending=False)
    total_country_revenue.plot(kind='bar',title="Country's Total Revenue",xlabel="Countries",ylabel="Total Revenue")
    plt.tight_layout()
    plt.savefig("outputs/plots/top_countries_revenue.png")
    plt.show()

def total_basket_amounts():
    each_orders_amount = df.groupby('InvoiceNo')["TotalRevenue"].sum()
    each_orders_amount.plot(kind='hist',bins=100,title="Total basket amount's",xlabel='Basket Amounts')
    plt.tight_layout()
    plt.savefig("outputs/plots/basket_amount_hist.png")
    plt.show()