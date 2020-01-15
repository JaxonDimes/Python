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





