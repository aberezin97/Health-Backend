import datetime
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from nutrition.models import Nutrition, Liquid
from nutrition.serializers import NutritionSerializer, ModifyGoalsOfDaySerializer, LiquidSerializer
from nutrition.permissions import IsAllowedToModifyDeleteNutrition, IsAllowedToReadWriteNutrition
from user.models import Day, User, Permission
from django.shortcuts import get_object_or_404


# Create your views here.
class NutritionAPIView(generics.ListCreateAPIView):
    queryset = Nutrition.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsAllowedToReadWriteNutrition)
    serializer_class = NutritionSerializer

    def list(self, request, *args, **kwargs):
        user_id = kwargs['user_id']
        user = User.objects.get(pk=user_id)
        try:
            date = datetime.date(
                kwargs['year'],
                kwargs['month'],
                kwargs['day']
            )
        except KeyError:
            date = datetime.date.today()
        try:
            day = Day.objects.get(user=user, date=date)
        except Day.DoesNotExist:
            create_new_day = False
            if user_id == request.user.id:
                create_new_day = True
            else:
                permission = get_object_or_404(Permission.objects.all(), sender=user, receiver=request.user)
                if permission.nutrition == 2:
                    create_new_day = True
            if create_new_day and abs((datetime.date.today() - date).days) <= 30:
                day = Day.objects.create(date=date, user=user)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        nutrition = Nutrition.objects.filter(day=day)
        liquid = Liquid.objects.filter(day=day)
        return Response({
            'goal_liquid': day.goal_liquid,
            'limitCalories': day.limit_calories,
            'limitProteins': day.limit_proteins,
            'limitFats': day.limit_fats,
            'limitCarbohydrates': day.limit_carbohydrates,
            'goalCalories': day.goal_calories,
            'goalProteins': day.goal_proteins,
            'goalFats': day.goal_fats,
            'goalCarbohydrates': day.goal_carbohydrates,
            'entries': NutritionSerializer(nutrition, many=True).data,
            'liquidEntries': LiquidSerializer(liquid, many=True).data
        })

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user_id = kwargs['user_id']
        user = User.objects.get(pk=user_id)
        try:
            date = datetime.date(
                kwargs['year'],
                kwargs['month'],
                kwargs['day']
            )
        except KeyError:
            date = datetime.date.today()
        try:
            day = Day.objects.get(user=user, date=date)
        except Day.DoesNotExist:
            if abs((datetime.date.today() - date).days) <= 30:
                day = Day.objects.create(date=date, user=user)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        nutrition = Nutrition(**serializer.validated_data, day=day)
        nutrition.save()
        return Response(NutritionSerializer(nutrition).data)


class LiquidAPIView(generics.ListCreateAPIView):
    queryset = Liquid.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsAllowedToReadWriteNutrition)
    serializer_class = LiquidSerializer

    def list(self, request, *args, **kwargs):
        user_id = kwargs['user_id']
        user = User.objects.get(pk=user_id)
        try:
            date = datetime.date(
                kwargs['year'],
                kwargs['month'],
                kwargs['day']
            )
        except KeyError:
            date = datetime.date.today()
        try:
            day = Day.objects.get(user=user, date=date)
        except Day.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        liquid = Liquid.objects.filter(day=day)
        return Response(LiquidSerializer(liquid, many=True).data)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user_id = kwargs['user_id']
        user = User.objects.get(pk=user_id)
        try:
            date = datetime.date(
                kwargs['year'],
                kwargs['month'],
                kwargs['day']
            )
        except KeyError:
            date = datetime.date.today()
        try:
            day = Day.objects.get(user=user, date=date)
        except Day.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        liquid = Liquid(**serializer.validated_data, day=day)
        liquid.save()
        return Response(LiquidSerializer(liquid).data)


class DeleteLiquidAPIView(generics.DestroyAPIView):
    queryset = Liquid.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsAllowedToModifyDeleteNutrition)
    serializer_class = LiquidSerializer


class ModifyNutritionAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Nutrition.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsAllowedToModifyDeleteNutrition)
    serializer_class = NutritionSerializer


class ModifyGoalsAPIView(generics.UpdateAPIView):
    queryset = Day.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsAllowedToReadWriteNutrition)
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