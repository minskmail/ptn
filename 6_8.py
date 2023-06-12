# Дан словарь, ключ - Название страны, значение - список городов, на вход поступает город, необходимо сказать из какой
# он страны

while 1:

    city = (input('Input city: '))

    countries = {
        'Belarus': ['minsk', 'hrodna', 'vitsebsk', 'brest', 'homiel', 'mahilow'],
        'Polska': ['warshawa', 'bialystok', 'poznan', 'hdansk']
    }


    def find_country(town):
        for cntry, towns in countries.items():
            if town.lower() in towns:
                return cntry

    country = find_country(city)
    print(country)
