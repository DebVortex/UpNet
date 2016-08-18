#Houses the :
#Plot generator(TODO)
#Mission Generator
#Name Generator
#News Generator
#Records Generator
#World Generator
import random
import logging
import pygame
import upsettings as settings
import GlobalFuns as Global
import NetExcepts as EN
import linereader
#TODO:rewrite classes
class WorldGen:
    def GenAll():
        log.info('Starting GenAll run!')
class NewsGen:
    def __init__(self,name,IP = ''):
        self.computer = name
        self.IP = IP
    def _CompCheck(Computer):
        if Comp == ISSD:
            return ('SocialDB')
        elif Comp == IAD:
            return ('AcadDB')
        elif Comp == GCD:
            return ('CrimeDB')
#IPgen now works. leaving it as of now...
def IPGen(name,IP=None):
    if IP==None:
        logging.debug('startgen!')
        not_valid = [10,127,169,172,192]
        first = random.randrange(1,256)
        while first in not_valid:
            first = random.randrange(1,256)
        ip = ".".join([str(first),str(random.randrange(1,256)),
        str(random.randrange(1,256)),str(random.randrange(1,256))])
        settings.IPset(name,ip)
        logging.debug('done!')
        return(ip)
    elif IP is not None:
        settings.IPset(name,IP)
    else:
        EN.GenError()
#passwords (i guess it is considered under generators? :P)
def passwordget(name):
    passwords = linereader.dopen(name)
    nolines = name.count('\n')
    logging.info('the number of lines in this files is :' + nolines)
    return file.getline(random.randint(1,nolines)
def StaticIP():
    IPGen('Introversionsoftware','50.19.100.182')   