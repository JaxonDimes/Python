filename = 'guest.txt'

with open(filename, 'w') as file_write:
    name = input("Name here: ")
    file_write.write(name)
