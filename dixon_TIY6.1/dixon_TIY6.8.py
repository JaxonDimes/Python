pet_info = {
    'Snivy': {
        'type': 'Grass',
        'animal': 'snake',
        'owner': 'Cyan'},
    'Oshawatt': {
        'type': 'Water',
        'animal': 'sea otter',
        'owner': 'Bianca'},
    'Tepig': {
        'type': 'Fire',
        'animal': 'pig',
        'owner': 'Ash'}
}
for name, info in pet_info.items():
    print(f"Name: {name.title()}")
    type = info['type']
    animal = info['animal']
    owner = info['owner']
    print(f"\tType: {type.title()}")
    print(f"\tAnimal: {animal.title()}")
    print(f"\tOwner: {owner.title()}")
