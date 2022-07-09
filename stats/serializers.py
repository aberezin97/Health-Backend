from rest_framework import serializers
from user.models import Day


class StatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = (
            'date',
            'weight',
            'eaten_calories',
            'eaten_fats',
            'eaten_proteins',
            'eaten_carbohydrates'
        )
        extra_kwargs = {
            'date': {
                'read_only': True,
            },
            'weight': {
                'read_only': True,
            },
            'eaten_calories': {
                'read_only': True,
            },
            'eaten_proteins': {
                'read_only': True,
            },
            'eaten_fats': {
                'read_only': True,
            },
            'eaten_carbohydrates': {
                'read_only': True,
            },
        }
