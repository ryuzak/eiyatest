from math import dist
from rest_framework import serializers

from vehicles.models import Vehicle

class VehicleSerializer(serializers.ModelSerializer):
    '''
        Serializador para modelo de vehiculo
    '''
    class Meta:
        model = Vehicle
        fields = '__all__'

