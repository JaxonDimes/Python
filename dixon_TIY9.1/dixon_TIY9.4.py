class Restaurant:
    def __init__(self, restaurant_type, cuisine_type):
        self.restaurant_type = restaurant_type
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_type} is now serving {self.cuisine_type}!")

    def open_restaurant(self):
        print(f"{self.restaurant_type} is now open!")

    def set_number_served(self, served):
        self.number_served = int(served)
        print(f"You have served {served} people today.")

    def increment_number_served(self, people):
        self.number_served += int(people)
        print(f"You have served {self.number_served} people today.")


restaurant = Restaurant('Burger King', 'Whopper')
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant.set_number_served(15)
restaurant.increment_number_served(16)
restaurant.increment_number_served(4)
restaurant.increment_number_served(-3)









