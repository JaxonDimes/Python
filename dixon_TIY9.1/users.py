class User:
    def __init__(self, first_name, last_name, fav_candy, fav_drink):
        self.first_name = first_name
        self.last_name = last_name
        self.fav_candy = fav_candy
        self.fav_drink = fav_drink
        self.attributes = ['add post = True', 'delete post = True', 'ban user = True']

    def describe_user(self):
        print(f"{self.first_name} "
              f"{self.last_name}'s preference of candy is "
              f"{self.fav_candy} and their favorite drink is "
              f"{self.fav_drink}.")

    def greet_user(self):
        print(f"It's nice to see you again, {self.first_name} {self.last_name}.\n")


class Admin(User):
    def show_privileges(self):
        show = Privileges()
        show.show_privilege()


class Privileges:
    def __init__(self):
        self.privileges = ['add post = True', 'delete post = True', 'ban user = True']

    def show_privilege(self):
        for privilege in self.privileges:
            print(privilege)


