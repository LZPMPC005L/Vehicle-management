from django.shortcuts import render
from rest_framework.views import APIView
from .models import Plate, User, Vehicle, Record,Area
from .serializers import PlateSerializer, UserSerializer, VehicleSerializer, RecordSerializer,TrafficviolationsSerializer
from rest_framework.response import Response
from django.core.mail import send_mail
from django11 import settings
from pyecharts.charts import Line
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt

# Create your views here.


class Stact():
    def __init__(self) -> None:
        self.msg = ''
        self.data = None
        self.code = 0

    def succeed(self, data):
        self.msg = 'success'
        self.data = data
        self.code = 200
        return {'msg': self.msg, 'data': self.data, 'code': self.code}
    
    def error(self, data):
        self.msg = 'error'
        self.data = data
        self.code = 400
        return {'msg': self.msg, 'data': self.data, 'code': self.code}


class PlateRegistration(APIView):
    def get(self, request):
        #Returns the licence plate number whose status is not 0
        plates = Plate.objects.filter(plate_status=0)
        s = PlateSerializer(plates, many=True)
        return render(request, 'plate.html', {'plates': s.data})
    
    def post(self, request):
        #Registered Vehicle Registration Number
        s = VehicleSerializer(data=request.data)
        if s.is_valid():
            #After successful registration, change the status of the plate list licence plate number to 1
            plate = Plate.objects.get(plate_id=request.data['vehicle_plate'])
            plate.plate_status = 1
            plate.save()
            s.save()
            return Response(data=Stact().succeed('Successful registration'),status=200)
        return Response(data=Stact().error(s.errors),status=400)

class UserRegistration(APIView):
    def get(self, request):
        return render(request, 'registration.html')
    #User Registration
    def post(self, request):
        mutable_data = request.data.copy()
        mutable_data['user_credit'] = 100
        s = UserSerializer(data=mutable_data)
        if s.is_valid():
            s.save()
            return Response(data=Stact().succeed('Successful registration'),status=200)
        return Response(data=Stact().error(s.errors),status=400)


class IdentfitionRecord(APIView):
    def get(self, request):
        return render(request, 'record.html')

    #Recognition and recording of licence plate numbers
    def post(self, request):
        #Printing data from the Vehicle table
        plate_ids = list(Plate.objects.filter(plate_number=request.data['vehicle_plate']).values_list('plate_id', flat=True))
        mutable_data = Vehicle.objects.filter(vehicle_plate__in=plate_ids).first()
        area_id = Area.objects.get(area_name=request.data['area_name']).area_id

        if mutable_data:
            record_data = {
                'area_id': area_id,
                'vehicle_id': mutable_data.vehicle_id
            }
            s = RecordSerializer(data=record_data)
            if s.is_valid():
                s.save()
                return Response(data=Stact().succeed('Recording Success'), status=200)
            return Response(data=Stact().error(s.errors), status=400)
        else:
            return Response(data=Stact().error('Invalid licence plate numbers'), status=400)



def send_email(violation_type, fine, deduction,mail):
    subject = f'违章记录: {violation_type}'
    message = f'您有一条新的违章记录: {violation_type}\n罚款: {fine}元\n扣分: {deduction}分'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [mail]
    send_mail(subject, message, from_email, recipient_list) 
    return True


class Violation(APIView):
    def get(self, request):
        context = {
            'range_3': range(3),
        }
        return render(request, 'trafficviolations.html',context=context)
    
    #违章记录
    def post(self, request):
        s = TrafficviolationsSerializer(data=request.data)
        if s.is_valid():
            #发送给用户邮箱，发送成功后将email_status改为1 ，根据违章类型和违章等级发送不同的邮件，轻微罚500元扣3分，严重罚1000元扣6分，非常严重罚2000元扣12分，如果用户信用分低于60分，则删除用户
            record = Record.objects.get(record_id=request.data['record_id'])
            user_id = record.vehicle_id.user_id
            user = User.objects.get(user_id=user_id.user_id)
            mutable_data = request.data.copy()
            if request.data['violation_level'] == '0':
                send_email(request.data['violation_id'], 500, 3, user.user_email)
                mutable_data['email_status'] = 1
                user.user_credit -= 3
            elif request.data['violation_level'] == '1':
                send_email(request.data['violation_id'], 1000, 6, user.user_email)
                mutable_data['email_status'] = 1
                user.user_credit -= 6
            elif request.data['violation_level'] == '2':
                send_email(request.data['violation_id'], 2000, 12, user.user_email)
                mutable_data['email_status'] = 1
                user.user_credit -= 12
            if user.user_credit < 60:
                user.delete()
            user.save()
            s = TrafficviolationsSerializer(data=mutable_data)
            s.is_valid()
            s.save()
            return Response(data=Stact().succeed('记录成功'),status=200)
        return Response(data=Stact().error(s.errors),status=400)


def send_email1(area_type,time,mail):
    for i in range(len(mail)):
        subject = f'尊敬的车主:'
        message = f'您好，{area_type}地区将在大概{time}时间左右发生堵车，请您绕道而行，谢谢！'
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [mail[i]]
        send_mail(subject, message, from_email, recipient_list) 
    return True


class AreaCondition(APIView):
    '''
    为了优化城市交通,部门希望分析不同时间的车辆流量,并确定容易拥堵的区域。该系统应该提供洞察力,帮助管理和减少交通拥堵。

        建议方法:
        您应该通过以下方式增强现有系统:

        实现一个功能,分析不同时间通过城市路口的车辆数量
        根据交通流量数据确定容易拥堵的区域
        关键点:考虑使用数据可视化工具来表示交通流量和拥堵模式;另外,实现算法来预测拥堵时间,并在检测到拥堵时通过电子邮件向驾驶员建议替代路线
    
    '''
    def get(self, request):
        #Plot the number of records per day per region, return the chart
        area = Area.objects.all()
        line = Line()
        mail = User.objects.all().values_list('user_email', flat=True)
        for i in area:
            record = list(Record.objects.filter(area_id=i.area_id).values())
            record = pd.DataFrame(record)
            record['record_date'] = pd.to_datetime(record['record_date'])
            record = record.groupby(record['record_date'].dt.hour).count()
            line.add_xaxis(record.index.astype(str).to_list())
            model = ARIMA(record['record_id'], order=(5,1,0))
            model_fit = model.fit()
            forecast = model_fit.forecast(steps=5).tolist()
            for j in range(len(forecast)):
                if forecast[j] > 100:
                    send_email1(i.area_name, j+1, mail)
            line.add_yaxis(i.area_name, record['record_id'].to_list())
        line.page_title = 'vehicular traffic'
        line.render('./templates/line.html')

        line2 = Line()
        record = list(Record.objects.all().values())
        record = pd.DataFrame(record)
        record['record_date'] = pd.to_datetime(record['record_date'])
        record = record.groupby(record['record_date'].dt.hour).count()
        line2.add_xaxis(record.index.astype(str).to_list())
        line2.add_yaxis('whole city', record['record_id'].to_list())
        line2.page_title = 'Vehicle flow throughout the city'
        line2.render('./templates/line2.html')
        return render(request, 'area.html')
    
@xframe_options_exempt    
def jump_years(request):
    """
    跳转可视化
    """
    return render(request, 'line.html', {})

@xframe_options_exempt    
def jump_years1(request):
    """
    跳转可视化
    """
    return render(request, 'line2.html', {})

