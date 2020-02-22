from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import AchievementViewSet

router = SimpleRouter()
router.register(r'', AchievementViewSet)

urlpatterns = [
    path('achievement/', include(router.urls))
]