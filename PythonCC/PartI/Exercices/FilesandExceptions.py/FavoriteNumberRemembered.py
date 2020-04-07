import json
from FavoriteNumber import get_number, read_value


def combined():
    number = read_value()
    if number:
        print(f"I know your favorite number! It’s {number}.")
    else:
        get_number()


if __name__ == "__main__":
    combined()
