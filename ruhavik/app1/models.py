from lib2to3.pgen2 import driver
from django.db import models


# Create your models here.


# class Camera(models.Model): #
#     camera_name = models.CharField(max_length=100,null=True,blank=True)
#     def __str__(self):
#         return self.camera_name

class Car(models.Model):#
    car_model = models.CharField(max_length=100,null=True,blank=True)
    car_number = models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
        return self.car_number

class City(models.Model):
    city_name = models.CharField(max_length=50,null=True,blank=True)
    state = models.IntegerField(blank=True,null=True)
    def __str__(self):
        return self.city_name

class Driver(models.Model):#
    car = models.ForeignKey(Car,on_delete=models.CASCADE,null=True,blank=True)
    driver_name = models.CharField(max_length=50,null=True,blank=True)
    driver_last_name = models.CharField(max_length=50,null=True,blank=True)
    driver_chat_id = models.CharField(max_length=50,null=True,blank=True)
    driver_username= models.CharField(max_length=50,null=True,blank=True)
    phone_number = models.CharField(max_length=50,null=True,blank=True)
    def __str__(self):
        return self.driver_name

    

class CameraCheckin(models.Model):
    # camera = models.ForeignKey(Camera,on_delete=models.CASCADE,null=True,blank=True)
    driver = models.ForeignKey(Driver,on_delete=models.CASCADE,null=True,blank=True)
    car = models.ForeignKey(Car,on_delete=models.CASCADE,null=True,blank=True)
    cover_check = models.BooleanField(null=True,blank=True)
    # support_st_check = models.BooleanField(null=True,blank=True)
    support_st_check_photo = models.ImageField(upload_to="images/support",null=True,blank=True)
    # chips_and_abrasions_check = models.BooleanField(null=True,blank=True)
    chips_and_abrasions_check_photo1 = models.ImageField(upload_to="images/chips",null=True,blank=True)
    chips_and_abrasions_check_photo2 = models.ImageField(upload_to="images/chips",null=True,blank=True)
    chips_and_abrasions_check_photo3 = models.ImageField(upload_to="images/chips",null=True,blank=True)
    chips_and_abrasions_check_photo4 = models.ImageField(upload_to="images/chips",null=True,blank=True)
    # camera_start = models.BooleanField(null=True,blank=True)
    camera_start_photo = models.ImageField(upload_to="images/camera",null=True,blank=True)
    ssd_date_check = models.BooleanField(null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    # def __str__(self):
    #     return self.created

# class SSD(models.Model):
#     ssd_name = models.CharField(max_length=100,null=True,blank=True)
#     ssd_number = models.CharField(max_length=100,null=True,blank=True)
#     def __str__(self):
#         return self.ssd_number

class ChangeSSD(models.Model):
    # ssd_new = models.ForeignKey(SSD,on_delete=models.CASCADE,null=True,blank=True)
    # ssd_old = models.ForeignKey(SSD,on_delete=models.CASCADE,null=True,blank=True)
    ssd_new =models.CharField(max_length=50,null=True,blank=True)
    ssd_old  =models.CharField(max_length=50,null=True,blank=True)
    driver = models.ForeignKey(Driver,on_delete=models.CASCADE,null=True,blank=True)
    car = models.ForeignKey(Car,on_delete=models.CASCADE,null=True,blank=True)
    change_date = models.DateTimeField(auto_now_add=True)
    # def __str__(self):
    #     return self.change_date

class Dinner_stop(models.Model):
    driver = models.ForeignKey(Driver,on_delete=models.CASCADE,null=True,blank=True)
    car = models.ForeignKey(Car,on_delete=models.CASCADE,null=True,blank=True)
    car_in_zone_photo = models.ImageField(upload_to="images/car",null=True,blank=True)
    alarm_check = models.BooleanField(null=True,blank=True)
    car_checkout = models.BooleanField(null=True,blank=True)
    dinner_date = models.DateTimeField(auto_now_add=True)
    # def __str__(self):
    #     return self.dinner_date

class Dtp_or_chp(models.Model):
    driver = models.ForeignKey(Driver,on_delete=models.CASCADE,null=True,blank=True)
    car = models.ForeignKey(Car,on_delete=models.CASCADE,null=True,blank=True)
    dtp_or_chp_date = models.DateTimeField(auto_now_add=True)
    dtp_or_chp_photo1 = models.ImageField(upload_to="images/dtp",null=True,blank=True)
    dtp_or_chp_photo2 = models.ImageField(upload_to="images/dtp",null=True,blank=True)
    dtp_or_chp_photo3 = models.ImageField(upload_to="images/dtp",null=True,blank=True)
    dtp_or_chp_photo4 = models.ImageField(upload_to="images/dtp",null=True,blank=True)
    dtp_date = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    # def __str__(self):
    #     return self.dtp_or_chp_date

# class dtp_chp_photos(models.Model):
#     photo = models.ForeignKey(Dtp_or_chp,null=True,blank=True,on_delete=models.CASCADE)
#     image = models.ImageField(upload_to="images/dtp",null=True,blank=True)

class Lunch_stop(models.Model):
    driver = models.ForeignKey(Driver,on_delete=models.CASCADE,null=True,blank=True)
    car = models.ForeignKey(Car,on_delete=models.CASCADE,null=True,blank=True)
    car_in_zone_photo = models.ImageField(upload_to="images/car",null=True,blank=True)
    alarm_check = models.BooleanField(null=True,blank=True)
    car_checkout = models.BooleanField(null=True,blank=True)
    launc_stop = models.DateTimeField(auto_now_add=True)
    # def __str__(self):
    #     return self.launc_stop

class Malfunctions(models.Model):
    driver = models.ForeignKey(Driver,on_delete=models.CASCADE,null=True,blank=True)
    car = models.ForeignKey(Car,on_delete=models.CASCADE,null=True,blank=True)
    malfunctions_date = models.DateTimeField(auto_now_add=True)
    # def __str__(self):
    #     return self.malfunctions_date

class Police_problem(models.Model):
    driver = models.ForeignKey(Driver,on_delete=models.CASCADE,null=True,blank=True)
    car = models.ForeignKey(Car,on_delete=models.CASCADE,null=True,blank=True)
    problem_date = models.DateTimeField(auto_now_add=True)
    # def __str__(self):
    #     return self.problem_date

class Refueling(models.Model):
    driver = models.ForeignKey(Driver,on_delete=models.CASCADE,null=True,blank=True)
    car = models.ForeignKey(Car,on_delete=models.CASCADE,null=True,blank=True)
    liter = models.CharField(max_length=30,null=True,blank=True)
    refueling_date = models.DateTimeField(auto_now_add=True)
    # def __str__(self):
    #     return self.refueling_date


class Trip_and_documents(models.Model):
    driver = models.ForeignKey(Driver,on_delete=models.CASCADE,null=True,blank=True)
    car = models.ForeignKey(Car,on_delete=models.CASCADE,null=True,blank=True)
    trip_sheet = models.BooleanField(null=True,blank=True)
    documents_check = models.BooleanField(null=True,blank=True)
    check_date = models.DateTimeField(auto_now_add=True)
    # def __str__(self):
    #     return self.check_date
    
class Start(models.Model):
    driver = models.ForeignKey(Driver,on_delete=models.CASCADE,null=True,blank=True)
    car = models.ForeignKey(Car,on_delete=models.CASCADE,null=True,blank=True)
    wheels_and_running_gear_check_photo1 = models.ImageField(upload_to="images/gear",null=True,blank=True)
    wheels_and_running_gear_check_photo2 = models.ImageField(upload_to="images/gear",null=True,blank=True)
    oil_check_photo2 = models.ImageField(upload_to="images/oil",null=True,blank=True)
    odometer_and_dashboard_readings_data = models.CharField(max_length=40,null=True,blank=True)
    odometer_and_dashboard_readings_data_photo = models.ImageField(upload_to="images/odometer",null=True,blank=True)
    tablet_connection = models.BooleanField(null=True,blank=True)
    start_date = models.DateTimeField(auto_now_add=True)
    # def __str__(self):
    #     return self.start_date

class End(models.Model):
    driver = models.ForeignKey(Driver,on_delete=models.CASCADE,null=True,blank=True)
    car = models.ForeignKey(Car,on_delete=models.CASCADE,null=True,blank=True)
    engine_stop = models.BooleanField(null=True,blank=True)
    odometer_and_dashboard_readings_data = models.CharField(max_length=40,null=True,blank=True)
    odometer_and_dashboard_readings_data_photo = models.ImageField(upload_to="images/odometer",null=True,blank=True)
    camera_stop = models.BooleanField(null=True,blank=True)
    camera_check_photo1 = models.ImageField(upload_to="images/camera",null=True,blank=True)
    camera_check_photo2 = models.ImageField(upload_to="images/camera",null=True,blank=True)
    camera_check_photo3 = models.ImageField(upload_to="images/camera",null=True,blank=True)
    camera_check_photo4 = models.ImageField(upload_to="images/camera",null=True,blank=True)
    construction_check = models.ImageField(upload_to="images/construction",null=True,blank=True)
    alarm_check = models.BooleanField(null=True,blank=True)
    camera_cover = models.ImageField(upload_to="images/camera",null=True,blank=True)
    end_date = models.DateTimeField(auto_now_add=True)
    # def __str__(self):
    #     return self.start_date

class Unique_km(models.Model):
    km = models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
        return self.km

class Activity(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE,null=True,blank=True)
    activnost_hours = models.FloatField(null=True,blank=True)
    activnost_date = models.DateTimeField(auto_now_add=True)
    

