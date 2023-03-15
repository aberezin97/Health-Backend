from django.db import models
from user.models import Day


# Create your models here.
class Exercise(models.Model):
    day = models.ForeignKey(Day, on_delete=models.CASCADE, related_name='exercise')
    name = models.CharField(max_length=256, blank=False, null=True)
    approaches = models.IntegerField()
    counts = models.IntegerField()

    def __str__(self):
        return f'{self.day} - {self.name}'