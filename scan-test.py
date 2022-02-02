import requests
from pathlib import Path

target_uri = "http://localhost:8000/ffmpeg/getMediaInfo"

#scan_dir = '/Users/Jason/Projects/mediamanager'
#scan_dir = '/mnt/media/Movie/Apex (2021)/'
scan_dir = '/mnt/media/Televison/'


valid_extensions = [
    '.mp4',
    '.m4v',
    '.avi',
    '.mpg',
    '.mpeg',
    '.mkv',
    '.wmv',
    '.mov',
    '.divx',
    '.MP4'
]

#recursive scan of all files
pathlist = Path(scan_dir).glob('**/*.*')
for path in pathlist:
    # because path is object not string
    print(path)
    for extension in valid_extensions:
        if str(path.suffix) == extension:
            path_in_str = str(path)
            post_data = {"target": path_in_str}
            response = requests.get(target_uri, data = post_data)
            print(response.json())

