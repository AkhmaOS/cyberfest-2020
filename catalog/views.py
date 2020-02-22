from rest_framework.viewsets import ModelViewSet

from .models import CatalogModel
from .serializers import CatalogSerializer


class CatalogViewSet(ModelViewSet):
    serializer_class = CatalogSerializer
    queryset = CatalogModel.objects.all()
    http_method_names = ['get', 'post', 'options']
