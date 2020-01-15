class Restaurant:
    def __init__(self, restaurant_type, cuisine_type):
        self.restaurant_type = restaurant_type
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_type} is now serving {self.cuisine_type}!")

    def open_restaurant(self):
        print(f"{self.restaurant_type} is now open!")


restaurant = Restaurant(input("Restaurant: "), input("Cuisine: "))
restaurant.describe_restaurant()
restaurant.open_restaurant()


