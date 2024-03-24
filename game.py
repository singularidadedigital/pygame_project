import pygame
from pygame import display, transform
from pygame.image import load
from pygame.locals import *

# pygame setup
pygame.init()

largura = 480
altura = 320

screen = display.set_mode(size=(largura, altura))
clock = pygame.time.Clock()

dt = 0

# carregar imagem de fundo
background = load('images/nature_5/orig.png')

# Music
pygame.mixer.music.load("assets/EssentialGameAudiopack/FullScores/Orchestral Scores/Ove_Melaa-Heaven_Sings.mp3")
pygame.mixer.music.play(-1)

running = True
if __name__ == "__main__":
    while running:
        # poll for events
        # pygame QUIT event means the user clicked X to close windows
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # RENDER THE GAME
        # Espaco do display
        screen.blit(background, (0, 0))
        display.flip()

        # LIMIT FPS
        dt = clock.tick(60) / 1000

pygame.quit()
