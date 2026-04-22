from django.shortcuts import render
import requests
from django.conf import settings
# Create your views here.
def index(request):
    if request.method == "POST":
        city = request.POST.get('city')
        # print(city)
        data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={settings.API_KEY}").json()
    
        
    return render(request,'index.html',{'data':data})
