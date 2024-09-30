
def calculate_tax(item, price, rate):
    print(item,"costs $", "{:.2f}".format(price*rate),"with tax.")

item = input("what item do you want to calculate tax on\n>")
price = float(input("what is the price of the item without tax\n>"))
rate = float(1.06875)

calculate_tax(item,price,rate)