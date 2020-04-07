class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(
            f"Restaurant name is: {self.restaurant_name}, it has {self.cuisine_type} cuisine")

    def open_restaurant(self):
        print("The restaurant is open")

    def set_number_served(self, served_people):
        self.number_served = served_people

    def increment_number_served(self, served_people):
        self.number_served += served_people


if __name__ == "__main__":
    restaurant = Restaurant("Marina", "Moroccan")
    print("Surved People : " + str(restaurant.number_served))
    print("------------------------")

    restaurant.number_served = 13
    print("Surved People : " + str(restaurant.number_served))
    print("------------------------")

    restaurant.increment_number_served(60)
    print("Surved People : " + str(restaurant.number_served))
