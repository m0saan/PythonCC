print("Enter two numbers : ")
try:
    num1 = int(input(">> "))
    num2 = int(input(">> "))
except ValueError:
    print("You should enter only numeric values!")
else:
    res = int(num1) + int(num2)
    print(res)
