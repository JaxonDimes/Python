import json


def get_username():
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def new_username():
    username = input("Name: ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username


def greet_user():
    username = get_username()
    if username:
        print(f"Welcome back, {username}.")
    else:
        username = new_username()
        print(f"Come back soon, {username}.")


greet_user()
