def sandwich(items, size = 12):
    true = True
    while true:
        if items != 'quit':
            list.append(items)
            sandwich(input("Toppings: "))
        elif items == 'quit':
            for item in list:
                print(item)
            print(f"Size = {12}")
            true = False

list = []
sandwich(input("Toppings: "))
