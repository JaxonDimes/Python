sandwich_orders = ['Sub', 'deli', 'italian', 'spicy']
finished_sandwiches = []
while sandwich_orders:
    item = sandwich_orders.pop()
    print(f"I made your {item.title()} sandwich.")
    finished_sandwiches.append(item.title())
    print(finished_sandwiches)
    print(sandwich_orders)






