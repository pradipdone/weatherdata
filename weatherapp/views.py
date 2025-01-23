# weatherapp/views.py
import requests
from django.shortcuts import render
from django.conf import settings

def get_weather_data(city):
    # VisualCrossing API URL (using the example URL you provided)
    api_url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}?unitGroup=us&key={settings.VISUALCROSSING_API_KEY}&contentType=json"
    
    # Make the GET request to the VisualCrossing API
    response = requests.get(api_url)
    
    # Parse the response JSON
    data = response.json()
    
    return data

def home(request):
    weather = None
    city = None
    error_message = None
    
    if request.method == 'POST':
        city = request.POST.get('city')
        if city:
            weather = get_weather_data(city)
            # Handle errors if the response is not successful
            if 'error' in weather:
                error_message = weather['error']
    
    return render(request, 'index.html', {'weather': weather, 'city': city, 'error_message': error_message})
