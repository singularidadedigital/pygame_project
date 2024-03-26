import sys

import pygame
from pygame import display, transform
from pygame.image import load
from pygame.locals import *

# pygame setup
pygame.init()

WIDTH = 500
HEIGHT = 320

screen = display.set_mode(size=(WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)
dt = 0

# carregar imagem de fundo
background = load('images/nature_5/orig.png')

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

        # text menu
        draw_text('Nova Genesis', font, (255, 255, 255), screen, 455, 20)

        mx, my = pygame.mouse.get_pos()

        # Button 1
        button_1 = pygame.Rect(50, 100, 200, 50)
        button_2 = pygame.Rect(50, 200, 200, 50)

        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                options()

        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)

        click = False

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
        draw_text('Nova Genesis', font, (255, 255, 255), screen, 200, 20)
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
