from rest_framework.viewsets import ModelViewSet

from .models import RatingModel
from .serializers import RatingSerializer


class RatingViewSet(ModelViewSet):
    serializer_class = RatingSerializer
    queryset = RatingModel.objects.all()
    http_method_names = ['get', 'post', 'options']
