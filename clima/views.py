from django.shortcuts import render
import json
import urllib.request

# Create your views here.

def index(request):
    if request.method == 'POST':

        city = request.POST['cidade']
        res = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=9c0208cc35a7a51bcbb5b28638e11c4f').read()
        json_data = json.loads(res)
        data = {
            "country_code2": str(json_data['sys']['country']),
            "coordinate": str(json_data['coord']['lon']) + ' ' +
            str(json_data['coord']['lat']),
            "temp": str(json_data['main']['temp'])+'k',
            "temperatura_min": str(json_data['main']['temp_min'])+'k',
            "pressure": str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity']),

        }

    else:
        city = ''
        data = {}    

    return render(request, 'index.html', {'cidade': city, 'data': data})
