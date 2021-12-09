import pygame

from Projectile import Projectile
from Wall import Wall

pygame.init()
game_window_width = 500
game_window_height = 500
game_window = pygame.display.set_mode((game_window_width, game_window_height))
pygame.display.set_caption("Battle City")

clock = pygame.time.Clock()

player_sprite_right = pygame.transform.scale(pygame.image.load('tmp/pl_right.png'), (25, 25))
player_sprite_left = pygame.transform.scale(pygame.image.load('tmp/pl_left.png'), (25, 25))
player_sprite_up = pygame.transform.scale(pygame.image.load('tmp/pl_up.png'), (25, 25))
player_sprite_down = pygame.transform.scale(pygame.image.load('tmp/pl_down.png'), (25, 25))

background_sprite = pygame.transform.scale(pygame.image.load('tmp/bg.png'), (game_window_width, game_window_height))

player_x = 50
player_y = 50
player_width = 25
player_height = 25
player_speed = 1

is_left, is_right, is_down, is_up = 0, 0, 0, 1

is_running = True

sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
walls = pygame.sprite.Group()
wall = Wall(0, 0)
sprites.add(wall)
walls.add(wall)
bullets_pixel_interval_count = 0
bullets_interval = 100

while is_running:
    clock.tick()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        player_y -= player_speed if player_y - player_speed >= 0 else player_y
        is_left, is_right, is_down, is_up = 0, 0, 0, 1
    elif keys[pygame.K_DOWN]:
        if player_y + player_speed + player_height <= game_window_height:
            player_y += player_speed
        is_left, is_right, is_down, is_up = 0, 0, 1, 0
    elif keys[pygame.K_RIGHT]:
        if player_x + player_speed <= game_window_width - player_width:
            player_x += player_speed
        is_left, is_right, is_down, is_up = 0, 1, 0, 0
    elif keys[pygame.K_LEFT]:
        player_x -= player_speed if player_x - player_speed >= 0 else player_x
        is_left, is_right, is_down, is_up = 1, 0, 0, 0
    elif keys[pygame.K_SPACE]:
        if bullets_pixel_interval_count > bullets_interval:
            if is_left:
                p = Projectile(player_x - 0.5 * player_width, player_y + 0.2 * player_height, -1, 0)
            elif is_right:
                p = Projectile(player_x + player_width, player_y + 0.2 * player_height, 1, 0)
            elif is_up:
                p = Projectile(player_x + 0.25 * player_width, player_y - 0.7 * player_height, 0, -1)
            elif is_down:
                p = Projectile(player_x + 0.25 * player_width, player_y + player_height, 0, 1)
            bullets.add(p)
            sprites.add(p)
            bullets_pixel_interval_count = 0

    game_window.blit(background_sprite, (0, 0))
    bullets_pixel_interval_count += 1

    player_coordinates = (player_x, player_y)
    if is_up:
        game_window.blit(player_sprite_up, player_coordinates)
    elif is_down:
        game_window.blit(player_sprite_down, player_coordinates)
    elif is_right:
        game_window.blit(player_sprite_right, player_coordinates)
    elif is_left:
        game_window.blit(player_sprite_left, player_coordinates)

    for e in sprites:
        game_window.blit(e.image, (e.rect.x, e.rect.y))
    bullets.update()

    pygame.display.update()
pygame.quit()
