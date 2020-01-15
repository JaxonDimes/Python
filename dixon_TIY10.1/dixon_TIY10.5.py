filename = 'poll_response.txt'

with open(filename, 'w') as item:
    true = True

    while true:
        ask = input("Why do you like programming?\n::")
        if ask == 'quit':
            print("Thank you for your response.")
            true = False
        else:
            item.write(f"{ask}\n")

