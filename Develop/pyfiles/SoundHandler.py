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
    logging.debug('Music Handler called for flicking on the lights.')
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
def queue(self,song):
    logging.debug('que new song!')
    pygame.mixer.music.queue(song)
    logging.debug('done!')
#it finally works! (30/4/2015)
#musiclist: adds music from a list to the master list.
def list(whatev):
    logging.debug('openmusiccfg')
    copy = open('Configuration\MusicConfig.cfg', "a")
    logging.debug('write')
    copy.write("\n")
    copy.write(whatev)
    ToAdd.close()
    copy.close()
    logging.debug('Done')
    logging.debug('-------------------')
# Randomisation of music to play.
def Randomise(level):
    music(settings.MRandomGet(),level)
def play(sound):
    Sound = pygame.mixer.Sound(sound)
    Sound.play()