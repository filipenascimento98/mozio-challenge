from django.contrib.gis.db import models


class Provider(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=50)
    language = models.CharField(max_length=2)
    currency = models.CharField(max_length=10)


class ServiceArea(models.Model):
    name = models.CharField(max_length=150)
    price = models.FloatField()
    coordinates = models.PolygonField(srid=4326)
    provider = models.ForeignKey(
        Provider,
        related_name='service_area',
        on_delete=models.CASCADE
    )
