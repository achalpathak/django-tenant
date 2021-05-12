from rest_framework import serializers

from .models import Products


class ProductSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=100, required=True)
    description = serializers.CharField(max_length=250, required=True)
    price = serializers.IntegerField(required=True)

    class Meta:
        model = Products
        fields = ("id", "title", "description", "price")
