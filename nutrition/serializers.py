from rest_framework import serializers
from nutrition.models import Nutrition
from user.models import Day


class NutritionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nutrition
        fields = ('id', 'time', 'name', 'calories', 'proteins', 'fats', 'carbohydrates', 'weight')
        extra_kwargs = {
            'name': {
                'required': True,
            },
            'weight': {
                'required': True,
            },
            'time': {
                'required': True,
                'format': '%H:%M',
            },
            'calories': {
                'required': True
            },
            'proteins': {
                'required': True
            },
            'fats': {
                'required': True
            },
            'carbohydrates': {
                'required': True
            }
        }


class ModifyGoalsOfDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = (
            'limit_calories',
            'goal_calories',
            'limit_proteins',
            'goal_proteins',
            'limit_fats',
            'goal_fats',
            'limit_carbohydrates',
            'goal_carbohydrates',
        )
        extra_kwargs = {
            'limit_calories': {
                'required': True,
            },
            'goal_calories': {
                'required': True,
            },
            'limit_proteins': {
                'required': True,
            },
            'goal_proteins': {
                'required': True,
            },
            'limit_fats': {
                'required': True,
            },
            'goal_fats': {
                'required': True,
            },
            'limit_carbohydrates': {
                'required': True,
            },
            'goal_carbohydrates': {
                'required': True,
            }
        }
