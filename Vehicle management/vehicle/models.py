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
    user_credit = models.IntegerField(default=100)



class Vehicle(models.Model):
    vehicle_id = models.AutoField(primary_key=True)
    vehicle_plate = models.ForeignKey(Plate, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle_status = models.BooleanField(default=True)


class Record(models.Model):
    record_id = models.AutoField(primary_key=True)
    vehicle_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    record_date = models.DateTimeField(auto_now_add=True,null=True)

'''
INSERT INTO public.vehicle_violationtype(
	violation_id, violation_name)
	VALUES (1, 'speeding');

INSERT INTO public.vehicle_violationtype(
	violation_id, violation_name)
	VALUES (2, 'run a red light');

INSERT INTO public.vehicle_violationtype(
	violation_id, violation_name)
	VALUES (3, 'illegal parking');
'''
class ViolationType(models.Model):
    violation_id = models.AutoField(primary_key=True)
    violation_name = models.CharField(max_length=50)

class Trafficviolations(models.Model):
    Trafficviolations_id = models.AutoField(primary_key=True)
    record_id = models.ForeignKey(Record, on_delete=models.CASCADE)                 
    violation_id = models.ForeignKey(ViolationType, on_delete=models.CASCADE)         # Types of offences 1 for speeding 2 for red light running 3 for illegal parking
    violation_date = models.DateTimeField(auto_now_add=True,null=True)
    violation_level = models.IntegerField()                                           # Violation level 0 is average 1 is serious 2 is very serious
    email_status = models.BooleanField(default=False,null=True)                       # whether to send mail 0 is not sent 1 is sent

