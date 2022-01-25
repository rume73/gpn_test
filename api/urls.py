from django.conf.urls import include
from django.urls import path
from rest_framework import routers

from .views import DeviationViewSet


router = routers.DefaultRouter()
router.register(r'deviations', DeviationViewSet, base_name='deviations')


urlpatterns = [
    path('v1/', include(router.urls),),
]
