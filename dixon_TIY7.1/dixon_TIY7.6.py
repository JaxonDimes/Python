toppings = []
requests = f"Any more toppings you want? \nHere:"



while True:
    order = input(requests)
    if order == 'quit':
        for topping in toppings:
            print(f"Topping {topping.title()}...")
        break
    else:
        toppings.append(order)


if len(toppings) == 12:
    for topping in toppings:
        print(f"Topping {topping.title()}...")

else:
    toppings.append(order)


while len(toppings) > 6:
    order = input(requests)
    if order == 'quit':
        for topping in toppings:
            print(f"Topping {topping.title()}...")
    else:
        toppings.append(order)










