import json


def get_username():
    filename = 'username.json'
    try:
        with open(filename, 'r') as f:
            username = json.load(f)
    except FileNotFoundError:
        print("Cannot find name.")
    else:
        return username


def new_username():
    username = input("Name please: ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
        return username


def greet():
    username = get_username()
    if username:
        print(f"Welcome back, {username}!")
    elif not username:
        username = new_username()
        print(f"Come again, {username}.")

greet()
