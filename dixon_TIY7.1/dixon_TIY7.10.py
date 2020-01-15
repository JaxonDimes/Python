responses = { 'McKinstry': 'a Sailboat in the Caribbean Sea..'}

activePolling = True

while activePolling:
    name = input("What is your name? ")
    vacationSpot = input("What would be your select vacation spot if you were given the option? ")
    responses[name] = vacationSpot
    iteration = input("Would another person respond? (Ya/no)")
    if iteration == 'no' or 'No' or 'nO' or 'NO':
        activePolling = False
print("\n////////// RESULTS \\\\\\\\\\\\\\\\\\\\")
for name, spot in responses.items():
    print(f"{name.title()} really wants to be in {spot.title()}")
