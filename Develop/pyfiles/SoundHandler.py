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
def quemusic(self,song):
    logging.debug('que new song!')
    pygame.mixer.music.queue(song)
    logging.debug('done!')
#it finally works! (30/4/2015)
#musiclist: adds music from a addon music list to the master.
def musiclist(Configfile):
    logging.debug('-------------------')
    logging.debug('adding Sound Config Info.')
    ToAdd = open(Configfile, "r")
    copy = open('Configuration\MusicConfig.cfg', "a")
    logging.debug('writing...')
    copy.write("\n")
    for line in ToAdd:
        copy.write(line)
    ToAdd.close()
    copy.close()
    logging.debug('Done!')
    logging.debug('-------------------')
# Randomisation of music to play.
def RandomiseGet(level):
    music(settings.MRandomGet(),level)
def Soundplay(sound):
    Sound = pygame.mixer.Sound(sound)
    Sound.play()
# Buttons..and all the noises that make upnet exciting
def ButtonNo(No):
    int(no)
    if no == 0:
        Soundplay('sounds/effects/buttons/0.wav')
    elif no == 1:
        Soundplay('sounds/effects/buttons/1.wav')
    elif no == 2:
        Soundplay('sounds/effects/buttons/2.wav')
    elif no == 3:
        Soundplay('sounds/effects/buttons/3.wav')
    elif no == 4:
        Soundplay('sounds/effects/buttons/4.wav')
    elif no == 5:
        Soundplay('sounds/effects/buttons/5.wav')
def 