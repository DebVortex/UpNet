import os
import sys
folder = raw_input('Full Mod Folder >:')
for root,dirs,files in os.walk(folder):
    newroot = root.replace(folder,'')
    for name in dirs:
        new = os.path.join(newroot,name)
        print(new)
        