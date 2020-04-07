riverNames = {'nile': 'egypt', 'forat': 'bahrien', 'mississippi': 'usa'}

for k in riverNames:
    if k == 'nile':
        print("The Nile runs through Egypt.")
    elif k == 'forat':
        print("The Forat runs through Bahrien.")
    else:
        print("Mississippi runs through United states.")

print("\n")
for key in riverNames.keys():
    print(key)

print("\n")
for value in riverNames.values():
    print(value)
