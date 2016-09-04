#system/python
import sys
import os
import urllib
import logging
import time
import random
#pygame
import pygame
#other pyfiles
import upsettings as settings
import SoundHandler as sound
import urllib2
import requests
import commandline
import Mods
def startupgame():
    detectOS()
    sound.StartupHandler()
    print('loading all Mods...')
    Mods.resScan()
    print('Finished loading!')
    commandline.mainmenu()
    logging.info('Init Complete')
    
# os detection
def detectOS():
    if sys.platform == "win32":
        logging.info('Stock Windows Installed.')
        settings.OSset('1')
        return('Windows')
    elif sys.platform == "cygwin":
        logging.info('Cygwin Installed.')
        settings.OSset('2')
        return('cygwin')
    elif sys.platform == "linux2":
        logging.info('Linux Kernels detected.')
        settings.OSset('3')
        return(linux)
    elif sys.platform == "darwin":
        logging.info('Mac OS.')
        settings.OSset('3')
        return('Mac OS X')
    else:
        logging.info('This OS is probably outdated or is not detected.')
        settings.OSset('4')
        return('unknown!')

def Spam(Spam):
    if Spam == 'True':
        try: 
            spamtext = open('spam.txt','r')
        except Exception:
            spamtext = open('pyfiles\spam.txt','r')
        for line in spamtext:
            logging.info(line)
        spamtext.close()
        logging.info('sorry :(')
    else:
        pass