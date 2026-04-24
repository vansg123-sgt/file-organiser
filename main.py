import os
import shutil

path = input("Enter folder path: ")

folders = {
    "Images": [".jpg", ".png"],
    "Docs": [".pdf", ".txt"],
    "Videos": [".mp4", ".mkv"]
}

for file in os.listdir(path):
    fpath = os.path.join(path, file)
    if os.path.isfile(fpath):
        for folder, exts in folders.items():
            if file.endswith(tuple(exts)):
                dest = os.path.join(path, folder)
                os.makedirs(dest, exist_ok=True)
                shutil.move(fpath, os.path.join(dest, file))
