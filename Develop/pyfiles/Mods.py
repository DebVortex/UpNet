#Module to intepreit all the files in a mod.
#NOTE: resource files are handled json-ly
import os
import sys
import logging
import upsettings
import SoundHandler as sound
import jsoncfg
import glob
def resScan():
    logging.info('starting to scan for all resources.json files...')
    for root, dirs, files in os.walk('.\mods'):
        for names in files:
            if names == "resources.json":
                resfile = os.path.join(root, names)
                print(resfile)
                logging.info('Resource file found: ' + resfile)
                rescfg = jsontree.load_config(resfile)
                if not soundlist:
                    logging.info('sound list not given skipping...')
                else:
                    logging.info('sound list is given. loading it.')
                    templist = []
                    for x in soundlist:
                        templist.append(x)
                    sound.genAlbowlist(templist)
    logging.info('added all modules.')