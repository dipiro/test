import pyowm

city = input('Какой город Вас интересует?: ')

owm = pyowm.OWM('35afd1462382e8b97093bb1ce1f57372', language='ru')

observation = owm.weather_at_place(city)
w = observation.get_weather()
temperature = w.get_temperature('celsius')['temp']
ww = w.get_detailed_status()

print( 'В городе ' + city + ' ' + str(temperature) + '. В этом горде ' + ww )

# https://github.com/csparpa/pyowm
#