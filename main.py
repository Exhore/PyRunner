import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("EdgeRunner")
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Cyberfall.otf', 50)


sky_surface = pygame.image.load('graphics/Sky.png').convert_alpha()
ground_surface = pygame.image.load('graphics/ground.png').convert_alpha()
text_surface = test_font.render("Runner", False, 'Black')

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()

# positions
snail_x_pos = 300
snail_y_pos = 270


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0,300))
    screen.blit(text_surface, (300, 50))
    snail_x_pos -= 1
    if snail_x_pos == -100:
        snail_x_pos = 820
    screen.blit(snail_surface, (snail_x_pos,snail_y_pos))


    pygame.display.update()
    clock.tick(60)



