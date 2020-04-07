with open("guest.txt", 'w') as file_object:
    entred_name = input("Enter your name : ")
    file_object.write(entred_name)
