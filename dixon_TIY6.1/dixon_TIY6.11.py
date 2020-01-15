cities = {
    'indianapolis' : {
        'country': 'United States',
        'population': ' 2,028,614',
        'fact': 'The Children’s Museum of Indianapolis is the largest children’s museum in the world.'},
    'Fort Wayne': {
        'country': 'United States',
        'population': '419,453',
        'fact': 'Fort Wayne is known as "the city of churches." How many churches do we have? 360.'},
    'Terre Haute': {
        'country': 'United States',
        'population': '170,943',
        'fact': 'The Crime Rate for this place is 41.38 per 1,000 residents.'
    }
}
for city, place in cities.items():
    print(city.title())
    country = place['country']
    population = place['population']
    fact = place['fact']
    print(f"\t{city.title()} is placed in {country.title()}")
    print(f"\t{city.title()}'s population is {population}.")
    print(f"\tFun Fact about {city.title()}: {fact.title()}")
