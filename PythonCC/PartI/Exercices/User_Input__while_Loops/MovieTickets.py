while True:
    print("Enter 'quit' to quit the program")
    age = input("Enter you age :")
    if age == 'quit':
        break
    age = int(age)
    if age < 3:
        cost = 0
    elif age >= 3 and age <= 12:
        cost = 10
    else:
        cost = 15
    print(f"the cost of their movie ticket is ${cost}.")
