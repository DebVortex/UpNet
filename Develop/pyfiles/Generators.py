#Houses the :
#Plot generator(TODO)
#Mission Generator
#Name Generator
#News Generator
#Records Generator
#World Generator
from __future__ import absolute_import
import random
import logging
import pygame
from . import upsettings as settings
from . import GlobalFuns as Global
from . import NetExcepts as EN
import linereader
import faker


#TODO:rewrite classes
class WorldGen:
    def GenAll():
        log.info('Starting GenAll run!')


class NewsGen:
    def __init__(self, name, IP=''):
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
def IPGen(name, IP=None):
    if IP is None:
        settings.IPset(name, (fake.ipv4()))
    elif IP is not None:
        settings.IPset(name, IP)
    else:
        EN.GenError()


#passwords (i guess it is considered under generators? :P)
def passwordcreate(name):
    Schars = None
    Digits = None
    Upcase = None
    LoCase = None
    if bool(secrets.randbelow(1)) == True:
        Schars = True
    else:
        Schars = False
    if bool(secrets.randbelow(1)) == True:
        Digits = True
    else:
        Digits = False
    if bool(secrets.randbelow(1)) == True:
        Upcase = True
    else:
        Upcase = False
    if bool(secrets.randbelow(1)) == True:
        LoCase = True
    else:
        LoCase = False
    
    length = secrets.randbelow(10)
    print(fake.password(length,Schars, Digits, Upcase, LoCase))
    return fake.password(length, Schars, Digits, Upcase, LoCase)
    
def StaticIP():
    IPGen('Introversionsoftware','50.19.100.182')
