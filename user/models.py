from datetime import date
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


# Create your models here.
class User(AbstractUser):
    image = models.ImageField(null=True)
    email = models.EmailField(unique=True, blank=False)
    first_name = models.CharField(_("first name"), max_length=150, blank=False)
    last_name = models.CharField(_("last name"), max_length=150, blank=False)


class Day(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    date = models.DateField(default=date.today)
    weight = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        blank=True,
        null=True
    )

    limit_calories = models.IntegerField(default=0)
    limit_proteins = models.IntegerField(default=0)
    limit_fats = models.IntegerField(default=0)
    limit_carbohydrates = models.IntegerField(default=0)
    goal_calories = models.IntegerField(default=0)
    goal_proteins = models.IntegerField(default=0)
    goal_fats = models.IntegerField(default=0)
    goal_carbohydrates = models.IntegerField(default=0)
    eaten_calories = models.IntegerField(default=0)
    eaten_proteins = models.IntegerField(default=0)
    eaten_fats = models.IntegerField(default=0)
    eaten_carbohydrates = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user.username} - {self.date}'


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    name = models.CharField(max_length=256, blank=False, null=False)
    calories = models.DecimalField(max_digits=5, decimal_places=1, default=0.0)
    proteins = models.DecimalField(max_digits=5, decimal_places=1, default=0.0)
    fats = models.DecimalField(max_digits=5, decimal_places=1, default=0.0)
    carbohydrates = models.DecimalField(max_digits=5, decimal_places=1, default=0.0)

    class Meta:
        unique_together = ('user', 'name',)

    def __str__(self):
        return f'{self.user.username} - {self.name}'
