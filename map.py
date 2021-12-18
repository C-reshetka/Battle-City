import pygame

from Player import Player
from Projectile import Projectile
from Wall import Wall

pygame.init()
game_window_width = 500
game_window_height = 500
game_window = pygame.display.set_mode((game_window_width, game_window_height))
pygame.display.set_caption("Battle City")

clock = pygame.time.Clock()

background_sprite = pygame.transform.scale(pygame.image.load('tmp/bg.png'), (game_window_width, game_window_height))

player_speed = 1

player = Player(50, 50)

is_running = True

sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()

sprites.add(player)
walls = pygame.sprite.Group()

wall = Wall(0, 0)
sprites.add(wall)
walls.add(wall)

wall = Wall(25, 25)
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

    delta_x, delta_y = 0, 0

    if keys[pygame.K_UP]:
        if player.rect.y - player_speed >= 0:
            player.move(0, -player_speed)
            delta_y = -player_speed
    elif keys[pygame.K_DOWN]:
        if player.rect.y + player_speed + player.height <= game_window_height:
            player.move(0, player_speed)
            delta_y = player_speed
    elif keys[pygame.K_RIGHT]:
        if player.rect.x + player_speed + player.width <= game_window_width:
            player.move(player_speed, 0)
            delta_x = player_speed
    elif keys[pygame.K_LEFT]:
        if player.rect.x - player_speed >= 0:
            player.move(-player_speed, 0)
            delta_x = -player_speed
    elif keys[pygame.K_SPACE]:
        if bullets_pixel_interval_count > bullets_interval:
            if player.is_left:
                p = Projectile(player.rect.x - 0.5 * player.width, player.rect.y + 0.2 * player.height, -1, 0)
            elif player.is_right:
                p = Projectile(player.rect.x + player.width, player.rect.y + 0.2 * player.height, 1, 0)
            elif player.is_up:
                p = Projectile(player.rect.x + 0.25 * player.width, player.rect.y - 0.7 * player.height, 0, -1)
            elif player.is_down:
                p = Projectile(player.rect.x + 0.25 * player.width, player.rect.y + player.height, 0, 1)
            bullets.add(p)
            sprites.add(p)
            bullets_pixel_interval_count = 0

    pygame.sprite.groupcollide(bullets, walls, True, False)

    game_window.blit(background_sprite, (0, 0))
    bullets_pixel_interval_count += 1

    if pygame.sprite.spritecollide(player, walls, False):
        player.change_sprite_on_move = False
        player.move(-delta_x, -delta_y)
        player.change_sprite_on_move = True
    for e in sprites:
        game_window.blit(e.image, (e.rect.x, e.rect.y))
    bullets.update()
    pygame.display.update()

pygame.quit()
