currentUsers = ['John', 'Doe', 'Jane', 'Mary', 'Admin']
newUsers = ['n00b', 'pl3b', 'John', 'r00k13', 'Admin']
for user in newUsers:
    if user in currentUsers:
        print(f"Hey, {user.title()} has already been used!")
    else:
        print("The username is available.")
