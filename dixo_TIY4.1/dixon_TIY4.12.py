my_drinks = ['Dr. Pepper', 'Mt. dew', 'Pepsi']
print("My drinks are:")
for item in my_drinks:
    print(item)
print("\nMy friends drinks are:")
friend_drinks = my_drinks[:]
friend_drinks.append('water')
for item in friend_drinks:
    print(item)
