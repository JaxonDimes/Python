dict = {'first_name': 'James',
        'last_name': 'Dixon',
        'age': '17',
        'city': 'Woodburn'}
print(f"Hello "
      f"{dict['first_name']} "
      f"{dict['last_name']}, you are "
      f"{dict['age']} years old and reside in "
      f"{dict['city']}.")
for item in dict.items():
    print(f"{item}")
