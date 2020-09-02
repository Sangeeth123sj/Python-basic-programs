import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.weatherbug.com/weather-forecast/10-day-weather/')

soup = BeautifulSoup(page.content, 'html.parser')
print(soup.find_all('day-card has-hourly-forecasts'))

