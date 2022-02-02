from pathlib import Path
import requests

#scan_dir = '/Users/Jason/Projects/mediamanager'
scan_dir = '/mnt/media/Television/'

target_uri = "http://localhost:8000/ffmpeg/getMediaInfo"

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

def try_loop(g):
    while True:
        try:
            yield next(g)
        except StopIteration:
            break
            #continue
            #pass
        except OSError as e:
            # log error
            continue

for file in try_loop(Path(scan_dir).glob('**/*.*')):
    print(file)
    #extension = str(file.suffix)

    for extension in valid_extensions:
        if str(path.suffix) == extension:
            
            path_in_str = str(path)
            post_data = {"target": path_in_str}
            #response = requests.get(target_uri, data = post_data)
            #print(response.json())

    
