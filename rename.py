import os
import shutil

folders = os.listdir()
for folder in folders:
    name = folder.split('-')
    if len(name) > 1:
        name = name[2].strip()
        fname, lname = name.split(' ')
        name = lname +' ' + fname

        shutil.move(folder, name)
    