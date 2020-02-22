from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import RatingViewSet

router = SimpleRouter()
router.register(r'', RatingViewSet)

urlpatterns = [
    path('rating/', include(router.urls))
]