class User():

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        print("User's fullname is " + self.first_name
              + ' ' + self.last_name + f" he is {self.age} years old.")

    def greet_user(self):
        print(f"Hello there {self.first_name} {self.last_name}. What is up!")


user1 = User("Mo", "Boustta", 21)
user1.describe_user()
user1.greet_user()
