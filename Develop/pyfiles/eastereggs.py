"""
Easter Eggs for the Game
DO NOT OPEN SCROLL IF YOU DO NOT WANT TO BE SPOILED.






















































You sure eh?
"""
import subprocess
import pygame
import os
import datetime
import upsettings as settings
import random
import logging
def Video(name):
    si = subprocess.STARTUPINFO()
    si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    clock = pygame.time.Clock()
    if name == 'win8':
        logging.info('Multitasking')
        subprocess.call('youtube-dl https://www.youtube.com/watch?v=ZVVOzLyt3fo', startupinfo=si)
        subprocess.call('ffmpeg -i "Windows 8 - Multitasking-ZVVOzLyt3fo.webm" -vcodec mpeg1video -acodec libmp3lame -intra "egg.mpg"', startupinfo=si)
        os.remove("Windows 8 - Multitasking-ZVVOzLyt3fo.webm")
    elif name == 'matt':
        logging.info('someone called visa exception... hmm...')
        subprocess.call('youtube-dl https://www.youtube.com/watch?v=TVOsBVDXSzc', startupinfo=si)
        subprocess.call('ffmpeg -i "Visa commercial with Matt Harding-TVOsBVDXSzc.webm" -vcodec mpeg1video -acodec libmp3lame -intra "egg.mpg"', startupinfo=si)
        os.remove("Visa commercial with Matt Harding-TVOsBVDXSzc.webm")
    elif name == 'Brexit':
        subprocess.call('youtube-dl https://www.youtube.com/watch?v=SoxxHeBJmz8', startupinfo=si)
        subprocess.call('ffmpeg -i "If You Wannabe Prime Minister-SoxxHeBJmz8.webm" -vcodec mpeg1video -acodec libmp3lame -intra "egg.mpg"', startupinfo=si)
        os.remove('If You Wannabe Prime Minister-SoxxHeBJmz8.webm')
    pygame.init()
    pygame.mixer.quit()
    logging.info('play start!')
    pygame.display.set_caption('Video easteregg')
    movie = pygame.movie.Movie('egg.mpg')
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