from random import choice
lottery = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e']

rand = choice(lottery)
rand2 = choice(lottery)
rand3 = choice(lottery)
rand4 = choice(lottery)

lottery_winner = [rand, rand2, rand3, rand4]
print(lottery_winner)
print(f"Any ticket matching: {lottery_winner} is a winner.")
