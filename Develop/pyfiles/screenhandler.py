import logging
import pygame
clock = pygame.time.Clock()


def fill(colour):
    logging.debug('Fill called! with ' + colour + ' as given.')
    while True:
        pygame.Surface.Fill(colour)
        clock.tick(60)
        pygame.display.flip()
    logging.fatal('definition has been stopped. This should not be happening.')


def Sprite():
    logging.debug('Sprite Draw Called!')


def addtext(text, locx, locy, size):
    font = pygame.font.SysFont("Dungeon", size)
    text2 = font.render(text, True, (0, 0, 0))
    screen.blit(text2, (locx, locy))
    logging.debug('textblit.')


def Video(Movie):
    logging.info('Movie module called. need to close pygame music streams.')
    try:
        pygame.mixer.quit()
    except Exception:
        pass  # ? What does this try do?
    clock = pygame.time.Clock()
    pygame.init()
    pygame.mixer.quit()
    logging.info('play start!')
    pygame.display.set_caption('Video')
    movie = pygame.movie.Movie(Movie)
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
        screen.blit(movie_screen, (0, 0))
        pygame.display.update()
        clock.tick(FPS)


def Icon(Loc):
    logging.info('Icon called,setting icon of screen.')
    pygame.display.set_icon(Pygame.image.load(Loc))


def createobject(icon, x, y):
    try:
        iconload = pygame.image.load(icon)
    except Exception:
        logging.error('create object was given a invalid extension that pygame cannot load!')
    pygame.screen.blit(iconload, (x, y))
    pygame.display.update()
    logging.info('successfuly created object!')
