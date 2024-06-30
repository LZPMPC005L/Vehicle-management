from django.db import models

# Create your models here.

'''
INSERT INTO vehicle_plate (plate_number, plate_price, plate_status) VALUES ('JA12345', 10000.00, False);
INSERT INTO vehicle_plate (plate_number, plate_price, plate_status) VALUES ('DB67890', 15000.00, False);
INSERT INTO vehicle_plate (plate_number, plate_price, plate_status) VALUES ('OC23456', 12000.00, False);
INSERT INTO vehicle_plate (plate_number, plate_price, plate_status) VALUES ('ID78901', 8000.00, False);
INSERT INTO vehicle_plate (plate_number, plate_price, plate_status) VALUES ('OE45678', 20000.00, False);
INSERT INTO vehicle_plate (plate_number, plate_price, plate_status) VALUES ('RF90123', 11000.00, False);
INSERT INTO vehicle_plate (plate_number, plate_price, plate_status) VALUES ('QG67890', 9000.00, False);
INSERT INTO vehicle_plate (plate_number, plate_price, plate_status) VALUES ('ZH12345', 18000.00, False);
INSERT INTO vehicle_plate (plate_number, plate_price, plate_status) VALUES ('XJ67890', 14000.00, False);
INSERT INTO vehicle_plate (plate_number, plate_price, plate_status) VALUES ('CK23456', 16000.00, False);
'''

class Plate(models.Model):
    plate_id = models.AutoField(primary_key=True)
    plate_number = models.CharField(max_length=10)
    plate_price = models.DecimalField(max_digits=10, decimal_places=2)
    plate_status = models.BooleanField(default=True)

'''
INSERT INTO public.vehicle_user (user_name, user_email, user_phone, user_address, user_password, user_credit) VALUES ('FDS', 'zhangsan@ example.com', '13812345678', 'No.1 Zhongguancun Street, Haidian District, Beijing', 'password12123', 100);
INSERT INTO public.vehicle_user (user_name, user_email, user_phone, user_address, user_password, user_credit) VALUES ('Li Si', 'lisi@example.com ', '13912345678', '100 Century Avenue, Pudong New Area, Shanghai', 'password456', 100);
INSERT INTO public.vehicle_user (user_name, user_email, user_phone, user_address, user_password, user_credit) VALUES ('Wang Wu', 'wangwu@example. com', '13712345678', 'No.123 Zhucun Road, Tianhe District, Guangzhou City', 'password789', 100);
INSERT INTO public.vehicle_user (user_name, user_email, user_phone, user_address, user_password, user_credit) VALUES ('Zhao Liu', 'zhaoliu@example. com', '13812345679', '456 Science and Technology Park Road, Nanshan District, Shenzhen', 'passwordabc', 100);
INSERT INTO public.vehicle_user (user_name, user_email, user_phone, user_address, user_password, user_credit) VALUES ('sunqi', 'sunqi@example. com', '13912345679', 'No. 789 Liou Street, Xihu District, Hangzhou', 'passworddef', 100);
INSERT INTO public.vehicle_user (user_name, user_email, user_phone, user_address, user_password, user_credit) VALUES ('zhouba', 'zhouba@example. com', '13712345679', '101 Hongxing Road, Jinjiang District, Chengdu', 'passwordghi', 100);
INSERT INTO public.vehicle_user (user_name, user_email, user_phone, user_address, user_password, user_credit) VALUES ('wujiu', 'wujiu@example. com', '13812345670', '111 Zou Rong Road, Yuzhong District, Chongqing', 'passwordjkl', 100);



'''
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=50)
    user_email = models.EmailField(max_length=50)
    user_phone = models.CharField(max_length=15)
    user_address = models.CharField(max_length=100)
    user_password = models.CharField(max_length=50)
    user_credit = models.IntegerField(default=100)


'''INSERT INTO public.vehicle_area(area_name)
	VALUES     ('Area AB'),
    ('Area CD'),
    ('Area EF'),
    ('Area GH'),
    ('Area IJ'),
    ('Area KL'),
    ('Area MN'),
    ('Area OP'),
    ('Area QR'),
    ('Area ST'),
    ('Area UV'),
    ('Area WX'),
    ('Area YZ'),
    ('Area BC'),
    ('Area DE'),
    ('Area FG'),
    ('Area HI'),
    ('Area JK'),
    ('Area LM'),
    ('Area NO');'''
class Area(models.Model):
    area_id = models.AutoField(primary_key=True)
    area_name = models.CharField(max_length=50)


class Vehicle(models.Model):
    vehicle_id = models.AutoField(primary_key=True)
    vehicle_plate = models.ForeignKey(Plate, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle_status = models.BooleanField(default=True)

'''
-- Generate a 24-hour time range for the previous 3 days.
WITH date_range AS (
  SELECT date_trunc('hour', NOW() - INTERVAL '72 hours') + (n || ' hours')::INTERVAL AS hour
  FROM generate_series(0, 71) n
)
-- Randomly select area_id from area table
, vehicle_area AS (
  SELECT area_id
  FROM public.vehicle_area
  ORDER BY random()
)
-- Randomly select vehicle_id from vehicle table
, vehicle_vehicle AS (
  SELECT vehicle_id
  FROM public.vehicle_vehicle
  ORDER BY random()
)
-- Insert record data
INSERT INTO public.vehicle_record (area_id_id, vehicle_id_id, record_date)
SELECT a.area_id, v.vehicle_id, d.hour
FROM date_range d
Cross-connected vehicles a
crosslinked vehicle v
ORDER BY random()
limit 10000; -- Limit insertion to 1000 items.



'''

class Record(models.Model):
    record_id = models.AutoField(primary_key=True)
    area_id = models.ForeignKey(Area, on_delete=models.CASCADE)
    vehicle_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    record_date = models.DateTimeField(auto_now_add=True,null=True)

'''
INSERT INTO public.vehicle_violationtype(
	violation_id, violation_name)
	VALUES (1, 'Speeding').

INSERT INTO public.vehicle_violationtype(
	violation_id, violation_name)
	VALUES (2, 'Running a red light'); INSERT INTO public.vehicle_violationtype( violation_id, violation_name); INSERT INTO public.

INSERT INTO public.vehicle_violationtype(
	violation_id, violation_name)
	VALUES (3, 'Parking violation'); INSERT INTO public.vehicle_violationtype( violation_id, violation_name); INSERT INTO public.


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

'''
INSERT INTO public.vehicle_emergency(emergency_type) VALUES (120);
INSERT INTO public.vehicle_emergency(emergency_type) VALUES (119);
INSERT INTO public.vehicle_emergency(emergency_type) VALUES (110);

'''

class Emergency(models.Model):
    emergency_id = models.AutoField(primary_key=True)
    emergency_type = models.CharField(max_length=10)                                           ## Emergency vehicle types 120 for ambulances 119 for fire engines 110 for police vehicles