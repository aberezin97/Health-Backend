import datetime
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from exercises.models import Exercise
from exercises.serializers import ExerciseSerializer
from user.models import Day
from exercises.permissions import IsExerciseOwner


class ExercisesAPIView(generics.ListCreateAPIView):
    queryset = Exercise.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ExerciseSerializer

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
        exercises = Exercise.objects.filter(day=day)
        return Response(ExerciseSerializer(exercises, many=True).data)

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
        exercise = Exercise(**serializer.validated_data, day=day)
        exercise.save()
        return Response(ExerciseSerializer(exercise).data)


class ModifyExerciseAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Exercise.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsExerciseOwner)
    serializer_class = ExerciseSerializer
