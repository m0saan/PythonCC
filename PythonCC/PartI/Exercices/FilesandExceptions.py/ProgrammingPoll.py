filename = "Poll.txt"
print("Enter 'q' to quits")
with open(filename, 'w') as file_object:
    while True:
        entred_name = input("Why you like programming : ")
        if entred_name == 'q':
            break
        file_object.write(entred_name + "\n")
