"""
Easter Eggs for the Game
DO NOT OPEN SCROLL IF YOU DO NOT WANT TO BE SPOILED.






















































You sure eh?
"""
import youtube_dl
import subprocess
import pygame
import os
import datetime
import upsettings as settings
import random
import logging
#Windows 8 Release date
def startEastereggcheck():
    if Glob.internet_on() == True:
        if settings.GetGlobsett('easteregg') == '1':
            if settings.GetGlobsett('Month') == '10' and settings.GetGlobsett('Date') == '1' :
                Video()
            else:
                pass
        else:
            pass
    else:
        pass
def Video():
    si = subprocess.STARTUPINFO()
    si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    clock = pygame.time.Clock()
    radomise = bool(random.randint(0, 1))
    if radomise == 1:
        logging.info('at-once')
        subprocess.call('youtube-dl https://www.youtube.com/watch?v=ZtRUjP-o24o', startupinfo=si)
        subprocess.call('ffmpeg -i "Windows 8 - Lenka - Everything At Once (TV Spot) _ Microsoft-ZZ2cftjyHys.mp4" -vcodec mpeg1video -acodec libmp3lame -intra "egg.mpg"', startupinfo=si)
    else:
        logging.info('Multitasking')
        subprocess.call('youtube-dl https://www.youtube.com/watch?v=ZVVOzLyt3fo', startupinfo=si)
        subprocess.call('ffmpeg -i "Windows 8 - Multitasking-ZVVOzLyt3fo.mp4" -vcodec mpeg1video -acodec libmp3lame -intra "egg.mpg"', startupinfo=si)
    pygame.init()
    pygame.mixer.quit()
    logging.info('play start!')
    pygame.display.set_caption('Windows 8 Trailer (You found a easter egg!)')
    movie = pygame.movie.Movie('egg.mpg')
    try:
        os.remove("Windows 8 - Lenka - Everything At Once (TV Spot) _ Microsoft-ZZ2cftjyHys.mp4")
    except Exception:
        os.remove("Windows 8 - Multitasking-ZVVOzLyt3fo.mp4")
    screen = pygame.display.set_mode(movie.get_size())
    movie_screen = pygame.Surface(movie.get_size()).convert()
    movie.set_display(movie_screen)
    movie.play()
    FPS = 60
    playing = True
    while movie.get_busy():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break
        screen.blit(movie_screen,(0,0))
        pygame.display.update()
        clock.tick(FPS)
    os.remove('egg.mpg')
def CCN83Secs():
    si = subprocess.STARTUPINFO()
    si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    clock = pygame.time.Clock()
    subprocess.call('youtube-dl https://www.youtube.com/watch?v=B11kASPfYxY', startupinfo=si)
    subprocess.call('ffmpeg -i "The History of Climate Change Negotiations in 83 seconds-B11kASPfYxY.mkv" -vcodec mpeg1video -acodec libmp3lame -intra "egg.mpg"', startupinfo=si)
    pygame.init()
    pygame.mixer.quit()
    pygame.display.set_caption('The History of Climate Change Negotiations in 83 seconds.')
    movie = pygame.movie.Movie('egg.mpg')
    os.remove("The History of Climate Change Negotiations in 83 seconds-B11kASPfYxY.mkv")
    screen = pygame.display.set_mode(movie.get_size())
    movie_screen = pygame.Surface(movie.get_size()).convert()
    movie.set_display(movie_screen)
    movie.play()
    FPS = 60
    playing = True
    while movie.get_busy():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break
        screen.blit(movie_screen,(0,0))
        pygame.display.update()
        clock.tick(FPS)
    os.remove('egg.mpg')
Win8Rec()