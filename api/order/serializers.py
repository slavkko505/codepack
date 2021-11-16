from rest_framework import serializers
from .models import Order
from api.jewelry.serializers import JewelryListSerializer


class OrderSerializer(serializers.ModelSerializer):
    meeting = JewelryListSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'jewelry', 'ordered_date', )


class OrderDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'
