true = True
filename = ['cats.txt', 'dogs.txt']
while true:
    try:
        for file in filename:
            with open(file, 'r') as name:
                print(name.read())
                true = False

    except FileNotFoundError:
        print(f"Error 404. File not found.")



