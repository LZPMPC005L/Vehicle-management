from django.shortcuts import render
from rest_framework.views import APIView
from .models import Plate, User, Vehicle, Record
from .serializers import PlateSerializer, UserSerializer, VehicleSerializer, RecordSerializer
from rest_framework.response import Response

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
        # Returns licence plate numbers whose status is not 0
        plates = Plate.objects.filter(plate_status=0)
        s = PlateSerializer(plates, many=True)
        return Response(data=Stact().succeed(s.data),status=200)
    
    def post(self, request):
        #Registered Vehicle Registration Numbers
        s = VehicleSerializer(data=request.data)
        if s.is_valid():
            # Change the plate meter licence plate number status to 1 after successful registration
            plate = Plate.objects.get(plate_id=request.data['vehicle_plate'])
            plate.plate_status = 1
            plate.save()
            s.save()
            return Response(data=Stact().succeed('Successful registration'),status=200)
        return Response(data=Stact().error(s.errors),status=400)

class UserRegistration(APIView):
    #User Registration
    def post(self, request):
        s = UserSerializer(data=request.data)
        if s.is_valid():
            s.save()
            return Response(data=Stact().succeed('Successful registration'),status=200)
        return Response(data=Stact().error(s.errors),status=400)

class IdentfitionRecord(APIView):
    #Identify and record licence plate numbers
    def post(self, request):
        s = RecordSerializer(data=request.data)
        if s.is_valid():
            s.save()
            return Response(data=Stact().succeed('Recording Success'),status=200)
        return Response(data=Stact().error(s.errors),status=400)
