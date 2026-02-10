import analysis as asis
import visualization as vs

def main():
    print("------E-Commerce Sale Analysis------\n")

    while True:
        print("1- How many customers ordered items from our E-Commerce Site, and what is the Customer Code of the customer who is ordered more items than the others?")
        print("2- How many different countries placed orders, and which country has the most total revenue of orders?")
        print("3- How many orders are there in each month, and which month has maximum orders?")
        print("4- Show the general mathematical results in the data set.")
        print("5- Average basket amount")
        print("6- Each customer’s percentage share of total revenue")
        print("7- Rate of refunded items")
        print("8- Monthly order's bar graphic")
        print("9- Each country's bar graphic of total revenues")
        print("10- Total basket amount's histogram graphic")
        print("0-Exit\n")
        try:
            choice = int(input("Please enter the number of the operation you want to run:\n"))
            
            if choice==1:
                print("There are total ")
                print(asis.total_customer())
            elif choice==2:
                print(asis.total_countries())
            elif choice==3:
                print(asis.monthly_orders())
            elif choice==4:
                print(asis.math_results())
            elif choice==5:
                print(asis.avrg_basket_amount())
            elif choice==6:
                print(asis.revenue_distribution_percentages())
            elif choice==7:
                print(asis.rate_refund_items())
            elif choice==8:
                vs.monthly_sale_bar_graphic()
            elif choice==9:
                vs.countries_total_revenue()
            elif choice==10:
                vs.total_basket_amounts()
            elif choice==0:
                print("Exiting...")
                break
            else:
                print("Please enter a number between 0-10\n")
        except ValueError:
            print("Please enter a valid number!\n")
        
        input("\nPlease enter to continue...")

if __name__ == "__main__":
    main()