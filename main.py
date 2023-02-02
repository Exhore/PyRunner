import pygame
from sys import exit

pygame.init()
screen    = pygame.display.set_mode((800,400))
pygame.display.set_caption("EdgeRunner")
clock     = pygame.time.Clock()
test_font = pygame.font.Font('font/Cyberfall.otf', 50)


# surfaces
sky_surface     = pygame.image.load('graphics/Sky.png').convert()
ground_surface  = pygame.image.load('graphics/ground.png').convert()
score_surface   = test_font.render("My game", False, 'Black')

#rects
score_rect      = score_surface.get_rect(center = (400,50))

#player
player_surface = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect    = player_surface.get_rect(midbottom = (80,300))

#snail
snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect    = snail_surface.get_rect(bottomright = (600, 300))

# mouse pos
mouse_pos = pygame.mouse.get_pos()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # mouse on player
        # if event.type == pygame.MOUSEMOTION:
        #     if player_rect.collidepoint(event.pos): print('collision')

    #invocar
    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0,300))
    pygame.draw.rect(screen, 'Pink', score_rect)
    screen.blit(score_surface, score_rect)
    screen.blit(player_surface, player_rect)
    screen.blit(snail_surface, snail_rect)
    # snail action
    snail_rect.x -= 3
    if snail_rect.right == -120:
        snail_rect.left = 800



    if player_rect.collidepoint(mouse_pos):
        print(pygame.mouse.get_pressed())



    pygame.display.update()
    clock.tick(60)



