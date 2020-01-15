try:
    one = input("Enter the first number: ")
    two = input("Enter the second number: ")
    print(int(one) + int(two))

except ValueError:
    print("You can not add a string.")
