from django.db import models
from user.models import Day


# Create your models here.
class Nutrition(models.Model):
    day = models.ForeignKey(Day, on_delete=models.CASCADE, related_name="nutrition")
    time = models.TimeField(null=True)
    name = models.CharField(max_length=256, blank=False, null=True)
    calories = models.DecimalField(max_digits=5, decimal_places=1, default=0.0)
    proteins = models.DecimalField(max_digits=5, decimal_places=1, default=0.0)
    fats = models.DecimalField(max_digits=5, decimal_places=1, default=0.0)
    carbohydrates = models.DecimalField(max_digits=5, decimal_places=1, default=0.0)
    weight = models.IntegerField()

    def __str__(self):
        return f'{self.day} - {self.time} - {self.name}'


class Liquid(models.Model):
    day = models.ForeignKey(Day, on_delete=models.CASCADE, related_name='liquid')
    time = models.TimeField(null=True)
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.day} - {self.time} - {self.quantity}'
