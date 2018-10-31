from signals.apps.relation import models
from . import serializers
from signals.libs.views import APIViewSet

class RelationViewSet(APIViewSet):
    queryset = models.Relation.objects.all()
    serializer_class = serializers.RelationSerializer

