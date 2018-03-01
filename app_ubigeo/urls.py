from django.conf.urls import url, include
from rest_framework import routers

from app_ubigeo.api.views import *

router = routers.DefaultRouter()
router.register(r'departamento', DepartamentoViewSet, base_name='departamento')
router.register(r'provincia', ProvinciaViewSet, base_name='provincia')
router.register(r'distrito', DistritoViewSet, base_name='distrito')

urlpatterns = [
    url(r'^api/', include(router.urls, namespace='api')),
]
