#Module to intepreit all the files in a mod.
#NOTE: resource files are handled json-ly
import os
import sys
import logging
from . import upsettings
from . import SoundHandler as sound
import json_config
import glob
Modstempglob = []
def resScan():
    logging.info('starting to scan for all resources.json files...')
    for root, dirs, files in os.walk('.\mods'):
        for names in files:
            if names == "resources.json":
                root = root
                print(root)
                resfile = os.path.join(root, names)
                Prasingres(resfile)
                logging.info('pushing job over to def...')
                sound.genAlbowlist(root,templist)
    logging.info('added all modules.')
def Prasingres(root,file):
    logging.info('got a job for me?')
    config = json_config.connect(file)
    if not (config["MusicFiles"]):
        logging.info('sound list not given skipping...')
    else:
        logging.info('sound list is given. loading it.')
        templist = []
        for x in config["MusicFiles"]:
            Modstempglob.append(root + x)
            logging.info('adding :' + root + x)