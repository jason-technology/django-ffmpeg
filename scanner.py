from pathlib import Path
import requests

#scan_dir = '/Users/Jason/Projects/mediamanager'
#scan_dir = '/mnt/media/Movie/'
scan_dir = '/mnt/media/Movie/Return of the Living Dead- Rave to the Grave (2005)/'

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
        except Exception as e:
            print(e)
            continue
        #except OSError as e:
        #    # log error
        #    continue
        #except IOError as e:
        #    # log error
        #    continue

for file in try_loop(Path(scan_dir).glob('**/*.*')):

    for extension in valid_extensions:
        if str(file.suffix) == extension:
            print(file)
            filePath = str(file)
            post_data = {"target": filePath}
            
            response = requests.get(target_uri, data = post_data)
            
            try:   
                print(response.json())
            except:
                continue
    



