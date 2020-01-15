import json
#this is the write
filename = 'number.json'
number = input("What's your favorite number: ")

with open(filename, 'w') as f:
    json.dump(number, f)
    print("Thank you. Remember")
