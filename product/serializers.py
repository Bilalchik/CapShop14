from rest_framework import serializers
from .models import Product, Brand, Category, Image, Storage, Color


class BrandListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('title', )


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title', )


class ProductListSerializer(serializers.ModelSerializer):
    brands = BrandListSerializer(many=True)
    category = CategoryListSerializer()

    class Meta:
        model = Product
        fields = (
            'id',
            'main_cover',
            'title',
            'description',
            'brands',
            'category',
            'actual_price'
        )


class StorageListSerializer(serializers.ModelSerializer):
    product = ProductListSerializer()

    class Meta:
        model = Storage
        fields = ('product', )
