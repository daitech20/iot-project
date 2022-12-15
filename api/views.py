from django.shortcuts import render
from .serializer import ToggleSerializer, DataLogSerializer, ConfigSerializer
from .models import Toggle, DataLog, Config
from rest_framework import generics, status
from rest_framework.response import Response

# Create your views here.
class ListDataLogs(generics.ListCreateAPIView):
    queryset = DataLog.objects.all()
    serializer_class = DataLogSerializer

class ToggleUpdate(generics.RetrieveUpdateAPIView):
    queryset = Toggle.objects.all()
    serializer_class = ToggleSerializer
    lookup_field = 'id'

class ConfigUpdate(generics.RetrieveUpdateAPIView):
    queryset = Config.objects.all()
    serializer_class = ConfigSerializer
    lookup_field = 'id'

def index(request):
    return render(request, "logs/index.html")

def room(request, room_name):
    return render(request, "logs/room.html", {"room_name": room_name})