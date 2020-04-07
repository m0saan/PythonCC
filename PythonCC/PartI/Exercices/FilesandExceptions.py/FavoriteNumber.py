import json
filename = "favorite.json"


def get_number():
    try:
        num = int(input("Enter a number : "))
    except ValueError:
        print("Please enter a valid numeric value (number)!")
    else:
        try:
            with open(filename, 'w') as f_obj:
                json.dump(num, f_obj)
        except FileNotFoundError:
            print("No such file or directory")


def read_value():
    try:
        with open(filename) as f_obj:
            number = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return number


if __name__ == "__main__":
    get_number()
    read_value()
