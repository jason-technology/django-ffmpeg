from converter import Converter
import json, os, subprocess
from datetime import datetime


def SerializeMediaInfo(inFile):
    
    now = datetime.now()
    
    fileName = os.path.basename(inFile)
    filePath = os.path.dirname(inFile)
    c = Converter()
    #inFile = '/Users/Jason/Projects/mediamanager/1_min_later.m4v'
    mediaInfo = c.probe(inFile)
    
    myProcess = subprocess.check_output(['md5','-q', '-s', str(mediaInfo)], encoding='utf8', text=True)
    fileFingerprint = myProcess.replace("\n","")
    
    serializedMediaInfo = {
        "audio_codec": mediaInfo.__dict__["streams"][0].__dict__["codec"],
        "audio_bitrate": int(mediaInfo.__dict__["streams"][0].__dict__["bitrate"]),
        "audio_samplerate": int(mediaInfo.__dict__["streams"][0].__dict__["audio_samplerate"]),
        "video_codec": mediaInfo.__dict__["streams"][1].__dict__["codec"],
        "video_bitrate": int(mediaInfo.__dict__["streams"][1].__dict__["bitrate"]),
        "video_fps": int(mediaInfo.__dict__["streams"][1].__dict__["video_fps"]),
        "filename": fileName,
        "filepath": filePath,
        "minutes": int(mediaInfo.__dict__["format"].__dict__["duration"]),
        "size": int(mediaInfo.__dict__["format"].__dict__["size"]),
        "bitrate": int(mediaInfo.__dict__["format"].__dict__["bitrate"]),
        "fingerprint": fileFingerprint,
        #"lastscan": str(now)
    }
    
    
    #return json.dumps(serializedMediaInfo)
    return serializedMediaInfo



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
