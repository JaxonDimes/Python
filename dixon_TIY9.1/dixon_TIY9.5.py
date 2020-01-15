class User:
    def __init__(self, first_name, last_name, fav_candy, fav_drink):
        self.first_name = first_name
        self.last_name = last_name
        self.fav_candy = fav_candy
        self.fav_drink = fav_drink
        self.login_attempts = 0

    def describe_user(self):
        print(f"{self.first_name} "
              f"{self.last_name}'s preference of candy is "
              f"{self.fav_candy} and their favorite drink is "
              f"{self.fav_drink}.")

    def greet_user(self):
        print(f"It's nice to see you again, {self.first_name} {self.last_name}.\n")

    def show_login_attempts(self):
        variable = int(self.login_attempts)
        print(f"You have {variable} login attempts.")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f"Login attempts reduced to {self.login_attempts}.")


my_user = User('James', 'Dixon', 'Heath', 'Dr.Pepper')

print(my_user.login_attempts)
my_user.increment_login_attempts()
my_user.increment_login_attempts()
my_user.increment_login_attempts()
my_user.increment_login_attempts()
my_user.increment_login_attempts()
my_user.increment_login_attempts()
my_user.increment_login_attempts()
my_user.increment_login_attempts()
my_user.show_login_attempts()
my_user.reset_login_attempts()
my_user.show_login_attempts()



