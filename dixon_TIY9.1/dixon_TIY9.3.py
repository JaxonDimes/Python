class User:
    def __init__(self, first_name, last_name, fav_candy, fav_drink):
        self.first_name = first_name
        self.last_name = last_name
        self.fav_candy = fav_candy
        self.fav_drink = fav_drink

    def describe_user(self):
        print(f"{self.first_name} "
              f"{self.last_name}'s preference of candy is "
              f"{self.fav_candy} and their favorite drink is "
              f"{self.fav_drink}.")

    def greet_user(self):
        print(f"It's nice to see you again, {self.first_name} {self.last_name}.\n")


my_user = User('James', 'Dixon', 'Heath', 'Dr.Pepper')
bob_user = User('Bob', 'Pickle', 'Whatchamacallits', 'Coca Cola')
randy_user = User('Randy', 'Newman', 'Chocolate', 'Juice')
abbey_user = User('Abbey', 'Richardson', 'anything Chocolate', 'Coffee')

my_user.describe_user()
my_user.greet_user()

bob_user.describe_user()
bob_user.greet_user()

randy_user.describe_user()
randy_user.greet_user()

abbey_user.describe_user()
abbey_user.greet_user()
