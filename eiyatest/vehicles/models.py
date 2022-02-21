from statistics import mode
from django.db import models

# Create your models here.
class Vehicle(models.Model):
    location = models.CharField(max_length=2, verbose_name='Ubicación Actual')
    fuel_km = models.FloatField(default=0, verbose_name='Consumo km/lt')
    distance = models.IntegerField(default=1, verbose_name='Distancia recorrida')
    fuel_consume = models.FloatField(default=0, verbose_name='Combustible consumido')

    class Meta:
        db_table = 'vehicles'
        ordering = ['id']

    
    def update_vehicle(self, city):
        '''
            Función para actualizar la ciudad, distancia recorrida y combustible consumido

            parametros:
              * self: clase padre
              * city: ciudad a trasladar

            sin retorno
        '''
        distance = 0
        if (self.location.lower()=='a' and city.lower()=='b') or (self.location.lower()=='b' and city.lower()=='a'):
            distance = 1
        elif (self.location.lower()=='c' and city.lower()=='b') or (self.location.lower()=='b' and city.lower()=='c'):
            distance = 4
        elif (self.location.lower()=='a' and city.lower()=='c') or (self.location.lower()=='c' and city.lower()=='a'):
            distance = 2
        elif self.location.lower() == city.lower():
            pass

        self.location = city.lower()
        self.distance += distance
        self.fuel_consume += (distance * self.fuel_km)
        self.save()

        return self


        