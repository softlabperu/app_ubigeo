from rest_framework.viewsets import ModelViewSet

from app_ubigeo.api.serializers import *


class DepartamentoViewSet(ModelViewSet):
    serializer_class = DepartamentoSerializer
    queryset = Departamento.objects.all()


class ProvinciaViewSet(ModelViewSet):
    serializer_class = ProvinciaSerializer

    def get_queryset(self):
        id_filter = self.request.query_params.get('id_filter', '')
        if id_filter:
            return Provincia.objects.filter(departamento_id=self.request.query_params['id_filter'])
        return Provincia.objects.all()


class DistritoViewSet(ModelViewSet):
    serializer_class = DistritoSerializer

    def get_queryset(self):
        id_filter = self.request.query_params.get('id_filter', '')
        if id_filter:
            return Distrito.objects.filter(provincia_id=self.request.query_params['id_filter'])
        return Distrito.objects.all()
