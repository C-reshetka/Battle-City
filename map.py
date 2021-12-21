import random

import pygame

from Enemy import Enemy
from Player import Player
from Projectile import Projectile
from UnbrokenWall import UnbrokenWall
from ArmoredWall import ArmoredWall


def display_sprites(sprites):
    for e in sprites:
        game_window.blit(e.image, (e.rect.x, e.rect.y))
    all_sprites.update()
    pygame.display.update()


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
            p = player_sprite.shoot()
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
all_walls = pygame.sprite.Group()
unbroken_walls = pygame.sprite.Group()
armored_walls = pygame.sprite.Group()

all_sprites.add(player)

w = ArmoredWall(25, 400)
armored_walls.add(w)
all_walls.add(w)
all_sprites.add(w)

for i in range(20):
    w = UnbrokenWall(0, i * 25)
    all_sprites.add(w)
    all_walls.add(w)
    unbroken_walls.add(w)

    w = UnbrokenWall(i * 25, 0)
    all_sprites.add(w)
    all_walls.add(w)
    unbroken_walls.add(w)

    w = UnbrokenWall(i * 25, 475)
    all_sprites.add(w)
    all_walls.add(w)
    unbroken_walls.add(w)

    w = UnbrokenWall(475, i * 25)
    all_sprites.add(w)
    all_walls.add(w)
    unbroken_walls.add(w)

player.shooting_interval = 100

enemies = pygame.sprite.Group()

e = Enemy(50, 50, bullets, all_sprites, delta_x=-1, health=1)
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

    for wall in pygame.sprite.groupcollide(all_walls, bullets, False, True):
        if type(wall) is not ArmoredWall:
            continue
        wall.armor -= 1
        if wall.armor < 1:
            wall.kill()

    enemies_collisions = pygame.sprite.spritecollide(player, enemies, False)

    if pygame.sprite.spritecollide(player, all_walls, False) or enemies_collisions:
        if enemies_collisions:
            player.kill()
        player.block_moving()

    for e in pygame.sprite.groupcollide(enemies, all_walls, False, False):
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
            is_collision = pygame.sprite.spritecollide(e, all_walls, False)
            if len(is_collision) == 0:
                break
            e.move(-delta_x, -delta_y)

    for enemy, bullet in pygame.sprite.groupcollide(enemies, bullets, False, True).items():
        if bullet[0].sender == "player":
            enemy.health -= 1
        if enemy.health < 1:
            enemy.kill()


    # display = threading.Thread(target=display_sprites(all_sprites))
    # display.start()
    display_sprites(all_sprites)

pygame.quit()
