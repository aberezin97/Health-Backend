from rest_framework import serializers
from user.models import Day


class WeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = ('id', 'date', 'weight')
        extra_kwargs = {
            'date': {
                'required': True,
            },
            'weight': {
                'required': True,
            },
        }
