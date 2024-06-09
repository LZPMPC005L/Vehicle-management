from django import forms
from rest_framework import serializers
from .models import Plate, User, Vehicle, Record, ViolationType, Trafficviolations


class PlateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plate
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = '__all__'

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ViolationType
        fields = '__all__'


class TrafficviolationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trafficviolations
        fields = '__all__'