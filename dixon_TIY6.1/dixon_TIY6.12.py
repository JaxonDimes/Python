pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}
print("REQUESTs PLEASE:")
request = input()
if request == '':
    print("Aight then, here ya go.")
else:
    pizza['toppings'].append(request)
print(f"You ordered a {pizza['crust']}-crust pizza"
      f" with the following toppings:")
for topping in pizza['toppings']:
    print(f"\t{topping.title()}")
print("Would you like anything else?")




