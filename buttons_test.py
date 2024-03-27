# import pygame
# import buttons
#
# # create display window
# SCREEN_WIDTH = 800
# SCREEN_HEIGHT = 500
#
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#
#
# pygame.display.set_caption("Button Demonstration")
#
# # load button images
# start_image = pygame.image.load('images/start_btn.png.png').convert_alpha()
# options_image = pygame.image.load('images/option_btn.png').convert_alpha()
#
# # create button instances
# start_button = buttons.Button(550, 200, start_image, 0.15)
# options_button = buttons.Button(550, 280, options_image, 0.15)
#
# # game loop
# run = True
# while run:
#
#     screen.fill((202, 228, 241))
#
#     if start_button.draw(screen):
#         print('START')
#         # run = False
#
#     if options_button.draw(screen):
#         print('OPTIONS')
#
#     # event handler
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#
#     pygame.display.update()
#
# pygame.quit()
