import datetime
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from weight.serializers import WeightSerializer
from user.models import Day, User
from user.permissions import IsDayOwner
from weight.permissions import IsAllowedToReadWriteWeight


# Create your views here.
class WeightAPIView(generics.ListCreateAPIView):
    queryset = Day.objects.exclude(weight=None)
    permission_classes = (permissions.IsAuthenticated, IsAllowedToReadWriteWeight)
    serializer_class = WeightSerializer

    def list(self, request, *args, **kwargs):
        user_id = kwargs['user_id']
        user = User.objects.get(pk=user_id)
        # serializer = self.serializer_class(data=request.data, context={'request': request})
        # serializer.is_valid(raise_exception=True)
        return Response(WeightSerializer(Day.objects.filter(user=user).exclude(weight=None), many=True).data)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        date = serializer.validated_data['date']
        try:
            day = Day.objects.get(user=request.user, date=date)
            if day.weight is not None:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except Day.DoesNotExist:
            if abs((datetime.date.today() - date).days) <= 30:
                day = Day.objects.create(date=date, user=request.user)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        instance = serializer.update(day, serializer.validated_data)
        return Response(WeightSerializer(instance).data)


class ModifyWeightAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Day.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsDayOwner)
    serializer_class = WeightSerializer

    def destroy(self, request, *args, **kwargs):
        try:
            day = Day.objects.get(pk=kwargs['pk'])
        except Day.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        day.weight = None
        day.save()
        return Response(status=status.HTTP_204_NO_CONTENT)