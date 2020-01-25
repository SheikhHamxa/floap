from django.db import models
# from USer.models import USer
# from USer.models import USer
from location.models import Franchise


class VehicleType(models.Model):
    type = (
        ('CAR', 'Car'),
        ('BIKE', 'Bike'),
            )
    vehicle_type = models.CharField(max_length=5, choices=type , unique= True)
    owner = models.ForeignKey('auth.User', related_name='vehicletype', on_delete=models.CASCADE)

    def __str__(self):
        return self.vehicle_type


class Vehicle(models.Model):
    name = models.CharField(max_length=100, null=True)
    reg_no = models.IntegerField(unique=True, null=True)
    total_tyre =(
        ('2', 'Two'),
        ('4', 'Four')
    )
    tyre=models.CharField(max_length=15, choices= total_tyre)
    vehicle_type=models.ForeignKey(VehicleType, related_name='vehicle', on_delete=models.CASCADE)
    franchise=models.ForeignKey(Franchise, related_name='vehicle', on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User', related_name='vehicle', on_delete=models.CASCADE)
    # user = models.ForeignKey('USer.USer', related_name='vehicle', on_delete=models.CASCADE)

    def __str__(self):
        template = ' {0.vehicle_type} {0.name} {0.reg_no} {0.franchise}'
        return template.format(self)