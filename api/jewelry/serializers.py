from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import Jewelry


class JewelryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jewelry
        fields = '__all__'

