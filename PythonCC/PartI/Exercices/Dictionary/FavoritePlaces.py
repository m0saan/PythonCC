favorite_places = {
    'MO': ['Chafchawen', 'Nadour', 'Dakhla'],
    'Yukinon': ['Tokyo', 'Fuji Mountain', 'Kyoto'],
    'Betty': ['Silicon Valley', 'Alaska', 'NewYork'],
}


for key, value in favorite_places.items():
    print(key + "'s favourite places are : ")
    for item in value:
        print(item)
    print()
