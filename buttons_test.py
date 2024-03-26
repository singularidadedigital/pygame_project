import pygame

# create display window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Button Demonstration")

# load button images
start_image = pygame.image.load('images/start_btn.png.png').convert_alpha()
options_image = pygame.image.load('images/option_btn.png').convert_alpha()


# button class
class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), (int(height * scale))))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self):
        # draw button on screen
        screen.blit(self.image, (self.rect.x, self.rect.y))


# create button instances
start_button = Button(450, 200, start_image, 0.15)
options_button = Button(450, 280, options_image, 0.15)

# game loop
run = True
while run:

    screen.fill((202, 228, 241))

    start_button.draw()
    options_button.draw()

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
