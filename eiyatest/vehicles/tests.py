from django.test import TestCase

from vehicles.models import Vehicle
from vehicles.serializers import VehicleSerializer


# Create your tests here.
class VehicleTest(TestCase):
    def setUp(self):
        self.vehicle_obj = {
            'location' : 'a',
            'fuel_km' : 2,
            'distance' : 0,
            'fuel_consume' : 0
        }

        self.vehicle_test = Vehicle.objects.create(
            location = 'b',
            fuel_km=4,
            distance = 0,
            fuel_consume = 0
        )

    def test_create_vehicle(self):
        vehicle = VehicleSerializer(data=self.vehicle_obj)
        vehicle.is_valid()
        vehicle.save()
        self.assertIsNotNone(vehicle.instance.pk)

    def test_update_distance_vehicle(self):
        vehicle = self.vehicle_test
        old = vehicle.distance
        vehicle.update_vehicle('c')
        self.assertNotEqual(old, vehicle.distance)