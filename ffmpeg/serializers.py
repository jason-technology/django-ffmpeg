from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import MediaFile, InvalidMediaFile

class MediaSerializer(serializers.ModelSerializer):
  class Meta:
    model = MediaFile
    fields = [
        "pk",
        "filename",
        "filepath",
        "size",
        "bitrate",
        "minutes",
        "audio_codec",
        "audio_bitrate",
        "audio_samplerate",
        "video_codec",
        "video_width",
        "video_height",
        "video_bitrate",
        "video_fps",
        "lastscan",
        "fingerprint",
        "kbpm",
    ]

    extra_kwargs = {
        "audio_codec": {"required": False},
        "lastscan": {"required": False},
        "filename": {"required": False},
        "filepath": {"required": False},
        "size": {"required": False},
        "bitrate": {"required": False},
        "minutes": {"required": False},
        "audio_codec": {"required": False},
        "audio_bitrate": {"required": False},
        "audio_samplerate": {"required": False},
        "video_codec": {"required": False},
        "video_width": {"required": False},
        "video_height": {"required": False},
        "video_bitrate": {"required": False},
        "video_fps": {"required": False},
        "lastscan": {"required": False},
        "fingerprint": {"required": True},
    }
    
    
    
class InvalidMediaSerializer(serializers.ModelSerializer):
  class Meta:
    model = InvalidMediaFile
    fields = [
        "pk",
        "filename",
        "filepath",
        "filepath",
        "scandate",
        "status",
    ]

    extra_kwargs = {
        "filename": {"required": True},
        "filepath": {"required": True},
        "lastscan": {"required": True},
        "status": {"required": True},
    }