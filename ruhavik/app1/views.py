from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import *
from django.core import serializers
from datetime import date
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
    context = { 
        'cities':cities,
        'unique':unique,
        'percentage':percentage,
        'km':unique.km,
        'drivers':drivers
    }

    return render(request,'app1/main.html',context=context)


def pop(request):
    start = Start.objects.get(driver__id = 1)
    return HttpResponse(start.start_date.time() )
    