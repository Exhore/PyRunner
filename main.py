import pygame
from sys import exit


def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surface = test_font.render(f'Score: {current_time}', False, (64,64,64))
    score_rect = score_surface.get_rect(center = (400,50))
    screen.blit(score_surface, score_rect)
    print(current_time)


pygame.init()
screen    = pygame.display.set_mode((800,400))
pygame.display.set_caption("EdgeRunner")
clock     = pygame.time.Clock()
test_font = pygame.font.Font('font/Cyberfall.otf', 50)

#start time
start_time = 0

# ground
sky_surface     = pygame.image.load('graphics/Sky.png').convert()
ground_surface  = pygame.image.load('graphics/ground.png').convert()

# score
# score_surface   = test_font.render("My game", False, (64,64,64))
# score_rect      = score_surface.get_rect(center = (400,50))


# positions for reset
player_pos = (80,300)
snail_pos  = (600,300)

# player
player_surface = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect    = player_surface.get_rect(midbottom = player_pos)
player_gravity = 0
# snail
snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect    = snail_surface.get_rect(midbottom = snail_pos)

# keys
keys = pygame.key.get_pressed()


#game active

game_active = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # if event.type == pygame.MOUSEBUTTONUP:
        #     print("MOUSE UP")
        # if event.type == pygame.MOUSEMOTION:
        #     print(event.pos)
        # if event.type == pygame.KEYDOWN:
        #     print('key down')
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom == 300:
                    player_gravity = -20


            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos):
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                snail_rect.left = 800
                game_active = True
                start_time = int(pygame.time.get_ticks() / 1000)

        # if event.type == pygame.MOUSEMOTION:
        #     if player_rect.collidepoint(event.pos):
        #         print("collision")
    if game_active:
        #invocar
        screen.blit(sky_surface, (0,0))
        screen.blit(ground_surface, (0,300))
        # pygame.draw.rect(screen, '#c0e8ec', score_rect)
        # screen.blit(score_surface, score_rect)
        screen.blit(player_surface, player_rect)
        screen.blit(snail_surface, snail_rect)
        
        display_score()
        
        #draw a line
        #pygame.draw.line(screen, 'black', (0, 0), (800,400))
        # snail action
        snail_rect.x -= 3
        if snail_rect.right == -120:
            snail_rect.left = 800

        # mouse pos
        mouse_pos = pygame.mouse.get_pos()

        #player gravity
        player_gravity += 1
        player_rect.y += player_gravity

        #fit to ground
        if player_rect.bottom >= 300:
            player_rect.bottom = 300



        #snail kill-collide-
        if snail_rect.colliderect(player_rect):
            game_active = False
    else:
        screen.fill('Black')



    pygame.display.update()
    clock.tick(60)



