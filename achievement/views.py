from rest_framework.viewsets import ModelViewSet

from .models import AchievementModel
from .serializers import AchievementSerializer


class AchievementViewSet(ModelViewSet):
    serializer_class = AchievementSerializer
    queryset = AchievementModel.objects.all()
    http_method_names = ['get', 'post', 'options']
