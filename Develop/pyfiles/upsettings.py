import easysettings
import datetime
import random
from pyfiles import NetExcepts as Excepts
import logging
import json
#NOTE: moving away from easysettings config files (pls remember!)
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
        Excepts.GetError(name)
def GetGlobsett(name):
    try:
        logging.debug(Globcfg.get(name))
        print((Globcfg.get(name)))
        return (Globcfg.get(name))
    except Exception:
        Excepts.GetError(name)