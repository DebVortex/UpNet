#main menu
import GlobalFuns as Global
import SoundHandler as Sound
import logging, os, sys, time
import debuger as debug
import upsettings as settings
import Generators as Gen
import sys
def mainmenu():
    print('1. New Game')
    print('2. Load Saved Game')
    print('3. Exit')
    selection = raw_input('Input >:')
    if selection == ['1','one','One']:
        Newgame()
    elif selection == ['3']:
        sys.exit('Err code : 0')
    elif selection == ['2']:
        LoadGame()
#New game
def Newgame():
    print('Please select your personal playstyle:')
    print('1 : Uplink Playstyle(Gateway to Upnet servers)')
    print('2 : No Gateway (Hacknet Experience)')
    selection = raw_input('Input >:')
    if selection == ['1']:
        Uplink()
    elif selection == ['2']:
        Hacknet()
def Uplink():
    printf('Connectiong to uplink access server...','0.1')
    Gen.IPGen('uplink')
    printf(settings.GetIPSett('uplink'))
# Text utils
def printf(text,timeperlett):
    listtext = text.list()
    for x in listtext:
        print(x,end='')
        time.sleep(timeperlett)
# play sounds in text.(same as above but with number sounds.)
def PSIT(text)
    listtext = text.list()
    for x in listtext:
        print(x,end='')
        if x == '1':
            Sound.play('1')
        elif x == '2':
            Sound.play('2')
        elif x == '3':
            Sound.play('3')
        elif x == '4':
            Sound.play('4')
        elif x == '5':
            Sound.play('5')
        elif x == '6':
            Sound.play('6')
        elif x == '7':
            Sound.play('7')
        elif x == '8':
            Sound.play('8')
        elif x == '9':
            Sound.play('9')
        elif x == '0':
            Sound.play('0')
        time.sleep(timeperlett)