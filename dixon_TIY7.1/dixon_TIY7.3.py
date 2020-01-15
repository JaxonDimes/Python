number = int(input("Please render a number that may or may not be a multiple of ten: "))
if number % 10 == 0:
    print(f"Looks like {number} is a multiple of ten.")
else:
    print("Not a multiple...")
