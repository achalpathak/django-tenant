from rest_framework import routers
from .apis import ProductViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r"products", ProductViewSet)

urlpatterns = [path("", include(router.urls))]
