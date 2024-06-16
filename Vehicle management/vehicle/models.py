from django.db import models

# Create your models here.

'''
INSERT INTO vehicle_plate (plate_number, plate_price, plate_status) VALUES ('京A12345', 10000.00, False);
INSERT INTO vehicle_plate (plate_number, plate_price, plate_status) VALUES ('沪B67890', 15000.00, False);
INSERT INTO vehicle_plate (plate_number, plate_price, plate_status) VALUES ('粤C23456', 12000.00, False);
INSERT INTO vehicle_plate (plate_number, plate_price, plate_status) VALUES ('陕D78901', 8000.00, False);
INSERT INTO vehicle_plate (plate_number, plate_price, plate_status) VALUES ('浙E45678', 20000.00, False);
INSERT INTO vehicle_plate (plate_number, plate_price, plate_status) VALUES ('鲁F90123', 11000.00, False);
INSERT INTO vehicle_plate (plate_number, plate_price, plate_status) VALUES ('豫G67890', 9000.00, False);
INSERT INTO vehicle_plate (plate_number, plate_price, plate_status) VALUES ('苏H12345', 18000.00, False);
INSERT INTO vehicle_plate (plate_number, plate_price, plate_status) VALUES ('冀J67890', 14000.00, False);
INSERT INTO vehicle_plate (plate_number, plate_price, plate_status) VALUES ('湘K23456', 16000.00, False);
'''

class Plate(models.Model):
    plate_id = models.AutoField(primary_key=True)
    plate_number = models.CharField(max_length=10)
    plate_price = models.DecimalField(max_digits=10, decimal_places=2)
    plate_status = models.BooleanField(default=True)

