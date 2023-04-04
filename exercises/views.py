import datetime

from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from exercises.models import Exercise
from exercises.serializers import ExerciseSerializer
from user.models import Day, User, Permission
from exercises.permissions import IsExerciseOwner, IsAllowedToReadWriteExercises


class ExercisesAPIView(generics.ListCreateAPIView):
    queryset = Exercise.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsAllowedToReadWriteExercises)
    serializer_class = ExerciseSerializer

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
                if permission.exercises == 2:
                    create_new_day = True
            if create_new_day and abs((datetime.date.today() - date).days) <= 30:
                day = Day.objects.create(date=date, user=user)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        exercises = Exercise.objects.filter(day=day)
        return Response(ExerciseSerializer(exercises, many=True).data)

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
        exercise = Exercise(**serializer.validated_data, day=day)
        exercise.save()
        return Response(ExerciseSerializer(exercise).data)


class ModifyExerciseAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Exercise.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsAllowedToReadWriteExercises)
    serializer_class = ExerciseSerializer
