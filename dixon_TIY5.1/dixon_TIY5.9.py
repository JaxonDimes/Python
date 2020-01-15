users = []
if users:
    for people in users:
        if people != 'admin':
            print(f"Hi {people.title()}, thanks for logging back in!")
        elif people == 'admin':
            print(f"Hello {people.title()}.")
else:
    print("We need to find some users.")


# 'admin', 'jaden', 'bob', 'karen', 'john'
