from rest_framework import serializers
from exercises.models import Exercise


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ('id', 'name', 'approaches', 'counts')
        extra_kwargs = {
            'name': {
                'required': True,
            },
            'approaches': {
                'required': True,
            },
            'counts': {
                'required': True,
            },
        }