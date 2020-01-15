class Restaurant:
    def __init__(self, restaurant_type, cuisine_type):
        self.restaurant_type = restaurant_type
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_type} is now serving {self.cuisine_type}!")

    def open_restaurant(self):
        print(f"{self.restaurant_type} is now open!")


best_iceCream_restaurant = Restaurant('Dairy Queen', 'Blizzards')
fast_food_restaurant = Restaurant('Burger King', 'Cheeseburgers')
best_restaurant = Restaurant("Wendy's", "Baconator")

best_iceCream_restaurant.describe_restaurant()
fast_food_restaurant.describe_restaurant()
best_restaurant.describe_restaurant()
