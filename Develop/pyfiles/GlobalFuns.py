#system
import sys
import os
#pygame
import pygame
#other pyfiles
import urllib
import logging
import time
import random
import upsettings as settings
import SoundHandler
import os
import urllib2
import requests
from tqdm import tqdm
def startupgame():
    eastereggs.startEastereggcheck()
    detectOS()
    #placeholder icon. (todo in the future.)
    logging.debug('setting icon..')
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
if you are REALLY paranoid... there is a config option under General.cfg to disable this.
'''
def internet_on():
    if settings.GetGlobsett('disableinterwebzcheck') == 0:
        try:
            response=urllib2.urlopen('8.8.8.8',timeout=1)
            return True
        except urllib2.URLError as err:
            return False
    else:
        logging.info('internet check is disabled.(This is Normal Most of the time if you manually disable it.)')
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
def DownloadItem(url,name,Size):
    if settings.GetGlobsett('disableinterwebzcheck') == '0':
        print('The size of this file is:' + Size)
        if Size > 100:
            print('This file is quite large and may take a long time on a bad internet.')
        urllib.urlretrieve (url, name)
        print('Done!')
    else:
        logging.info('Connection to internet is currently turned off. please enable it for downloading.')