from signals.apps.related import models
from . import serializers
from signals.libs.views import APIViewSet

class JobViewSet(APIViewSet):
    queryset = models.Job.objects.all()
    serializer_class = serializers.JobSerializer

