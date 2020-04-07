numbers = list(range(1, 10))

for num in numbers:
    if num == 1:
        s = "st"
    elif num == 2:
        s = "nd"
    elif num == 3:
        s = "rd"
    else:
        s = "th"
    print(str(num) + s)
