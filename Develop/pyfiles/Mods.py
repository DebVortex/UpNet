#Module to intepreit all the files in a mod.
#NOTE: resource files are handled json-ly
import os
import sys
import logging
import upsettings
import SoundHandler as sound
import jsoncfg
def InfoScan():
    logging.info('starting to scan for all resources.json files...')
    for root, dir, files in os.walk("/Mods"):
        for name in files:
            if name == "resources.json":
                logging.info('Resource file found: ' + os.path.join(root, name))
                if not soundlist:
                    logging.info('sound list not given skipping...')
                else:
                    logging.info('sound list is given. loading it.')
                    for x in soundlist:
                        sound.list(x)
                    logging.info('added all modules.')
                    
def 