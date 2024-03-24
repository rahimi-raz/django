from django.shortcuts import render
import json
import requests

result = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20008&distance=25&API_KEY=51838DC2-B14D-4FA5-A746-6954DE53931B")

# Create your views here.
def index(request):

    try:
        api = json.loads(result.content)
    except Exception as e:
        api = 'Error'
    
    aqicolorstate=""
    description=""
    if api[0]['Category']['Number'] == 1 :
        description= "Air quality is considered satisfactory, and air pollution poses little or no risk."
        aqicolorstate="Good"
    elif api[0]['Category']['Number'] == 2 :
        description= "Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution."
        aqicolorstate="Moderate"
    elif api[0]['Category']['Number'] == 3 :
        aqicolorstate="USG"
        description= "Members of sensitive groups may experience health effects. The general public is not likely to be affected."
    elif api[0]['Category']['Number'] == 4 :
        aqicolorstate="unhealthy"
        description= "Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects."
    elif api[0]['Category']['Number'] == 5 :
        aqicolorstate="veryunhelthy"
        description= "Health alert: everyone may experience more serious health effects."
    elif api[0]['Category']['Number'] == 6 :
        aqicolorstate="hazardous"
        description= "	Health warnings of emergency conditions. The entire population is more likely to be affected."
    else: 
        aqicolorstate="hazardous"
        description= "Data in unavailable"


    return render(request,"index.html",{
        'api' : api,
        'aqicolorstate' : aqicolorstate,
        'description' : description,
        })

def about(request):
    return render(request,"about.html",{})