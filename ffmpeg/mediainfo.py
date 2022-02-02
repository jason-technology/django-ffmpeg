from converter import Converter
import json, os, hashlib

from .serializers import MediaSerializer

def SerializeMediaFile(inFile):
    
    fileName = os.path.basename(inFile)
    filePath = os.path.dirname(inFile)
    mediaInstance = Converter()
    validMediaFile = None
 
    #Determine if file is a valid media file
    try:
        mediaInfo = mediaInstance.probe(inFile)
        fileFingerprint = hashlib.sha1(str(mediaInfo).encode())
        streamTest = mediaInfo.__dict__["streams"][0].__dict__["type"]
    
        #Determine which stream is audio and video
        if streamTest == "video":
            videoStream = 0
            audioStream = 1
        else:
            videoStream = 1
            audioStream = 0
            validMediaFile = True
    except:
        validMediaFile = False
        print("not a valid media file")
    

    
    if validMediaFile:
        serializedMediaInfo = {
            "audio_codec": mediaInfo.__dict__["streams"][audioStream].__dict__["codec"],
            "audio_bitrate": mediaInfo.__dict__["streams"][audioStream].__dict__["bitrate"],
            "audio_samplerate": mediaInfo.__dict__["streams"][audioStream].__dict__["audio_samplerate"],
            "video_codec": mediaInfo.__dict__["streams"][videoStream].__dict__["codec"],
            "video_width": mediaInfo.__dict__["streams"][videoStream].__dict__["video_width"],
            "video_height": mediaInfo.__dict__["streams"][videoStream].__dict__["video_height"],
            "video_bitrate": mediaInfo.__dict__["streams"][videoStream].__dict__["bitrate"],
            "video_fps": mediaInfo.__dict__["streams"][videoStream].__dict__["video_fps"],
            "filename": fileName,
            "filepath": filePath,
            "minutes": mediaInfo.__dict__["format"].__dict__["duration"],
            "size": mediaInfo.__dict__["format"].__dict__["size"],
            "bitrate": mediaInfo.__dict__["format"].__dict__["bitrate"],
            "fingerprint": str(fileFingerprint.hexdigest()),
            "kbpm": mediaInfo.__dict__["format"].__dict__["size"] / mediaInfo.__dict__["format"].__dict__["duration"]
        }
    
        if serializedMediaInfo["audio_bitrate"] is not None:
            serializedMediaInfo["audio_bitrate"] = int(serializedMediaInfo["audio_bitrate"])
        if serializedMediaInfo["audio_samplerate"] is not None:
            serializedMediaInfo["audio_samplerate"] = int(serializedMediaInfo["audio_samplerate"])
        if serializedMediaInfo["video_fps"] is not None:
            serializedMediaInfo["video_fps"] = int(serializedMediaInfo["video_fps"])
        if serializedMediaInfo["minutes"] is not None:
            serializedMediaInfo["minutes"] = int(serializedMediaInfo["minutes"])
        if serializedMediaInfo["kbpm"] is not None:
            serializedMediaInfo["kbpm"] = int(serializedMediaInfo["kbpm"])       
        
    else:
        serializedMediaInfo = {}
     
    serializedMediaFile = MediaSerializer(data=serializedMediaInfo)
    
    #try:
    #    serializedMediaFile.is_valid(raise_exception=True)
    #except:
    #    return SerializeMediaFile.errors
    
    if serializedMediaFile.is_valid():
        serializedMediaFile.save()
        return serializedMediaFile.data
    else:
        return serializedMediaFile.errors


#inFile = '/Users/Jason/Projects/mediamanager/1_min_later.m4v'

#json_info = SerializeMediaInfo(inFile)

#print(json_info)

#fileFingerprint = subprocess.check_output(['md5','-q', '-s', json_info], encoding='utf8', text=True)

#print(tempData)

# info.__dict__ reference
#{
#    'format': MediaFormatInfo(format=mov,mp4,m4a,3gp,3g2,mj2, duration=2.27), 
#    'posters_as_video': True, 
#    'streams': [
    #   MediaStreamInfo(type=audio, codec=aac, channels=2, rate=44100, bitrate=129367, creation_time=2021-11-22T23:24:24.000000Z, language=eng, handler_name=SoundHandler, vendor_id=[0][0][0][0]), MediaStreamInfo(type=video, codec=h264, width=1280, height=720, fps=30.0, bitrate=408181, creation_time=2021-11-22T23:24:24.000000Z, language=eng, handler_name=VideoHandler, vendor_id=[0][0][0][0])
    # ]
#}

#info.__dict__["streams"][0].__dict__ reference (as json)
#{
    #"index": 0, 
    #"type": "audio", 
    #"codec": "aac", 
    #"codec_desc": "AAC (Advanced Audio Coding)", 
    # "duration": 2.252313, 
    # "bitrate": 129367, 
    # "video_width": null, 
    # "video_height": null, 
    # "video_fps": null, 
    # "audio_channels": 2, 
    # "audio_samplerate": 44100.0, 
    # "attached_pic": 0, 
    # "sub_forced": null, 
    # "sub_default": null, 
    # "metadata": {
        # "creation_time": "2021-11-22T23:24:24.000000Z", 
        # "language": "eng", 
        # "handler_name": "SoundHandler", 
        # "vendor_id": "[0][0][0][0]"
    #}
#}

#info.__dict__["streams"][1].__dict__ reference (as json)
#{
    # "index": 1, 
    # "type": "video", 
    # "codec": "h264", 
    # "codec_desc": "H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10", 
    # "duration": 2.268933, 
    # "bitrate": 408181, 
    # "video_width": 1280, 
    # "video_height": 720, 
    # "video_fps": 29.97002997002997, 
    # "audio_channels": null, 
    # "audio_samplerate": null, 
    # "attached_pic": 0, 
    # "sub_forced": null, 
    # "sub_default": null, 
    # "metadata": {
        # "creation_time": "2021-11-22T23:24:24.000000Z", 
        # "language": "eng", 
        # "handler_name": "VideoHandler", 
        # "vendor_id": "[0][0][0][0]"
    #}
#}
