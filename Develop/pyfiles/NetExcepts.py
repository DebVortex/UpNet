import logging
import pygame
Version = 'Version number: 0.2'
Feature = 'Sound,Render,Get,NOPE,PrivateException'
#sond errors
def SouError(file):
    logging.fatal("Called a invalid Sound file from master sound file with the name of :"+ file)
#Generation errors (TODO: Diversify it.)
def GenError():
    logging.fatal("Generation of stuff has failed!")
def RenError(name):
    logging.fatal("Rendering has failed! Name: " + name)
def GetError(whatev):
    logging.fatal("Getting the requested thing: " + str(whatev) + " has failed!")
def NOPE():
    logging.fatal("NOPE")
    logging.fatal("http://pruebakr-1.webcindario.com/nope.jpg")
    pygame.quit()
def private():
    logging.fatal("Can't Touch This! It is a private man!")
    logging.fatal('Here is a video for your Efforts ;) > https://youtu.be/otCpCn0l4Wo?t=14s')
def yes():
    count = 0
    while count < 1000000:
        print('Y')
        count += 1
def ModInfo():
    logging.info(Version)
    logging.info(Feature)