cost = input("What is the cost of the crypto?")
user_cost = float(cost)
quantity = input("what is the quantity of cryptos do you want?")
user_quantity = float(quantity)

total_cost = user_cost * user_quantity

if total_cost < 20:
    print("You need to buy more cryptos you cheap ass")

else:
    print(total_cost)