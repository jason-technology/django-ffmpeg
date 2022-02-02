from pathlib import Path

#scan_dir = '/Users/Jason/Projects/mediamanager'
scan_dir = '/mnt/media/Television/'

extensions = []

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
    extension = str(file.suffix)
    if extension not in extensions:
        extensions.append(extension)
        

for extension in extensions:
    print(extension)


#recursive scan of all files
#pathlist = Path(scan_dir).glob('**/*.*')
#for path in pathlist:
    # because path is object not string
#    print(path)
    #extension = str(path.suffix)
    #if extension not in extensions:
    #    extensions.append(extension)
        

#for extension in extensions:
#    print(extension)
    
