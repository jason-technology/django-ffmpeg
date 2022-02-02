from django.contrib import admin

# Register your models here.
from .models import MediaFile, InvalidMediaFile
admin.site.register(MediaFile)
admin.site.register(InvalidMediaFile)