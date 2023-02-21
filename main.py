import pygame
from sys import exit


def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surface = texto_pequeno.render(f'SCORE: {score}', False, "gold")
    score_rect = score_surface.get_rect(center=(700,30))
    screen.blit(score_surface, score_rect)
    return current_time

pygame.init()
# window res
screen = pygame.display.set_mode((800, 400))
#title of game
pygame.display.set_caption("EdgeRunner")
clock = pygame.time.Clock()

#text assign
texto_grande = pygame.font.Font('font/Cyberfall.otf', 50)
texto_mediano = pygame.font.Font('font/Cyberfall.otf', 20)
texto_pequeno = pygame.font.Font('font/Cyberfall.otf', 17)

# score init
score = 0


# start time
start_time = 0

# ground
sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()


# positions for reset
player_pos = (80, 300)
snail_pos = (600, 300)

# player
player_surface = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom=player_pos)
player_gravity = 0


# intro screen
player_stand = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
# 2x o rotozoom, rotozoom es el mejor, y puedo rotar donde el 0
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center=(400, 200))

#game name
game_name = texto_grande.render('EdgeRunner', False, (111, 196, 169))
game_name_rect = game_name.get_rect(center=(400, 60))

#game message
game_message = texto_mediano.render('Press SPACE to run', False, (111,196,169))
game_message_rect = game_message.get_rect(center=(400,350))

# snail
snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom=snail_pos)

# keys
keys = pygame.key.get_pressed()

# mouse pos
mouse_pos = pygame.mouse.get_pos()


# game active
game_active = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

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

    if game_active:
        # invocar
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        # cuidado con las capas
        ############################### REAL TIME
        score = display_score()
        screen.blit(player_surface, player_rect)
        screen.blit(snail_surface, snail_rect)


        snail_rect.x -= 4
        if snail_rect.right == -120:
            snail_rect.left = 800


        # player gravity
        player_gravity += 1
        player_rect.y += player_gravity

        # fit to ground
        if player_rect.bottom >= 300:
            player_rect.bottom = 300

        # snail kill-collide-
        if snail_rect.colliderect(player_rect):
            game_active = False

        ###############################

    else:
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rect)

        #score message out of game
        score_message = texto_pequeno.render(f'Tu score: {score}', False, (111,196,169))
        score_message_rect = score_message.get_rect(center=(400,330))
        screen.blit(game_name, game_name_rect)


        if score == 0: screen.blit(game_message, game_message_rect)
        else: screen.blit(score_message, score_message_rect)

    pygame.display.update()
    clock.tick(60)
