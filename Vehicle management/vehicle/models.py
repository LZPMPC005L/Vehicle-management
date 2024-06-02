from django.db import models

# Create your models here.

class Plate(models.Model):
    plate_id = models.AutoField(primary_key=True)
    plate_number = models.CharField(max_length=10)
    plate_price = models.DecimalField(max_digits=10, decimal_places=2)
    plate_status = models.BooleanField(default=True)

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=50)
    user_email = models.EmailField(max_length=50)
    user_phone = models.CharField(max_length=15)
    user_address = models.CharField(max_length=100)
    user_password = models.CharField(max_length=50)



class Vehicle(models.Model):
    vehicle_id = models.AutoField(primary_key=True)
    vehicle_plate = models.ForeignKey(Plate, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle_status = models.BooleanField(default=True)


class Record(models.Model):
    record_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    plate_id = models.ForeignKey(Plate, on_delete=models.CASCADE)
    record_date = models.DateTimeField(auto_now_add=True,null=True)


