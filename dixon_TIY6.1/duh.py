friends = {
    'first_name': ['Hayden', 'Aung', 'Tristan', 'Jackson', 'Nick', 'Tarron'],
    'last_name': ['Heche', 'Han', 'Taylor', 'Foote', 'Tucker', 'White'],
    'age': ['18', '17', '17', '17', '18', '16'],
    'city': ['Fort Wayne', 'Fort Wayne', 'Garret', 'Fort Wayne', ' Leo', 'Fort Wayne']}

for value in range(0, 6):
    print(f"Friend {value + 1}: "
          f"{friends['first_name'][value]},"
          f" {friends['last_name'][value]},"
          f" {friends['age'][value]},"
          f" {friends['city'][value]}")

dealer = ['Focus', 'Explorer', 'F150', 'Fusion', 'Mustang', 'Edge', 'Taurus', 'Flex']
wants = ['Explorer', 'Trail Blazer', 'F150']
unavailable = []
inventory = []
for car in dealer:
    if car in wants:
        print(f"{car} is in stock.")
        inventory.append(car)
    else:
        unavailable.append(car)
print("\nThese are your cars in stock:")
print(inventory)
print("\nThese cars are not in your wants:")
print(unavailable)

