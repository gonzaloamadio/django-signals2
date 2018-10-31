from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our viewsets with it.
app_name='related'
router = DefaultRouter()
router.register(r'jobs', views.JobViewSet, base_name="related-job")
urlpatterns = router.urls

