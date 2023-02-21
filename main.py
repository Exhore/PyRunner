import pygame
from sys import exit
from random import randint


def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surface = texto_pequeno.render(f'SCORE: {score}', False, "black")
    score_rect = score_surface.get_rect(center=(700,30))
    screen.blit(score_surface, score_rect)
    return current_time


def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5
            if obstacle_rect.bottom == 300: screen.blit(snail_surface, obstacle_rect)
            else: screen.blit(mosca_surface, obstacle_rect)
            #delete obstacles if they are out of screen
            obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

        return obstacle_list
    else:
        return []


def collisions(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                return False
    return True






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
mosca_pos = (600, 90)

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

# obstacles
snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom=snail_pos)

mosca_surface = pygame.image.load('graphics/Fly/Fly1.png').convert_alpha()
mosca_surface_rect = mosca_surface.get_rect(midbottom=mosca_pos)



obstacle_rect_list = []


# keys
keys = pygame.key.get_pressed()

# mouse pos
mouse_pos = pygame.mouse.get_pos()


# game active
game_active = False


# timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            #space press
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom == 300:
                    player_gravity = -20

            # press mousebutton and collide with player model
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos):
                    player_gravity = -20

            #obstacle event
            if event.type == obstacle_timer:
                if randint(0,2):
                    obstacle_rect_list.append(snail_surface.get_rect(midbottom=(randint(900,1100),300)))
                else:
                    obstacle_rect_list.append(mosca_surface.get_rect(midbottom=(randint(900,1100),210)))

        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = int(pygame.time.get_ticks() / 1000)



    if game_active:
        # invocar
        screen.blit(ground_surface, (0, 300))
        screen.blit(sky_surface, (0, 0))
        # cuidado con las capas
        ############################### REAL TIME
        score = display_score()
        screen.blit(player_surface, player_rect)


        # obstacle movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)


        # player gravity
        player_gravity += 1
        player_rect.y += player_gravity

        # fit to ground
        if player_rect.bottom >= 300:
            player_rect.bottom = 300

        #collision
        game_active = collisions(player_rect, obstacle_rect_list)


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
