import logging
import pygame
clock = pygame.time.Clock()
def fill(colour):
    logging.debug('Fill called! with ' + colour + ' as given.')
    while True:
        pygame.Surface.Fill(colour)
        clock.tick(60)
        pygame.display.flip()
    logging.fatal('defenition has been stopped. This should not be happening.')
def Sprite():
    logging.debug('Sprite Draw Called!')
def addtext(text,locx,locy,size):
    font = pygame.font.SysFont("Dungeon", size)
    text2 = font.render(text, True, (0, 0, 0))
    screen.blit(text2,(locx,locy)
    logging.debug('textblit.')
def video(Movie):
    logging.info('Movie module called. need to close pygame music streams.')
    try:
        pygmae.mixer.quit
    except Exception:
        pass