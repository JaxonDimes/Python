people = {
    'james': {
        'first_name': 'James',
        'last_name': 'Dixon',
        'age': '17',
        'city': 'Woodburn'},
    'john': {'first_name': 'John',
             'last_name': 'Doe',
             'age': '18',
             'city': 'Fort Wayne'},
    'jane': {'first_name': 'Jane',
             'last_name': 'Doe',
             'age': '21',
             'city': 'auburn'}
    }
for name, detail in people.items():
    print(f"Name: {name.title()}")
    full_name = f"{detail['first_name']} {detail['last_name']}"
    location = detail['city']
    age = detail['age']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
    print(f"\tAge: {int(age)}")


