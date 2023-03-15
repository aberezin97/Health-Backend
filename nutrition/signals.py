from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from nutrition.models import Nutrition

@receiver([post_save, post_delete], sender=Nutrition)
def calculate_day_intake(sender, instance=None, created=False, **kwargs):
    day = instance.day
    calories = 0
    proteins = 0
    fats = 0
    carbohydrates = 0
    for nutrition in day.nutrition.all():
        calories += nutrition.calories / 100 * nutrition.weight
        proteins += nutrition.proteins / 100 * nutrition.weight
        fats += nutrition.fats / 100 * nutrition.weight
        carbohydrates += nutrition.carbohydrates / 100 * nutrition.weight
    day.eaten_calories = calories
    day.eaten_proteins = proteins
    day.eaten_fats = fats
    day.eaten_carbohydrates = carbohydrates
    day.save()