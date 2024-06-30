from django.shortcuts import render
from rest_framework.views import APIView
from .models import Plate, User, Vehicle, Record,Area,Emergency
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

'''
    In emergency situations, it is vital that vehicles such as ambulances, fire engines and police vehicles be given priority. The system should detect emergency vehicles and provide them with a clear route, possibly by controlling traffic lights or notifying other drivers.

    Suggested Approach.
    You should enhance your existing system by.
    I Implementing a procedure for detecting and prioritising emergency vehicles at urban intersections
    I Designing a function to control traffic signals or send yield notifications to other drivers.

    Key point: For simplicity, use email notifications in this scenario, but explore other real-time notification avenues; also, ensure that the system is able to differentiate between emergency vehicles and regular traffic.


'''
def send_email2(area_type,emergency_type,mail):
    for i in range(len(mail)):
        subject = f'emergency notice:'
        message = f'Hello, there is an emergency in the area of {area_type}, please give way to {emergency_type} vehicles in the vicinity, thank you.！'
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [mail[i]]
        send_mail(subject, message, from_email, recipient_list) 
    return True



class IdentfitionRecord(APIView):
    def get(self, request):
        return render(request, 'record.html')

    #Recognition and recording of licence plate numbers
    def post(self, request):
        #Printing data from the Vehicle table

        if Emergency.objects.filter(emergency_type=request.data['vehicle_plate']).exists():
            emergency = Emergency.objects.get(emergency_type=request.data['vehicle_plate'])
            area_id = Area.objects.get(area_name=request.data['area_name']).area_id
            mail = User.objects.all().values_list('user_email', flat=True)
            send_email2(request.data['area_name'], request.data['vehicle_plate'], mail)
            record_data = {
                'area_id': area_id,
                'vehicle_id': emergency.emergency_id
            }
            s = RecordSerializer(data=record_data)
            if s.is_valid():
                s.save()
                return Response(data=Stact().succeed('Recording Success'), status=200)
            return Response(data=Stact().error(s.errors), status=400)

        else:
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
    subject = f'v: {violation_type}'
    message = f'You have one new violation: {violation_type}\nFine: {fine}$\nPoints: {deduction}points'
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
    
    #endorsement
    def post(self, request):
        s = TrafficviolationsSerializer(data=request.data)
        if s.is_valid():
            #Send to the user's email address, after sending successfully change email_status to 1 , according to the type of violation and violation level send different emails, minor penalty 500 yuan deduction of 3 points, serious penalty 1,000 yuan deduction of 6 points, a very serious penalty of 2,000 yuan deduction of 12 points, if the user's credit score is less than 60 points, delete the user
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
            return Response(data=Stact().succeed('Recording Success'),status=200)
        return Response(data=Stact().error(s.errors),status=400)


def send_email1(area_type,time,mail):
    for i in range(len(mail)):
        subject = f'Honourable owners:'
        message = f'Hello, there will be a traffic jam in the {area_type} area around {time}, please take a detour, thank you!！'
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [mail[i]]
        send_mail(subject, message, from_email, recipient_list) 
    return True


class AreaCondition(APIView):
    '''
    In order to optimise urban traffic, the department would like to analyse the flow of vehicles at different times of the day and identify areas prone to congestion. The system should provide insights to help manage and reduce traffic congestion.

        Suggested Approach.
        You should enhance the existing system by.

        Implementing a function that analyses the number of vehicles passing through a city junction at different times of day
        Identify congestion-prone areas based on traffic flow data.
        Key point: Consider using data visualisation tools to represent traffic flows and congestion patterns; in addition, implement algorithms to predict congestion times and suggest alternative routes to drivers via email when congestion is detected.


    
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
    Jump Visualisation
    """
    return render(request, 'line.html', {})

@xframe_options_exempt    
def jump_years1(request):
    """
    Jump Visualisation
    """
    return render(request, 'line2.html', {})

