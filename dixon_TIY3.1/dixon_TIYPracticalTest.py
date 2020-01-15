print("Type in your favorite candy below!")
index = [input()]
list = []
for candy in index:
    if candy == '':
        index.remove('')
        for item in index:
            list.append(item.title())
        print(f"Candy: {list}")
    else:
        index.append(input())
