from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from .models import Product, Stock
from .serializers import ProductSerializer, StockSerializer

class ProductPagination(PageNumberPagination):
    page_size = 10

class ProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.query_params.get('name', None)
        description = self.request.query_params.get('description', None)
        if name:
            queryset = queryset.filter(name__icontains=name)
        if description:
            queryset = queryset.filter(description__icontains=description)
        return queryset

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class StockPagination(PageNumberPagination):
    page_size = 10

class StockListView(generics.ListCreateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    pagination_class = StockPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        product_id = self.request.query_params.get('product_id', None)
        if product_id:
            queryset = queryset.filter(stockproduct__product_id=product_id)
        return queryset

class StockDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
