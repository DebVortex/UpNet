import sys
import pygame
import urllib
import logging
import os
import logging
import time
import random
import upsettings as settings
import SoundHandler
import os
import eastereggs
import urllib2
def startupgame():
    eastereggs.startEastereggcheck()
    #placeholder icon. (todo in the future.)
    logging.debug('setting icon..')
    print os.getcwd()
    #pygame.display.set_icon(pygame.image.load('images\icon3.ico'))
    logging.debug('set icon!')
    SoundHandler.StartupHandler()
    logging.debug('get date from system.')
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
'''
check for internet. This only tries to connect to google's DNS.
if you are REALLY paranoid.. there is a config option under General.cfg to disable this.
'''
def internet_on():
    if GetGlobsett(disableinterwebzcheck) == 0:
        try:
            response=urllib2.urlopen('8.8.8.8',timeout=1)
            return True
        except urllib2.URLError as err: pass
            return False
    else:
        logging.info('internet check is disabled.')