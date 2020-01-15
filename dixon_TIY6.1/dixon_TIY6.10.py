numbers = {
    'john': {'1','2','3','4'},
    'james': {'13','7'},
    'joe': {'15', '91'},
    'tony': {'3000'},
    'abbey': {'17', '74'},
    }
for value, item in numbers.items():
    print(f"{value.title()}'s favorite numbers are:")
    for index in item:
        print(f"\t{index}")



#'favoriteNumbers': ['5', '13', '2', '3000', '17', '69'],
#'people': ['john', 'james', 'joe', 'tony', 'abby', 'n00bmaster69']
