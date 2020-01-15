rivers = {'nile': 'egypt', 'St. Marys River': 'Fort Wayne', 'Murray': 'australia'}
for water, place in rivers.items():
    print(f"The {water.title()} river runs through {place.title()}.")
for water, place in rivers.items():
    print(f"\n{water.title()}")
    print(f"\t{place.title()}")
