import logging
import pygame
import GlobalFuns as Global
import upsettings as settings
import NetExcepts as Excepts
debug = settings.GetGlobsett('debug')
if debug==1:
    logging.debug('--------------DEBUG INFO--------------')
    logging.debug('Detected OS:' + Global.detectOS())
    logging.debug("driver used :" + pygame.display.get_driver())
    logging.debug('--------------Netexcerpts--------------')
    print(Excepts.Version)
    print(NetExcepts.Feature)
    logging.debug('---------------------------------------')