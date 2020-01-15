numberPeople = int(input("How many people are attending you at a table? \nHere: "))
if numberPeople <= 7:
    print(f"Ah, yes. Your table of {numberPeople} is here...")
else:
    print(f"Oop, you are going to have to wait. We do not have a table for {numberPeople}, sorry.")
