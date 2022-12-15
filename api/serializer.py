from rest_framework import serializers
from .models import Toggle, DataLog, Config
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

class ToggleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Toggle     


class DataLogSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = DataLog

    def save(self, **kwargs):
        channel_layer = get_channel_layer()
        datalog = super().save(**kwargs)
        async_to_sync(channel_layer.group_send)(
            "chat_iot", {"type": "chat_message", "message": str(datalog.time) + " co trom dot nhap!"}
        )
        return datalog

        

class ConfigSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Config 