# Brandon Arias CIS 245
# weather project
# API Key : http://api.openweathermap.org/data/2.5/forecast?id=524901&appid=21ad8f1bef4fecfb95bd7d8328a5c54e
# API Parameters URL - https://openweathermap.org/api/one-call-api

import requests
# create main function/welcome message

print("Local Weather Report")

# zip code function

def by_zip():
        zip_code = int(input('Enter Zip code: '))
        url = 'https://api.openweathermap.org/data/2.5/weather?zip={},us&units=imperial&appid=21ad8f1bef4fecfb95bd7d8328a5c54e'.format(zip_code)
        res = requests.get(url)
        data = res.json()
        show_data(data)

        anotherZip = input('Check Weather in a Different Zip Code? Type Yes or No: ')
        if question == 'Yes':

            main()

        if question == 'No':
            print("Thanks for Using!")

            exit()

# city search function

def by_city():
    city = input('Enter City Name: ')
    url = 'https://api.openweathermap.org/data/2.5/weather?q={},us&appid=21ad8f1bef4fecfb95bd7d8328a5c54e&units=imperial'.format(city)
    res = requests.get(url)
    data = res.json()
    show_data(data)

    anotherCity = input('Check Weather in a Different City? Type Yes or No: ')
    if question == 'Yes':
        main()

    if question == 'No':
        print("Thanks for Using!")
        exit()

# print data/readble format function

def show_data(data):
    temp = data['main']['temp']
    hightemp = data['main']['temp_max']
    lowtemp = data['main']['temp_min']
    wind_speed = data['wind']['speed']
    press = data['main']['pressure']
    latitude = data['coord']['lat']
    longitude = data['coord']['lon']
    humid = data['main']['humidity']
    description = data['weather'][0]['description']

    print('Current Temperature : {} degree fahrenheit'.format(temp))
    print('High Temperature : {} degree fahrenheit'.format(hightemp))
    print('Low Temperature : {} degree fahrenheit'.format(lowtemp))
    print('Wind Speed : {} m/s'.format(wind_speed))
    print('Pressure : {} hPa'.format(press))
    print('Latitude : {}'.format(latitude))
    print('Longitude : {}'.format(longitude))
    print('Humidity : {} %'.format(humid))
    print('Description : {}'.format(description))

# ask again/loop

def main():
    while True:
        answer = input("Check the Weather! Please type 'zip' for zipcode or 'city' for city name: ")
        if answer == 'city':
            try:
                print("Searching...")
                by_city()

            except Exception:
                print("City Not Found")
                by_city()

        if answer == 'zip':
            try:
                print("Searching...")
                by_zip()

            except Exception:
                print("Zip Not Found")
                by_zip()

        else:
            print("Invalid Entry. Enter one of the options.")


main()
