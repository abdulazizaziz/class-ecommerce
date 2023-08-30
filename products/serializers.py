from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class VariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variant
        fields = ['name']

class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    category = CategorySerializer()
    variants = VariantSerializer(many=True)
    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'price',
            'description',
            'weight',
            'unit',
            'photo',
            'created',
            'updated',
            'brand',
            'category',
            'variants',
        ]

class ProductPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'