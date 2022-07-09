import datetime
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from nutrition.models import Nutrition
from nutrition.serializers import NutritionSerializer, ModifyGoalsOfDaySerializer
from nutrition.permissions import IsNutritionOwner
from user.models import Day


# Create your views here.
class NutritionAPIView(generics.ListCreateAPIView):
    queryset = Nutrition.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = NutritionSerializer

    def list(self, request, *args, **kwargs):
        try:
            date = datetime.date(
                kwargs['year'],
                kwargs['month'],
                kwargs['day']
            )
        except KeyError:
            date = datetime.date.today()
        try:
            day = Day.objects.get(user=request.user, date=date)
        except Day.DoesNotExist:
            if abs((datetime.date.today() - date).days) <= 30:
                day = Day.objects.create(date=date, user=request.user)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        nutrition = Nutrition.objects.filter(day=day)
        return Response({
            'limitCalories': day.limit_calories,
            'limitProteins': day.limit_proteins,
            'limitFats': day.limit_fats,
            'limitCarbohydrates': day.limit_carbohydrates,
            'goalCalories': day.goal_calories,
            'goalProteins': day.goal_proteins,
            'goalFats': day.goal_fats,
            'goalCarbohydrates': day.goal_carbohydrates,
            'entries': NutritionSerializer(nutrition, many=True).data
        })

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        try:
            date = datetime.date(
                kwargs['year'],
                kwargs['month'],
                kwargs['day']
            )
        except KeyError:
            date = datetime.date.today()
        try:
            day = Day.objects.get(user=request.user, date=date)
        except Day.DoesNotExist:
            if abs((datetime.date.today() - date).days) <= 30:
                day = Day.objects.create(date=date, user=request.user)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        nutrition = Nutrition(**serializer.validated_data, day=day)
        nutrition.save()
        return Response(NutritionSerializer(nutrition).data)


class ModifyNutritionAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Nutrition.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsNutritionOwner)
    serializer_class = NutritionSerializer


class ModifyGoalsAPIView(generics.UpdateAPIView):
    queryset = Day.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ModifyGoalsOfDaySerializer

    def update(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        try:
            date = datetime.date(
                kwargs['year'],
                kwargs['month'],
                kwargs['day']
            )
        except KeyError:
            date = datetime.date.today()
        try:
            day = Day.objects.get(user=request.user, date=date)
        except Day.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        instance = serializer.update(day, serializer.validated_data)
        return Response(ModifyGoalsOfDaySerializer(instance).data)