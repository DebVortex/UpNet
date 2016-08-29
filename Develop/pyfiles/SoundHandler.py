# Sound Handler #
# Handles all things related to sounds: Loading,lists loading,playing, etc etc...
import logging
import pygame
import upsettings as settings
import easysettings
import shutil
import os
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

def music(song=None,level='1.0'):
    if song == None:
        RandomiseGet(level)
    else:
        logging.debug('new song init!')
        pygame.mixer.music.load(settings.MusiclistGetSong(song))
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(float(level))
        logging.debug('done!')