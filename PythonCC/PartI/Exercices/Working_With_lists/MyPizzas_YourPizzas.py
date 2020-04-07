pizzas = ["Margarita", "Ton", "Vegetarien"]
friend_pizzas = pizzas[:]
pizzas.append("Quatre Fromage")
friend_pizzas.append("Cisilien")

print("My favorite pizzas are : ")
for pizza in pizzas:
    print(pizza)

print("My friend’s favorite pizzas are :")
for friend_pizza in friend_pizzas:
    print(friend_pizza)
