filename = "guest_book.txt"
print("Enter 'q' to quits")
with open(filename, 'w') as file_object:
    while True:
        entred_name = input("Enter your name : ")
        if entred_name == 'q':
            break
        print(f"Hello there {entred_name}")
        file_object.write(entred_name.strip() + "\n")
