from rest_framework import serializers
from .models import MediaFile

class MediaSerializer(serializers.ModelSerializer):
  class Meta:
    model = MediaFile
    fields = [
        "pk",
        "filename",
        "filepath",
        "size",
        "minutes",
        "audio_codec",
        "audio_bitrate",
        "audio_samplerate",
        "video_codec",
        "video_bitrate",
        "video_fps",
        "lastscan",
        "fingerprint",
    ]
    extra_kwargs = {
        "audio_codec": {"required": False},
        "lastscan": {"required": False},
        "filename": {"required": False},
        "filepath": {"required": False},
        "size": {"required": False},
        "minutes": {"required": False},
        "audio_codec": {"required": False},
        "audio_bitrate": {"required": False},
        "audio_samplerate": {"required": False},
        "video_codec": {"required": False},
        "video_bitrate": {"required": False},
        "video_fps": {"required": False},
        "lastscan": {"required": False},
        "fingerprint": {"required": False},
    }
    