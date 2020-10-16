import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import json

def types (extension):
        return {
            '.jpg' : 'Images',
            '.jpx' : 'Images',
            '.png' : 'Images',
            '.gif' : 'Images',
            '.webp' : 'Images',
            '.cr2' : 'Images',
            '.tif' : 'Images',
            '.bmp' : 'Images',
            '.jxr' : 'Images',
            '.psd' : 'Images',
            '.ico' : 'Images',
            '.heic' : 'Images',
            '.mp4' : 'Videos',
            '.m4c' : 'Videos',
            '.mkv' : 'Videos',
            '.webm' : 'Videos',
            '.mov' : 'Videos',
            '.avi' : 'Videos',
            '.wmv' : 'Videos',
            '.mpg' : 'Videos',
            '.flv' : 'Videos',
            '.mid' : 'Audios',
            '.mp3' : 'Audios',
            '.m4a' : 'Audios',
            '.ogg' : 'Audios',
            '.flac' : 'Audios',
            '.wav' : 'Audios',
            '.amr' : 'Audios',
            '.epub' : 'Compressed',
            '.zip' : 'Compressed',
            '.tar' : 'Compressed',
            '.rar' : 'Compressed',
            '.gz' : 'Compressed',
            '.bz2' : 'Compressed',
            '.7z' : 'Compressed',
            '.pdf' : 'Documents',
            '.doc' : 'Documents',
            '.docx' : 'Documents',
            '.txt' : 'Documents',
            '.exe' : 'Applications',
            '.torrent' : 'Torrents',
            '.svg' : 'Vectors'
        }.get(extension, 'Others')

class MyHandler(FileSystemEventHandler):
    i = 1

    def on_modified(self, event):
            for name in os.listdir(folder_to_track):
                extension = os.path.splitext(name)[1]
                func = types (extension)
                if not func == 'Others':
                    src = folder_to_track + "\\" + name
                    new_destination = folder_to_track + "\\" +func
                    if not os.path.exists(new_destination):
                        os.makedirs(new_destination)
                    new_destination = new_destination + "\\" + name
                    if not os.path.exists(new_destination):
                        for retry in range(100):
                            try:
                                os.rename(src, new_destination)
                                break
                            except:
                                pass



folder_to_track = 'C:\\Users\\Umer\\Downloads'


event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive = True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
    observer.join()
