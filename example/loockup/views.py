from django.shortcuts import render
import json
import requests

result = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=25&API_KEY=51838DC2-B14D-4FA5-A746-6954DE53931B")

# Create your views here.
def index(request):

    try:
        api = json.loads(result.content)
    except Exception as e:
        api = 'Error'
    return render(request,"index.html",{'api' : api})
# https://www.airnowapi.org/aq/observation/zipCode/current/?format=text/csv&zipCode=20002&distance=25&API_KEY=51838DC2-B14D-4FA5-A746-6954DE53931B


def about(request):
    return render(request,"about.html",{})