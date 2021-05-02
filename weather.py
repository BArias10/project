# Brandon Arias CIS 245
# weather project
# API Key : http://api.openweathermap.org/data/2.5/forecast?id=524901&appid=21ad8f1bef4fecfb95bd7d8328a5c54e
# API Parameters URL - https://openweathermap.org/api/one-call-api

# create main function/welcome message

# zip code function

def by_zip():
        zip_code = int(input('Please Enter Your Zip code: '))
        url = 'https://api.openweathermap.org/data/2.5/weather?zip={},us&units=imperial&appid=21ad8f1bef4fecfb95bd7d8328a5c54e'.format(zip_code)
        res = requests.get(url)
        data = res.json()
        show_data(data)

# city search function

def by_city():
    city = input('Please Enter Your City Name: ')
    url = 'https://api.openweathermap.org/data/2.5/weather?q={},us&appid=21ad8f1bef4fecfb95bd7d8328a5c54e&units=imperial'.format(city)
    res = requests.get(url)
    data = res.json()
    show_data(data)

# print data/readble format function

# ask again/loop
