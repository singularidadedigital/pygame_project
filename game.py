from pygame import display, transform
from pygame.image import load

largura = 480
altura = 320

screen = display.set_mode(
    size=(largura, altura),
    flags=0,
    depth=0,
    display=0,
    vsync=0
)

# carregar imagem de fundo
background = load('images/nature_5/orig.png')

while True:
    # Espaco do display
    screen.blit(
        background,
        (0, 0)
    )
    display.update()

display.set_caption('Pygame Project')

