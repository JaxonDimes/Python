import json


def get_number():
    filename = 'number.json'
    try:
        with open(filename) as f:
            number = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return number


def new_number():
    number = input("Number: ")
    filename = 'number.json'
    with open(filename, 'w') as f:
        json.dump(number, f)
        return number


def greet():
    number = get_number()
    if number:
        print(f"I know your number, it is {number}!")
    else:
        number = new_number()
        print(f"Gotta remember that number, {number}.")

greet()
