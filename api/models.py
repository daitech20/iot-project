from django.db import models
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
# Create your models here.


class Toggle(models.Model):
    value = models.BooleanField(default=False)

class DataLog(models.Model):
    time = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # channel_layer = get_channel_layer()

        super().save(*args, **kwargs)
        # async_to_sync(channel_layer.group_send)(
        #     "chat_o", {"type": "chat_message", "message": str(self.time)}
        # )

class Config(models.Model):
    delay = models.IntegerField(default=1000)