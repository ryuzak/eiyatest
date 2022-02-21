from django.shortcuts import get_object_or_404

from rest_framework import viewsets, status

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from vehicles.serializers import VehicleSerializer
from vehicles.models import Vehicle

class VehiclesViewSet(viewsets.ModelViewSet):
    '''
        ModelViewSet para listar vehiculos, crear nuevos vehiculos y
        CRUD de vehiculos

        data para crear y/o actualizar:
          * location: lugar origen del vehiculo -> string
          * fuel_km: consumo de combustible -> float
          * distance: distancia recorrida -> int
          * fuel_consume: combustible consumido -> float
    '''
    serializer_class = VehicleSerializer

    def get_queryset(self):
        return Vehicle.objects.all()

class VehicleUpdateLocationAPIView(APIView):
    permission_class = (AllowAny,)

    def put(self, request):
        '''
            Vista para actualizar ciudad del vehiculo

            data:
              * vehicle_id: id del vehiculo a mover
              * city: ciudad a la que se desea mover el vehiculo
            
            respuesta actualización de información
        '''
        vehicle_obj = get_object_or_404(Vehicle, pk=request.data.get('vehicle_id'))
        vehicle_obj.update_vehicle(request.data.get('city'))
        return Response({'message':'vehiculo actualizado'}, status=status.HTTP_200_OK)
