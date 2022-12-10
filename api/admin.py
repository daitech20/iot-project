from django.contrib import admin
from .models import DataLog, Config, Toggle

# Register your models here.
admin.site.register(DataLog)
admin.site.register(Config)
admin.site.register(Toggle)