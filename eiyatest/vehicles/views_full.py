from django.shortcuts import render
from django.template.loader import render_to_string

from vehicles.models import Vehicle
from vehicles.serializers import VehicleSerializer

def retrieveVehicles(request):
    '''
        función para devolver template con listado de vehiculos
    '''
    vehicles_list = Vehicle.objects.all().order_by('location')
    return render(request, 'vehicles.html', {'vehicles_list':vehicles_list})

#def updateTable(request):
#    vehicles_list = Vehicle.objects.all().order_by('location')
#    return render_to_string(request, 'table_partial.html', {'vehicles_list':vehicles_list})
