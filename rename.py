import os
import shutil

folders = os.listdir()
for folder in folders:
    name = folder.split('-')
    if len(name) > 1:
        name = name[2].strip()
        name = name.split(' ')
        fname, lname = name[0], name[-1]
        name = lname +' ' + fname
        shutil.move(folder, name)
    