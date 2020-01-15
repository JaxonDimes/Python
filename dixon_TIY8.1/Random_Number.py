
dice = [1, 2, 3, 4, 5, 6]


stop = input("say when: ")
sop = True
while sop:
    if stop == 'quit':
        print(dice)
        sop = False
    else:
        for number in dice:
            stop = input("say when: ")
            dice.append(number)



