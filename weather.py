import requests
import json
import config as cnf

almaty_id = 1526384
zhez_id = 1516589
ast_id = 1526273
shym_id = 1518980

url = f'https://api.openweathermap.org/data/2.5/weather?&appid={cnf.api_key}'

def temperature(city_id):
    response = requests.get(url, params={'id': city_id, 'units': 'metric', 'lang': 'ru'})
    data = json.loads(response.text)
    temp_now = data['main']['temp']
    feels_like = data['main']['feels_like']
    return temp_now, feels_like

if __name__ == '__main__':
    temperature()