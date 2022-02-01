#from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from django.views import View

from rest_framework.renderers import TemplateHTMLRenderer


import subprocess

from .models import MediaFile
from .serializers import MediaSerializer

from .mediainfo import SerializeMediaFile

# Create your views here.
class MediaFiles(generics.ListCreateAPIView):
    queryset = MediaFile.objects.all()
    serializer_class = MediaSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
class MediaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MediaFile.objects.all()
    serializer_class = MediaSerializer
    

class FFMPEGVersion(APIView):
    """
    View to list installed FFMPEG version.

    """
    #renderer_classes = [TemplateHTMLRenderer]
    #template_name = './profile_list.html'
    
    def get(self, request, format=None):
        """
        Return local ffmpeg -version
        """
        myProcess = subprocess.check_output(['ffmpeg','-version'], encoding='utf8', text=True)
        myResponse = myProcess.replace("\n", "<br>")
        return Response({'profiles': myResponse})

class FFPROBE(View):
    """
    View to list installed FFMPEG version.

    """
    def get(self, request, format=None):
        """
        Return local ffmpeg -version
        """
        myProcess = subprocess.check_output(['ffprobe','-version'], encoding='utf8', text=True)
        myResponse = myProcess.replace("\n", "<br>")
        return HttpResponse(myResponse)
    
class GetMediaInfo(APIView):
    
    def get(self, request, format=None):
        inFile = request.data.get('target')
            
        mediaInfo = SerializeMediaFile(inFile)
        
        #if request.data.get('save') == "True":
        #    MediaFiles(mediaInfo)
        
        return Response(mediaInfo)
    