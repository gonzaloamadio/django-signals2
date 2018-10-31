from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our viewsets with it.
app_name='relation'
router = DefaultRouter()
router.register(r'relation', views.RelationViewSet, base_name="relation-relation")
urlpatterns = router.urls


