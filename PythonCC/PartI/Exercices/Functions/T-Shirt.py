def make_shirt(size, message):
    print("Your T-Shirt size is " + size +
          f" and {message} will be printed on it.")


print("Call the function using positional arguments.")
make_shirt('L', 'Keep calm and learn Python!')

print()

print("Call the function using keyword arguments.")
make_shirt(message='Keep calm and learn Python!', size='L')
