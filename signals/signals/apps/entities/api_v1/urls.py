from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our viewsets with it.
app_name='entities'
router = DefaultRouter()
router.register(r'persons', views.PersonViewSet, base_name="entities-persons")
router.register(r'companies', views.CompanyViewSet, base_name="entities-companies")
urlpatterns = router.urls

