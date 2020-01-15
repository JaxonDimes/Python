list = ['Robert Downey Jr.', 'Scarlett Johanson', 'Abby']
message = f"Hello {list[0].title()}, you are invited to dinner."
print(message)
message = f"Hello {list[1].title()}, you are invited to dinner."
print(message)
message = f"Hello {list[2].title()}, you are invited to a dinner."
print(message)
uhoh = f"\noh no, {list[0].title()} couldnt make it."
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
print("\n Wait a minute, I have a bigger table.")
list.insert(0, 'John Wick')
list.insert(2, 'Creeper, aww man')
list.append('THE HOLY hAnDgReNaDe')
message = f"\nHello {list[0].title()}, you are invited to dinner, again."
print(message)
message = f"Hello {list[1].title()}, you are invited to dinner, again."
print(message)
message = f"Hello {list[2].title()}, you are invited to a dinner, again."
print(message)
message = f"Hello {list[3].title()}, you are invited to dinner, again."
print(message)
message = f"Hello {list[4].title()}, you are invited to dinner, again."
print(message)
message = f"Hello {list[5].title()}, you are invited to a dinner, again."
print(message)
print("\nWell crap, Amazon wont deliver my table in the same day.")
john = list.pop(0)
print(f"\nSorry {john.title()}, not enough space now.")
steve = list.pop(0)
print(f"Sorry {steve.title()}, you have been deleted.")
creeper = list.pop(0)
print(f"{creeper.title()} your invitation blew up.")
blackWidow = list.pop(0)
print(f"{blackWidow.title()}, your invite has been revoked.")
print(f"\n{list[0]}, you are still invited.")
print(f"{list[1]}, you are still wOrThY.")
del list[0]
del list[0]
print(list)
