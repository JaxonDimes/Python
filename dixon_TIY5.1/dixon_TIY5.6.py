age = input()
if  int(age) < 2:
    print("You are a baby.")
elif int(age) >= 2 and int(age) < 4:
    print("You are a toddler.")
elif int(age) >= 4 and int(age) < 13:
    print("You a kid now.")
elif int(age) >= 13 and int(age) < 20:
    print("You are a teenager, good luck surviving high school.")
elif int(age) >= 20 and int(age) < 65:
    print("You are an adult.")
elif int(age) >= 65:
    print("You are ancient.")
print(age)
