active = True
while active:
    entredToping = input("Enter a topping or 'quit' to stop the program : ")
    if entredToping == 'quit':
        active = False
    print(f"{entredToping} is added to your pizza")
