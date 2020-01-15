list = ['Robert Downey Jr.', 'Scarlett Johanson', 'Abby']
message = f"Hello {list[0].title()}, you are invited to dinner."
print(message)
message = f"Hello {list[1].title()}, you are invited to dinner."
print(message)
message = f"Hello {list[2].title()}, you are invited to a dinner."
print(message)
uhoh = f"oh no, {list[0].title()} couldnt make it."
print(uhoh)
didnt_arrive = 'Robert Downey Jr.'
list.remove(didnt_arrive)
list.insert(0, 'Steve? from Minecraft')
message = f"\nHello {list[0].title()}, you are invited to dinner."
print(message)
message = f"Hello {list[1].title()}, you are invited to dinner."
print(message)
message = f"Hello {list[2].title()}, you are invited to a dinner."
print(message)

