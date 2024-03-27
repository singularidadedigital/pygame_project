import sys

import pygame
from pygame import display, transform
from pygame.image import load
from pygame.locals import *

# pygame setup
import buttons

pygame.init()

WIDTH = 800
HEIGHT = 500

screen = display.set_mode(size=(WIDTH, HEIGHT))

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)
dt = 0
pygame.display.set_caption("Nova Genesis - A Rodrigo Luciano Costa New Game")
scale = 2

# carregar imagem de fundo
background = load('images/nature_5/orig.png')
background = pygame.transform.scale(background, (int(800), (int(500))))
# Music
pygame.mixer.music.load("assets/EssentialGameAudiopack/FullScores/Orchestral Scores/Ove_Melaa-Heaven_Sings.mp3")
pygame.mixer.music.play(-1)
running = True


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topright = (x, y)
    surface.blit(textobj, textrect)

click = False

def main_menu():
    while True:

        # poll for events
        # pygame QUIT event means the user clicked X to close windows
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        # RENDER THE GAME
        # Espaco do display
        screen.blit(background, (0, 0))

        # text menu
        draw_text('Nova Genesis', font, (255, 255, 255), screen, 230, 70)

        # load button images
        start_image = pygame.image.load('images/start_btn.png.png').convert_alpha()
        options_image = pygame.image.load('images/option_btn.png').convert_alpha()


        # create button instances
        start_button = buttons.Button(650, 50, start_image, 0.20)
        options_button = buttons.Button(650, 150, options_image, 0.20)

        if start_button.draw(screen):
            print('START')
            # run = False

        if options_button.draw(screen):
            print('OPTIONS')


        pygame.display.update()

        # LIMIT FPS
        clock.tick(60) / 1000


def game():
    running = True
    while running:
        draw_text('game start', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        pygame.display.update()
        clock.tick(60) / 1000


def options():
    running = True
    while running:
        draw_text('game start', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        pygame.display.update()
        clock.tick(60) / 1000


# if "__name__" == "__main__":
main_menu()
