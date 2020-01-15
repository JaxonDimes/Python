numbers = {
    'favoriteNumbers': ['5', '13', '2', '3000', '17'],
    'people': ['john', 'james', 'joe', 'tony', 'abby']}
for value in range(0, 5):
    print(f"{value + 1}: "
          f" {numbers['people'][value]}'s favorite number is {numbers['favoriteNumbers'][value]}.")
