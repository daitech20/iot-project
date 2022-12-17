import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name

        print("room name: ", self.room_name)
        print("room group: ", self.room_group_name)
        print("chanel name: ", self.channel_name)

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        # Send message to room group
        if "toggle" in text_data_json:
            toggle = text_data_json["toggle"]
            await self.channel_layer.group_send(
                self.room_group_name, {"type": "chat_message", "message": message, "toggle": toggle}
            )
        else:
            await self.channel_layer.group_send(
                self.room_group_name, {"type": "chat_message", "message": message}
            )

    # Receive message from room group
    async def chat_message(self, event):
        print("event", event)
        message = event["message"]
        # Send message to WebSocket
        if "toggle" in event:
            toggle = event["toggle"]
            await self.send(text_data=json.dumps({"message": message, "toggle": toggle}))
        else:
            await self.send(text_data=json.dumps({"message": message}))