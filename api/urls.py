from django.urls import path, include
from .views import ListDataLogs, ToggleUpdate, ConfigUpdate, index, room


urlpatterns = [
    path('api/list-data-logs', ListDataLogs.as_view()),
    path('api/update/toggle/<int:id>', ToggleUpdate.as_view()),
    path('api/update/config/<int:id>', ConfigUpdate.as_view()),
    path("", index, name="index"),
    path("chat/<str:room_name>/", room, name="room"),
]