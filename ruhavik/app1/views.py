from queue import Empty
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import *
from django.core import serializers
from datetime import date
from datetime import timedelta
# Create your views here.
def test(request):

    today = str(date.today())
    if request.method == "GET":
        try:
            data = CameraCheckin.objects.filter(created__date = today).values()
        except Exception as e:
            message = {
                "message":"not found"
            }
            return JsonResponse(message, status=404)
        return JsonResponse({"models_to_return": list(data)})

def start(request):
    today = str(date.today())
    if request.method == "GET":
        try:
            data = Trip_and_documents.objects.filter(check_date__date = today).values()
        except Exception as e:
            message = {
                "message":"not found"
            }
            return JsonResponse(message, status=404)
        return JsonResponse({"models_to_return": list(data)})

def kms(request):
    today = str(date.today())
    if request.method == "GET":
        try:
            data = Start.objects.filter(start_date__date = today).values()
        except Exception as e:
            message = {
                "message":"not found"
            }
            return JsonResponse(message, status=404)
        return JsonResponse({"models_to_return": list(data)})

def main(request):
    cities = City.objects.all()
    drivers = Driver.objects.all()
    unique = Unique_km.objects.get(id =1)
    percentage = int(unique.km)*100/50000
    
    today = date.today()
    # tomorrow = today + timedelta(days=1)
    # print(yesterday)
    data = End.objects.filter(end_date__date = today)
    # print(today)
    if not data:
        pass
    else:
    # print(data)
        for i in drivers:
            # print(i.id)
            start = Start.objects.filter(driver__id = i.id)
            end = End.objects.filter(driver__id = i.id)
            start_time_int = []
            end_time_int = []
            time_difference = []
            for j in start:
                # print(j.start_date.time())

                start_time = j.start_date.time()
                start_time_int.append((start_time.hour * 3600) + (start_time.minute * 60) + (start_time.second))
            for p in end:
                end_time = p.end_date.time()
                end_time_int.append((end_time.hour * 3600) + (end_time.minute * 60) + (end_time.second))
            for b in range(len(end)):
                time_difference.append(((end_time_int[b] - start_time_int[b]) / 3600))
            for g in range(len(time_difference)):
                activ = Activity.objects.filter(activnost_date__date =today, driver__id = i.id)
                if activ:
                    pass
                else:
                    Activity.objects.create(
                        driver = i,
                        activnost_hours = format(time_difference[g], ".2f")
                    )
            
    

    context = { 
        'cities':cities,
        'unique':unique,
        'percentage':format(percentage, ".1f"),
        'km':unique.km,
        'drivers':drivers
    }

    return render(request,'app1/main.html',context=context)


    