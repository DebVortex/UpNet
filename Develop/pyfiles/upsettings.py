import easysettings
import datetime
import random
import NetExcepts as Excepts
import logging
IPcfg = easysettings.EasySettings("Configuration\IPcfg.cfg")
Globcfg = easysettings.EasySettings("Configuration\General.cfg")
Globmusic = easysettings.EasySettings("Configuration\MusicConfig.cfg")
Eggscfg = easysettings.EasySettings("Configuration\eastereggs.cfg")
def IPset(name,IP):
    IPcfg.set(name,IP)
    IPcfg.save()
def OSset(OSnum):
    Globcfg.set('platform',OSnum)
    Globcfg.save()
def Date(Date,Month):
    Globcfg.set('Date',Date)
    Globcfg.set('Month',Month)
    Globcfg.save()
def GetIPSett(name):
    try:
        IPcfg.get(name)
    except Exception:
        logging.warn('unable to get ' + name + ' that is in settings!')
def GetGlobsett(name):
    try:
        logging.debug(Globcfg.get(name))
        print(Globcfg.get(name))
        return (Globcfg.get(name))
    except Exception:
        Excepts.GetError(name)

def MusiclistGetSong(song):
    try:
        logging.debug(song)
        return (Globmusic.get(song))
    except Exception:
        Excepts.SouError(song)
        
def MRandomGet():
    MusiclistRand = Globmusic.list_options()
    return random.choice(MusiclistRand)