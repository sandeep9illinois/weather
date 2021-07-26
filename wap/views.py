from django.shortcuts import render
import requests

from .models import City
from .forms import CityForm

# Create your views here.

def index(request):
    url='http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=3641e7c75942626f3f598602831aa110'
    #city = 'Walnut Creek'

    if request.method=='POST':
        form = CityForm(request.POST)
        form.save()
    
    form = CityForm()

    #cities = ['Walnut Creek','London', 'New Delhi']#
    cities=City.objects.all() 
    weather_data =[]

    for city in cities:

        r = requests.get(url.format(city)).json()
        print(r)
        city_weather = {
            'city': r['name'],
            'temp': r['main']['temp'],
            'desc': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
        }
        weather_data.append(city_weather)

    print(weather_data)
    context = {'weather_data': weather_data, 'form': form}

    return render(request,'wap/weather.html', context)