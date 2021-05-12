from rest_framework import viewsets
from .models import Products
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all().order_by("-id")
    serializer_class = ProductSerializer
