from django.db import models

# Create your object models here.

class MediaFile(models.Model):
  filename = models.CharField(max_length=255)
  filepath = models.CharField(max_length=255)
  size = models.IntegerField(default=0)
  bitrate = models.IntegerField(default=0, blank=True, null=True)
  audio_codec = models.CharField(max_length=20, blank=True, null=True)
  audio_bitrate = models.IntegerField(default=0, blank=True, null=True)
  audio_samplerate = models.IntegerField(default=0, blank=True, null=True)
  video_codec = models.CharField(max_length=20, blank=True, null=True)
  video_width = models.IntegerField(default=0, blank=True, null=True)
  video_height = models.IntegerField(default=0, blank=True, null=True)
  video_bitrate = models.IntegerField(default=0, blank=True, null=True)
  video_fps = models.IntegerField(default=0, blank=True, null=True)
  minutes = models.IntegerField(default=0, blank=True, null=True)
  lastscan = models.DateField(auto_now=True)
  fingerprint = models.CharField(unique=True, max_length=255, blank=True, null=True)
  kbpm = models.IntegerField(default=0, blank=True, null=True)
  
  # This def causes object to show as Title in the admin UI instead of Object_1
  def __str__(self):
    return self.fingerprint