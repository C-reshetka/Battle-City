import random

import pygame

from Player import Player
from Projectile import Projectile
from Wall import Wall
from Enemy import Enemy


def process_keys(player_sprite, bullets_group, all_sprites_group):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        if player_sprite.rect.y - player_sprite.speed >= 0:
            player_sprite.move(0, -player_sprite.speed)
    elif keys[pygame.K_DOWN]:
        if player_sprite.rect.y + player_sprite.speed + player_sprite.height <= game_window_height:
            player_sprite.move(0, player_sprite.speed)
    elif keys[pygame.K_RIGHT]:
        if player_sprite.rect.x + player_sprite.speed + player_sprite.width <= game_window_width:
            player_sprite.move(player_sprite.speed, 0)
    elif keys[pygame.K_LEFT]:
        if player_sprite.rect.x - player_sprite.speed >= 0:
            player_sprite.move(-player_sprite.speed, 0)
    elif keys[pygame.K_SPACE]:
        if not player_sprite.can_shoot:
            return
        if player_sprite.last_projectile_distance > player_sprite.shooting_interval:
            p = None
            if player_sprite.is_left:
                p = Projectile(player_sprite.rect.x - 0.5 * player_sprite.width,
                               player_sprite.rect.y + 0.2 * player_sprite.height, -1, 0)
            elif player_sprite.is_right:
                p = Projectile(player_sprite.rect.x + player_sprite.width,
                               player_sprite.rect.y + 0.2 * player_sprite.height, 1, 0)
            elif player_sprite.is_up:
                p = Projectile(player_sprite.rect.x + 0.25 * player_sprite.width,
                               player_sprite.rect.y - 0.7 * player_sprite.height, 0, -1)
            elif player_sprite.is_down:
                p = Projectile(player_sprite.rect.x + 0.25 * player_sprite.width,
                               player_sprite.rect.y + player_sprite.height, 0, 1)
            player_sprite.last_projectile_distance = 0
            bullets_group.add(p)
            all_sprites_group.add(p)


pygame.init()
game_window_width = 500
game_window_height = 500
game_window = pygame.display.set_mode((game_window_width, game_window_height))
pygame.display.set_caption("Battle City")
clock = pygame.time.Clock()

background_sprite = pygame.transform.scale(pygame.image.load('tmp/bg.png'), (game_window_width, game_window_height))

player = Player(150, 150)
player.speed = 1

all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
walls = pygame.sprite.Group()

all_sprites.add(player)

wall = Wall(25, 25)
all_sprites.add(wall)
walls.add(wall)

wall = Wall(50, 25)
all_sprites.add(wall)
walls.add(wall)

wall = Wall(100, 25)
all_sprites.add(wall)
walls.add(wall)

wall = Wall(75, 25)
all_sprites.add(wall)
walls.add(wall)

wall = Wall(25, 75)
all_sprites.add(wall)
walls.add(wall)

wall = Wall(50, 75)
all_sprites.add(wall)
walls.add(wall)

wall = Wall(100, 75)
all_sprites.add(wall)
walls.add(wall)

wall = Wall(75, 75)
all_sprites.add(wall)
walls.add(wall)

wall = Wall(25, 50)
all_sprites.add(wall)
walls.add(wall)

wall = Wall(100, 50)
all_sprites.add(wall)
walls.add(wall)

player.shooting_interval = 100

enemies = pygame.sprite.Group()

e = Enemy(50, 50, -1)
enemies.add(e)
all_sprites.add(e)

is_running = True

while is_running:
    clock.tick()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    game_window.blit(background_sprite, (0, 0))
    process_keys(player, bullets, all_sprites)

    pygame.sprite.groupcollide(bullets, walls, True, False)
    if pygame.sprite.spritecollide(player, walls, False) or pygame.sprite.spritecollide(player, enemies, False):
        player.block_moving()

    for e in pygame.sprite.groupcollide(enemies, walls, False, False):
        is_collision = True
        while True:
            if e.rect.x % 25 != 0:
                if e.rect.x % 25 > 12.5:
                    e.rect.x = (e.rect.x // 25) * 25 + 25
                else:
                    e.rect.x = (e.rect.x // 25) * 25
            if e.rect.y % 25 != 0:
                if e.rect.y % 25 > 12.5:
                    e.rect.y = (e.rect.y // 25) * 25 + 25
                else:
                    e.rect.y = (e.rect.y // 25) * 25
            delta_x, delta_y = random.randrange(-1, 2), random.randrange(-1, 2)
            if delta_x * delta_y != 0:
                tmp = random.randrange(0, 2)
                if tmp == 0:
                    delta_y = 0
                else:
                    delta_x = 0
            e.move(delta_x, delta_y)
            is_collision = pygame.sprite.spritecollide(e, walls, False)
            if len(is_collision) == 0:
                break
            e.move(-delta_x, -delta_y)

    for e in all_sprites:
        game_window.blit(e.image, (e.rect.x, e.rect.y))
    all_sprites.update()
    pygame.display.update()

pygame.quit()
