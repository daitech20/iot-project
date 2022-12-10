from rest_framework import serializers
from .models import Toggle, DataLog, Config

class ToggleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Toggle     


class DataLogSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = DataLog


class ConfigSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Config 