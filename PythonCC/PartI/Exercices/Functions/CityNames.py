def describe_city(city_name='El Attaouia', country='Morocco'):
    return f'"{city_name}, {country}"'


print(describe_city())
print(describe_city('Tokyo', 'Japan'))
print(describe_city('Paris', 'Frace'))
