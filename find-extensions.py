from pathlib import Path

#scan_dir = '/Users/Jason/Projects/mediamanager'
scan_dir = '/mnt/media/Movie/'

extensions = []

#recursive scan of all files
pathlist = Path(scan_dir).glob('**/*.*')
for path in pathlist:
    # because path is object not string
    extension = str(path.suffix)
    if extension not in extensions:
        extensions.append(extension)
        

for extension in extensions:
    print(extension)
    
