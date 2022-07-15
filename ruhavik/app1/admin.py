from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Car)
admin.site.register(City)
admin.site.register(Driver)

admin.site.register(CameraCheckin)
admin.site.register(ChangeSSD)
admin.site.register(Dinner_stop)
admin.site.register(Dtp_or_chp)
admin.site.register(Lunch_stop)

admin.site.register(Malfunctions)
admin.site.register(Police_problem)
admin.site.register(Refueling)
admin.site.register(Trip_and_documents)
# admin.site.register(Start)
admin.site.register(End)
admin.site.register(Unique_km)

class Start1(admin.ModelAdmin):
    list_display = ('driver','start_date')

admin.site.register(Start,Start1)