'''
INSERT INTO public.vehicle_user (user_name, user_email, user_phone, user_address, user_password, user_credit) VALUES ('张三', 'zhangsan@example.com', '13812345678', '北京市海淀区中关村大街1号', 'password123', 100);
INSERT INTO public.vehicle_user (user_name, user_email, user_phone, user_address, user_password, user_credit) VALUES ('李四', 'lisi@example.com', '13912345678', '上海市浦东新区世纪大道100号', 'password456', 100);
INSERT INTO public.vehicle_user (user_name, user_email, user_phone, user_address, user_password, user_credit) VALUES ('王五', 'wangwu@example.com', '13712345678', '广州市天河区珠村路123号', 'password789', 100);
INSERT INTO public.vehicle_user (user_name, user_email, user_phone, user_address, user_password, user_credit) VALUES ('赵六', 'zhaoliu@example.com', '13812345679', '深圳市南山区科技园路456号', 'passwordabc', 100);
INSERT INTO public.vehicle_user (user_name, user_email, user_phone, user_address, user_password, user_credit) VALUES ('孙七', 'sunqi@example.com', '13912345679', '杭州市西湖区留下街789号', 'passworddef', 100);
INSERT INTO public.vehicle_user (user_name, user_email, user_phone, user_address, user_password, user_credit) VALUES ('周八', 'zhouba@example.com', '13712345679', '成都市锦江区红星路101号', 'passwordghi', 100);
INSERT INTO public.vehicle_user (user_name, user_email, user_phone, user_address, user_password, user_credit) VALUES ('吴九', 'wujiu@example.com', '13812345670', '重庆市渝中区邹容路111号', 'passwordjkl', 100);
INSERT INTO public.vehicle_user (user_name, user_email, user_phone, user_address, user_password, user_credit) VALUES ('郑十', 'zhengshi@example.com', '13912345670', '南京市玄武区中央路222号', 'passwordmno', 100);
INSERT INTO public.vehicle_user (user_name, user_email, user_phone, user_address, user_password, user_credit) VALUES ('王一', 'wangyi@example.com', '13712345670', '武汉市洪山区珞狮路333号', 'passwordpqr', 100);
INSERT INTO public.vehicle_user (user_name, user_email, user_phone, user_address, user_password, user_credit) VALUES ('张二', 'zhanger@example.com', '13812345671', '西安市碑林区长安街444号', 'passwordstu', 100);
INSERT INTO public.vehicle_user (user_name, user_email, user_phone, user_address, user_password, user_credit) VALUES ('李三', 'lisan@example.com', '13912345671', '厦门市思明区软件园路555号', 'passwordvwx', 100);
INSERT INTO public.vehicle_user (user_name, user_email, user_phone, user_address, user_password, user_credit) VALUES ('赵四', 'zhaosi@example.com', '13712345671', '长沙市开福区芙蓉中路666号', 'passwordyz0', 100);
INSERT INTO public.vehicle_user (user_name, user_email, user_phone, user_address, user_password, user_credit) VALUES ('孙五', 'sunwu@example.com', '13812345672', '贵阳市观山湖区中华路777号', 'password123', 100);
INSERT INTO public.vehicle_user (user_name, user_email, user_phone, user_address, user_password, user_credit) VALUES ('周六', 'zhouliu@example.com', '13912345672', '合肥市包河区青阳路888号', 'password456', 100);
INSERT INTO public.vehicle_user (user_name, user_email, user_phone, user_address, user_password, user_credit) VALUES ('吴七', 'wuqi@example.com', '13712345672', '郑州市金水区经三路999号', 'password789', 100);
INSERT INTO public.vehicle_user (user_name, user_email, user_phone, user_address, user_password, user_credit) VALUES ('郑八', 'zhengba@example.com', '13812345673', '大连市沙河口区中山路111号', 'passwordabc', 100);
INSERT INTO public.vehicle_user (user_name, user_email, user_phone, user_address, user_password, user_credit) VALUES ('王九', 'wangjiu@example.com', '13912345673', '青岛市市南区东海路222号', 'passworddef', 100);
INSERT INTO public.vehicle_user (user_name, user_email, user_phone, user_address, user_password, user_credit) VALUES ('张十', 'zhangshi@example.com', '13712345673', '哈尔滨市南岗区红旗大街333号', 'passwordghi', 100);
INSERT INTO public.vehicle_user (user_name, user_email, user_phone, user_address, user_password, user_credit) VALUES ('李一', 'liyi@example.com', '13812345674', '济南市历下区解放路444号', 'passwordjkl', 100);
INSERT INTO public.vehicle_user (user_name, user_email, user_phone, user_address, user_password, user_credit) VALUES ('赵二', 'zhaoer@example.com', '13912345674', '石家庄市桥西区中山路555号', 'passwordmno', 100);
INSERT INTO public.vehicle_user (user_name, user_email, user_phone, user_address, user_password, user_credit) VALUES ('孙三', 'sunsan@example.com', '13712345674', '沈阳市和平区太原街666号', 'passwordpqr', 100);
INSERT INTO public.vehicle_user (user_name, user_email, user_phone, user_address, user_password, user_credit) VALUES ('周四', 'zhousi@example.com', '13812345675', '昆明市盘龙区北京路777号', 'passwordstu', 100);
INSERT INTO public.vehicle_user (user_name, user_email, user_phone, user_address, user_password, user_credit) VALUES ('吴五', 'wuwu@example.com', '13912345675', '无锡市新吴区锡沪路888号', 'passwordvwx', 100);
INSERT INTO public.vehicle_user (user_name, user_email, user_phone, user_address, user_password, user_credit) VALUES ('郑六', 'zhengliu@example.com', '13712345675', '宁波市江东区天源路999号', 'passwordyz0', 100);
INSERT INTO public.vehicle_user (user_name, user_email, user_phone, user_address, user_password, user_credit) VALUES ('王七', 'wangqi@example.com', '13812345676', '温州市鹿城区瓯江路111号', 'password123', 100);
INSERT INTO public.vehicle_user (user_name, user_email, user_phone, user_address, user_password, user_credit) VALUES ('张八', 'zhangba@example.com', '13912345676', '嘉兴市秀洲区中环南路222号', 'password456', 100);

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
-- 生成前3天24小时的时间范围
WITH date_range AS (
  SELECT date_trunc('hour', NOW() - INTERVAL '72 hours') + (n || ' hours')::INTERVAL AS hour
  FROM generate_series(0, 71) n
)
-- 从Area表中随机选择area_id
, vehicle_area AS (
  SELECT area_id
  FROM public.vehicle_area
  ORDER BY random()
)
-- 从Vehicle表中随机选择vehicle_id
, vehicle_vehicle AS (
  SELECT vehicle_id
  FROM public.vehicle_vehicle
  ORDER BY random()
)
-- 插入Record数据
INSERT INTO public.vehicle_record (area_id_id, vehicle_id_id, record_date)
SELECT a.area_id, v.vehicle_id, d.hour
FROM date_range d
CROSS JOIN vehicle_area a
CROSS JOIN vehicle_vehicle v
ORDER BY random()
LIMIT 10000; -- 限制插入1000条数据

'''

class Record(models.Model):
    record_id = models.AutoField(primary_key=True)
    area_id = models.ForeignKey(Area, on_delete=models.CASCADE)
    vehicle_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    record_date = models.DateTimeField(auto_now_add=True,null=True)

'''
INSERT INTO public.vehicle_violationtype(
	violation_id, violation_name)
	VALUES (1, '超速');

INSERT INTO public.vehicle_violationtype(
	violation_id, violation_name)
	VALUES (2, '闯红灯');

INSERT INTO public.vehicle_violationtype(
	violation_id, violation_name)
	VALUES (3, '违章停车');
'''
class ViolationType(models.Model):
    violation_id = models.AutoField(primary_key=True)
    violation_name = models.CharField(max_length=50)

class Trafficviolations(models.Model):
    Trafficviolations_id = models.AutoField(primary_key=True)
    record_id = models.ForeignKey(Record, on_delete=models.CASCADE)                 
    violation_id = models.ForeignKey(ViolationType, on_delete=models.CASCADE)         #违章类型 1为超速 2为闯红灯 3为违章停车
    violation_date = models.DateTimeField(auto_now_add=True,null=True)
    violation_level = models.IntegerField()                                           #违章等级 0为一般 1为严重 2为非常严重
    email_status = models.BooleanField(default=False,null=True)                       #是否发送邮件 0为未发送 1为已发送

