from __future__ import absolute_import
from pyfiles import GlobalFuns, SoundHandler, upsettings, Generators, commandline
import logging
import os
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

GlobalFuns.startupgame()
SoundHandler.music('Clouds', 0.5)
logging.info('os check.')
print(GlobalFuns.detectOS())
logging.info('connecting to global signup page...')
Generators.IPGen('uplinksignup')
logging.info('generated uplink login system!')
