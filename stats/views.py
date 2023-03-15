from rest_framework import generics, permissions
from rest_framework.response import Response
from user.models import Day, User
from stats.serializers import StatsSerializer
from django.shortcuts import get_object_or_404
from stats.permissions import IsAllowedToReadStats


# Create your views here.
class StatsAPIView(generics.ListAPIView):
    queryset = Day.objects.order_by('-date')[:30]
    permission_classes = (permissions.IsAuthenticated, IsAllowedToReadStats)
    serializer_class = StatsSerializer

    def list(self, request, *args, **kwargs):
        user = get_object_or_404(User.objects.all(), pk=kwargs['user_id'])
        return Response(StatsSerializer(Day.objects.filter(user=user).order_by('date')[:30], many=True).data)