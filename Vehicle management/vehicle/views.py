from django.shortcuts import render
from rest_framework.views import APIView
from .models import Plate, User, Vehicle, Record
from .serializers import PlateSerializer, UserSerializer, VehicleSerializer, RecordSerializer,TrafficviolationsSerializer
from rest_framework.response import Response
from django.core.mail import send_mail
from django11 import settings

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
class PlateRegistration(APIView):
    def get(self, request):
        # Returns licence plate numbers whose status is not 0
        plates = Plate.objects.filter(plate_status=0)
        s = PlateSerializer(plates, many=True)
        return render(request, 'plate.html', {'plates': s.data})
    
    def post(self, request):
        #Registered Vehicle Registration Numbers
        s = VehicleSerializer(data=request.data)
        if s.is_valid():
            #Change the plate meter licence plate number status to 1 after successful registration
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

    #Identify and record licence plate numbers
    def post(self, request):
        # Print the data from the Vehicle table
        plate_ids = list(Plate.objects.filter(plate_number=request.data['vehicle_plate']).values_list('plate_id', flat=True))
        mutable_data = Vehicle.objects.filter(vehicle_plate__in=plate_ids).first()

        if mutable_data:
            record_data = {
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
    subject = f'endorsement: {violation_type}'
    message = f'You have a new violation: {violation_type}\nfine: {fine}$\ndeduct marks: {deduction}ingredient'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = ['3037160185@qq.com']
    send_mail(subject, message, from_email, recipient_list) 
    return True


class Violation(APIView):
    def get(self, request):
        context = {
            'range_3': range(3),
        }
        return render(request, 'trafficviolations.html',context=context)
    
    # Violation records
    def post(self, request):
        s = TrafficviolationsSerializer(data=request.data)
        if s.is_valid():
            #Send to user's mailbox, change email_status to 1 after successful sending, send different emails according to the type of violation and the level of violation, minor penalty 500 RMB deduction of 3 points, serious penalty 1,000 RMB deduction of 6 points, very serious penalty 2,000 RMB deduction of 12 points, if the user's credit score is less than 60 points, then delete the user
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
        
    

