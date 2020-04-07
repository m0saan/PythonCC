def city_country(city, country, population=0):
    if population:
        return f"{city}, {country} - population {population}".title()
    return f"{city}, {country}".title()


if __name__ == "__main__":
    print(city_country("tokyo", "japan", 10000000))
