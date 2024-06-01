from django.shortcuts import render
from rest_framework import viewsets
from drf_spectacular.utils import extend_schema
from .models import Category, Brand, Product, ProductLine
from .serializers import (
    CategorySerializer,
    BrandSerializer,
    ProductSerializer,
    ProductLineSerializer,
)
from rest_framework.response import Response


class CategoryViewSet(viewsets.ViewSet):
    """
    Simple Viewset for viewing all categories.
    """

    queryset = Category.objects.all()

    @extend_schema(responses=CategorySerializer)
    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)


class BrandViewSet(viewsets.ViewSet):
    """
    Simple Viewset for viewing all brands.
    """

    queryset = Brand.objects.all()

    @extend_schema(responses=BrandSerializer)
    def list(self, request):
        serializer = BrandSerializer(self.queryset, many=True)
        return Response(serializer.data)


class ProductViewSet(viewsets.ViewSet):
    """
    Simple Viewset for viewing all products.
    """

    queryset = Product.objects.all()

    @extend_schema(responses=ProductSerializer)
    def list(self, request):
        serializer = ProductSerializer(self.queryset, many=True)
        return Response(serializer.data)


class ProductLineViewSet(viewsets.ViewSet):
    """
    Simple Viewset for viewing all productlines.
    """

    queryset = ProductLine.objects.all()

    @extend_schema(responses=ProductLineSerializer)
    def list(self, request):
        serializer = ProductLineSerializer(self.queryset, many=True)
        return Response(serializer.data)
