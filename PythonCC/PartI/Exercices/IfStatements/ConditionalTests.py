car = 'subaru'

print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

print("\nIs car != 'subaru'? I predict False.")
print(car != 'subaru')

print("\nIs car.lower() != 'subaru'? I predict True.")
print(car.lower() != 'Subaru')

print("\nIs car == 'subaru' and car.upper() == 'SUBARZ'? I predict True.")
print(car == 'subaru' and car.upper() == 'SUBARU')

cars = ["BMW", "Honda", "Bugati", "Ferrari"]

print("\nIs BMW in cars[]? I predict True")
print("BMW" in cars)

print("\nIs Ford not in cars[]? I predict True")
print("Ford" not in cars)

print("\nIs Ford not in cars[] or BMW in cars[] ? I predict True")
print("Ford" not in cars and "BMW" in cars)
