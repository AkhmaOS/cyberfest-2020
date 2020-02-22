from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import CatalogViewSet

router = SimpleRouter()
router.register(r'', CatalogViewSet)

urlpatterns = [
    path('catalog/', include(router.urls))
]