# Score Average for Mario Kart
print("What is the designated course amount?")
scores = []
scoresLength = len(scores)
raceAmount = input()
raceScore = input()
if int(raceAmount) == 1:
    print("Wait a minute, your race is your average!")
elif int(raceAmount) == 0:
    print(f"You cannot have {raceAmount} races in Mario Kart.")
elif int(raceAmount) >= 2 and int(raceAmount) <= 32:
    print(f"{raceAmount} Races, Please put in the scores:")
