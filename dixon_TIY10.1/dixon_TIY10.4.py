filename = 'guest_book.txt'

with open(filename, 'w') as object:
    true = True
    while true:
        name = input("Name here please: ")
        if name != 'quit':
            print(f"Thank you {name} for visiting.")
            object.write(f"{name} visited recently.\n")
        elif name == 'quit':
            print("Thank you all.")
            true = False
