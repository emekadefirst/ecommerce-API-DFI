from rest_framework import serializers
from .models import *

"""GET Serializers"""

class CartSerializer(serializers.Serializer):
    class Meta:
        model = Cart
        fields = ['user']


class CartItemSerializers(serializers.ModelSerializer):
    cart = CartSerializer()
    class Meta:
        model = CartItem
        fields = ['cart', 'product', 'quantity']

"""POST serializers"""
class CreateCartItemSerializer(serializers.ModelSerializer):
    cart = serializers.SlugField(slug_field="id", queryset=Cart.objects.all())
    product = serializers.SlugField(slug_field="name", queryset=Product.objects.all())

    class Meta:
        model = CartItem
        fields = ['cart', 'product', 'quantity']

    def create(self, validated_data):
        return CartItem.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.quantity = validated_data.get("quantity", instance.quantity)
        return instance
