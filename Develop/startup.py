from pyfiles import GlobalFuns as Global
from pyfiles import SoundHandler as Sound
import logging
import os
from pyfiles import debuger as debug
from pyfiles import upsettings as settings
from pyfiles import Generators as Gen
logging.basicConfig(filename='DEBUG.log',level=logging.DEBUG)
logging.info('imports are ok!')
print('---------------------------------')
print('POWERED BY:')
print('PYTHON')
print('OTHER LIBRARIES:')
print('EASYSETTINGS')
print('PYGAME')
print('---------------------------------')
print('starting up upnet...')
Global.startupgame()
Sound.music('Clouds',0.5)
logging.info('os check.')
print(Global.detectOS())
logging.info('connecting to global signup page...')
Gen.IPGen('uplinksignup')
logging.info('generated uplink login system!')