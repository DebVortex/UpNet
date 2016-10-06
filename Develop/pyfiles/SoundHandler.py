# Sound Handler #
# Handles all things related to sounds: Loading,lists loading,playing, etc etc...
#Workaround for python 3.5 nuisences
import logging
import pygame
from pyfiles import upsettings as settings
from pyfiles import NetExcepts as Excepts
import easysettings
import shutil
import os
from pyfiles import albow

#Generic sound stuff.
def StartupHandler():
    logging.debug('Starting up Music module')
    if pygame.mixer.get_init():
        logging.debug('mixer get init returns true. not starting it up again.')
        pass
    else:
        logging.debug('mixer not started. Starting it up.')
        pygame.mixer.init(48000)
        logging.debug('done!')

def genAlbowlist(resfile):
    """
    FOR MODDERS: DO NOT CALL THIS DIRECTLY
    game will call this when loading resource files!
    """
    logging.debug('New Albow list called!')
    if resfile == []:
        logging.error('List is invalid! refusing to load.')
    else:
        albow.Playlist(resfile,True,True)
    logging.debug('Albowlist added!')