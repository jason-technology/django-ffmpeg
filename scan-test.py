import requests
from pathlib import Path

target_uri = "http://192.168.0.99:8000/ffmpeg/getMediaInfo"

#scan_dir = '/Users/Jason/Projects/mediamanager'
#scan_dir = '/mnt/media/Movie/Apex (2021)/'
scan_dir = '/mnt/media/Movie/Return of the Living Dead- Rave to the Grave (2005)'


valid_extensions = [
    '.mp4',
    '.m4v',
    '.avi',
    '.mpg',
    '.mpeg',
    '.mkv'
]

#recursive scan of all files
pathlist = Path(scan_dir).glob('**/*.*')
for path in pathlist:
    # because path is object not string
    
    for extension in valid_extensions:
        if str(path.suffix) == extension:
            path_in_str = str(path)
            post_data = {"target": path_in_str}
            response = requests.get(target_uri, data = post_data)
            print(response.json())

#for target in scan_targets:

    #post_data = {
    #    "target": target
    #}

    #response = requests.get(target_uri, data = post_data)

    #print(response.json())

