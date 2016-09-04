#Module to intepreit all the files in a mod.
#NOTE: resource files are handled json-ly
import os
import sys
import logging
import upsettings
import SoundHandler as sound
import jsoncfg
def resScan():
    print('called?')
    logging.info('starting to scan for all resources.json files...')
    for root, dirs, files in os.walk("\Mods"):
        print(dirs)
        for name in files:
            
            if name == "resources.json":
                resfile = os.path.join(root, name)
                logging.info('Resource file found: ' + resfile)
                rescfg = jsoncfg.load_config(resfile)
                if not soundlist:
                    logging.info('sound list not given skipping...')
                else:
                    logging.info('sound list is given. loading it.')
                    templist = []
                    for x in soundlist:
                        templist.append(x)
                    sound.genAlbowlist(templist)
    logging.info('added all modules.')