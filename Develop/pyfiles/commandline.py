#main menu
from . import GlobalFuns as Global
from . import SoundHandler as Sound
import logging
import os
import sys
import time
from . import upsettings as settings
from . import Generators as Gen


def mainmenu():
    printf('1. New User')
    print('')
    printf('2. Returning User')
    print('')
    printf('3. Retire')
    print('')
    printf('4. Exit')
    print('')
    selection = eval(input('Input >:'))
    selection = int(selection)
    print(selection)
    if selection == 1:
        Newgame()
    elif selection == 3:
        sys.exit('Err code : 0')
    elif selection == 2:
        LoadGame()


#New game
def Newgame():
    print('Please select your personal playstyle:')
    print('1 : Uplink Playstyle(Gateway to Upnet servers)')
    print('2 : No Gateway (Hacknet Experience)')
    Newgamesel = input('Input >:')
    if Newgamesel == 1:
        Uplink()
    elif Newgamesel == 2:
        printf('narp! not done yet :)')


def Uplink():
    printf('Connectiong to uplink access server...', '0.1')
    Gen.IPGen('uplink')
    printf(settings.GetIPSett('uplink'))


# Text utils
def printf(text, timeperlett='None'):
    if timeperlett == 'None':
        timeperlett = '0.02'
        timeperlett = float(timeperlett)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(timeperlett)


# play sounds in text.(same as above but with number sounds.)
def PSIT(text):
    listtext = text.list()
    for x in listtext:
        print(x)
        if x == '1':
            Sound.play(Global.corefile + '\buttons\1.wav')
        elif x == '2':
            Sound.play(Global.corefile + '\buttons\2.wav')
        elif x == '3':
            Sound.play(Global.corefile + '\buttons\3.wav')
        elif x == '4':
            Sound.play(Global.corefile + '\buttons\4.wav')
        elif x == '5':
            Sound.play(Global.corefile + '\buttons\5.wav')
        elif x == '6':
            Sound.play(Global.corefile + '\buttons\6.wav')
        elif x == '7':
            Sound.play(Global.corefile + '\buttons\7.wav')
        elif x == '8':
            Sound.play(Global.corefile + '\buttons\8.wav')
        elif x == '9':
            Sound.play(Global.corefile + '\buttons\9.wav')
        elif x == '0':
            Sound.play(Global.corefile + '\buttons\0.wav')
