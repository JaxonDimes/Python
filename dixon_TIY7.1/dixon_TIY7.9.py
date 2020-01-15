sandwich_orders = ['Beef Sub', 'pastrami', 'Xtra Crust', 'pastrami', 'pastrami']
print("The deli has ran out of pastrami...")

print(sandwich_orders)
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    #print("Sorry we ran out of pastrami...")

print(sandwich_orders)







