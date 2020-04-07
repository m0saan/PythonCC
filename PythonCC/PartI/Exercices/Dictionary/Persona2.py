persona1 = {
    "first_name": "Mo",
    "last_name": "Boustta",
    "age": 21,
    "city": "El Attaouia"
}

persona2 = {
    "first_name": "Betty",
    "last_name": "Cooper",
    "age": 23,
    "city": "USA"
}
persona3 = {
    "first_name": "David",
    "last_name": "Spouse",
    "age": 29,
    "city": "UK"
}

listOfDict = [persona1, persona2, persona3]
count = 0
for _dict in listOfDict:
    for k, v in _dict.items():
        print(k + " :"+str(v))
    print()
