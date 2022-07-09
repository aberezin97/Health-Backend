from rest_framework import generics, permissions
from rest_framework.response import Response
from user.models import Day
from stats.serializers import StatsSerializer

# Create your views here.
class StatsAPIView(generics.ListAPIView):
    queryset = Day.objects.order_by('-date')[:30]
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = StatsSerializer

    def list(self, request, *args, **kwargs):
        return Response(StatsSerializer(Day.objects.filter(user=request.user).order_by('date')[:30], many=True).data)