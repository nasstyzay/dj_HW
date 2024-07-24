from rest_framework import serializers
from .models import Product, Stock, StockProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class StockProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProduct
        fields = ('product', 'price')


class StockSerializer(serializers.ModelSerializer):
    products = StockProductSerializer(many=True, write_only=True)

    class Meta:
        model = Stock
        fields = '__all__'

    def create(self, validated_data):
        products_data = validated_data.pop('products')
        stock = Stock.objects.create(**validated_data)
        for product_data in products_data:
            StockProduct.objects.create(stock=stock, **product_data)
        return stock

    def update(self, instance, validated_data):
        products_data = validated_data.pop('products')
        instance.address = validated_data.get('address', instance.address)
        instance.save()

        for product_data in products_data:
            product, created = StockProduct.objects.update_or_create(
                stock=instance,
                product=product_data['product'],
                defaults={'price': product_data['price']}
            )
        return instance
