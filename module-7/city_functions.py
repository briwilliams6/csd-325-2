#Assignment 7.2
def location(city, country, population=None, language=None):
#will return string such as Santiago, Chile
    if population and language:
        return f"{city.strip().title()}, {country.strip().title()} - population {population}, {language}"
    elif population:
        return f"{city.strip().title()}, {country.strip().title()} - population {population}"
    else:
        return f"{city.strip().title()}, {country.strip().title()}"
#3 calls with different cities
place1= location ('Santiago', ' Chile')
place2= location ('New York City', ' United States', 8580000)
place3= location ('Athens', ' Greece', 643000, 'Greek')

print(place1)
print(place2)
print(place3)