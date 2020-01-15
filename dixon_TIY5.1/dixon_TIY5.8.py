users = ['admin', 'jaden', 'bob', 'karen', 'john']
for people in users:
    if people == 'admin':
        print(f"Hello {people.title()}.")
    else:
        print(f"Hi {people.title()}, thanks for logging back in!")
