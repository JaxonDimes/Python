favorite_locations = {
    'james': {
        'place1': 'The Attic: Attic in my house where I stash bodies and such.',
        'place2': '7th Period: 7th Period class at Woodlan',
        'place3': 'alone: anywhere where the title follows...'},
    'Mr. McKinstry': {
        'place1': 'The Baseball Field: Progressive Field in Cleveland',
        'place2': 'The Beach: Fernandina Beach Florida',
        'place3': 'here: FWCS Career Academy'},
    'Nikolai': {
        'place1': 'Kino Der Untoten: Theater of the Dead',
        'place2': 'Alpha Omega: Overrun Safe haven in Nevada',
        'place3': 'Tag Der Toten: Day of the Dead (as a tribute to George Romero)'}
    }
for name, info in favorite_locations.items():
    print(f"Name: {name.title()}")
    locations = f"\t{info['place1']}"
    locations2 = f"\t{info['place2']}"
    locations3 = f"\t{info['place3']}"
    print(locations)
    print(locations2)
    print(locations3)

