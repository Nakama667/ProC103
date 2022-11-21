import sys
import time
import random

import os
import shutil
import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/preet/Downloads"

class FileEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f"Olá, {event.src_path} craftado!")

    def on_deleted(self, event):
        print(f"Eita nois, deletaram {event.src_path}!")

    def on_modified(self, event):
        print(f"ih, {event.src_path} foi modificado")
    
    def on_moved(self, event):
        print(f"mexeram o {event.src_path} la pro {event.dest_path}")
        

event_handler = FileEventHandler()

observer = Observer()

observer.schedule(event_handler, from_dir, recursive=True)

observer.start()

try:
    while True:
        time.sleep(2)
        print("tururururururu ruruuuuuu")
except KeyboardInterrupt:
    print("PC da positivo")
    observer.stop()

