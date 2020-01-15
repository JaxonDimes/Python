from random import choice


def random_variable():
    rand = choice(lottery)
    return rand


lottery = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e']

rand = choice(lottery)
rand2 = choice(lottery)
rand3 = choice(lottery)
rand4 = choice(lottery)

lottery_winner = [rand, rand2, rand3, rand4]
print(lottery_winner)
print(f"Any ticket matching: {lottery_winner} is a winner.")

count = 0

false = True
while false:
    count += 1
    my_ticket = []
    my_ticket.append(random_variable())
    my_ticket.append(random_variable())
    my_ticket.append(random_variable())
    my_ticket.append(random_variable())
    if my_ticket == lottery_winner:
        print(my_ticket)
        print(lottery_winner)
        print("YOU WON THE LOTTERY")
        print(count)
        false = False
