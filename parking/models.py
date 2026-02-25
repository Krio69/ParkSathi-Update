from django.db import models

class Parking(models.Model):
    name = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()
    total_slots = models.IntegerField(default=50)
    available_slots = models.IntegerField(default=20)
    price_per_hour = models.FloatField(default=20)

    def __str__(self):
        return self.name