class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(
            f"Restaurant name is: {self.restaurant_name}, it has {self.cuisine_type} cuisine")

    def open_restaurant(self):
        print("The restaurant is open")


if __name__ == "__main__":
    myRestaurant = Restaurant("Marina", "Moroccan")
    print(myRestaurant.restaurant_name)
    print(myRestaurant.cuisine_type)
    myRestaurant.open_restaurant()
    myRestaurant.describe_restaurant()
