import random

import pygame as pg

from armored_wall import ArmoredWall
from enemy import Enemy
from player import Player
from projectile import Projectile
from unbroken_wall import UnbrokenWall


class Game:
    def __init__(self, map):
        self.game_window = pg.display.set_mode((500, 550))
        self.background = Game.load_sprite("bg", 500, 500)
        self.game_over_screen = Game.load_sprite('game_over_screen', 500, 500)
        self.win_screen = Game.load_sprite('win_screen', 500, 500)
        self.init_sprite_groups()
        self.player = None
        self.score = 0
        self.init_map(map)
        self.score_and_health_line = Game.load_sprite('green_scale', 500, 50)
        self.is_running = True
        self.is_win = False

        self.main_loop()

    def init_sprite_groups(self):
        self.all_sprites = pg.sprite.Group()
        self.bullets = pg.sprite.Group()
        self.all_walls = pg.sprite.Group()
        self.unbroken_walls = pg.sprite.Group()
        self.armored_walls = pg.sprite.Group()
        self.enemies = pg.sprite.Group()

    def register_sprite(self, sprite, *groups):
        self.all_sprites.add(sprite)
        for g in groups:
            g.add(sprite)

    @staticmethod
    def load_sprite(name, width, height):
        path = f"images/{name}.png"
        loaded_sprite = pg.transform.scale(pg.image.load(path), (width, height))
        return loaded_sprite

    def main_loop(self):
        while True:
            self.handle_input()
            self.process_game_logic()
            self.draw()

    def handle_input(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                quit()

        keys = pg.key.get_pressed()
        if keys[pg.K_UP]:
            if self.player.rect.y - self.player.speed >= 0:
                self.player.move(0, -self.player.speed)
        elif keys[pg.K_DOWN]:
            if self.player.rect.y + self.player.speed + self.player.height <= self.game_window.get_height():
                self.player.move(0, self.player.speed)
        elif keys[pg.K_RIGHT]:
            if self.player.rect.x + self.player.speed + self.player.width <= self.game_window.get_width():
                self.player.move(self.player.speed, 0)
        elif keys[pg.K_LEFT]:
            if self.player.rect.x - self.player.speed >= 0:
                self.player.move(-self.player.speed, 0)
        elif keys[pg.K_SPACE]:
            if not self.player.can_shoot:
                return
            if self.player.last_projectile_distance > self.player.shooting_interval:
                p = self.player.shoot()
                print(p)
                self.player.last_projectile_distance = 0
                self.register_sprite(p, self.bullets)

    def process_game_logic(self):
        if not self.is_running:
            return
        if len(self.enemies) == 0:
            self.is_running = False
            self.is_win = True
            return

        for wall in pg.sprite.groupcollide(self.all_walls, self.bullets, False, True):
            if type(wall) is not ArmoredWall:
                continue
            wall: ArmoredWall
            wall.armor -= 1
            if wall.armor < 1:
                wall.kill()

        if pg.sprite.spritecollide(self.player, self.all_walls, False) or pg.sprite.spritecollide(self.player,
                                                                                                  self.enemies, False):
            if pg.sprite.spritecollide(self.player, self.enemies, False):
                self.player.kill()
                self.is_running = False
            self.player.block_moving()

        for e in pg.sprite.groupcollide(self.enemies, self.all_walls, False, False):
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
                e: Player
                e.move(delta_x, delta_y)
                is_collision = pg.sprite.spritecollide(e, self.all_walls, False)
                if len(is_collision) == 0:
                    break
                e.move(-delta_x, -delta_y)

        for enemy, bullets in pg.sprite.groupcollide(self.enemies, self.bullets, False, True).items():
            enemy: Enemy
            bullets: [Projectile]
            if bullets[0].sender == "player":
                enemy.health -= 1
            if enemy.health < 1:
                enemy.kill()
                self.score += 1

        for bullet in pg.sprite.spritecollide(self.player, self.bullets, True):
            bullet: Projectile
            if bullet.sender == "enemy":
                self.player.health -= 1
            if self.player.health < 1:
                self.player.kill()
                self.is_running = False

    def draw(self):
        if not self.is_running:
            if self.is_win:
                self.draw_score_and_health()
                self.win()
            else:
                self.draw_score_and_health()
                self.game_over()
            pg.display.flip()
            return
        self.game_window.blit(self.background, (0, 0))
        self.game_window.blit(self.score_and_health_line, (0, 500))
        for e in self.all_sprites:
            self.game_window.blit(e.image, (e.rect.x, e.rect.y))
        self.draw_score_and_health()
        pg.display.flip()
        self.all_sprites.update()

    def init_map(self, map):
        for i in range(20):
            for j in range(20):
                if map[i][j] == 1:
                    wall = UnbrokenWall(j * 25, i * 25)
                    self.register_sprite(wall, self.all_walls, self.unbroken_walls)

                elif map[i][j] == 9:
                    if self.player is not None:
                        raise ValueError
                    self.player = Player(j * 25, i * 25, health=5)
                    self.player.speed = 1
                    self.player.shooting_interval = 100
                    self.register_sprite(self.player)

                elif map[i][j] == 2:
                    wall = ArmoredWall(j * 25, i * 25)
                    self.register_sprite(wall, self.all_walls, self.armored_walls)

                elif map[i][j] == 3:
                    e = Enemy(j * 25, i * 25, self.bullets, self.all_sprites, -1, 0, 2)
                    self.register_sprite(e, self.enemies)

    def draw_score_and_health(self):
        font = pg.font.Font(pg.font.match_font('arial'), 32)
        if not self.is_running:
            self.player.health = 0
        score = font.render('Score:  ' + str(self.score), True, (0, 0, 0))
        text_rect = score.get_rect()
        text_rect.topleft = (0, 505)
        self.game_window.blit(score, text_rect)

        health = font.render('Health:  ' + str(self.player.health), True, (0, 0, 0))
        text_rect = score.get_rect()
        text_rect.topleft = (150, 505)
        self.game_window.blit(health, text_rect)

    def game_over(self):
        if len(self.enemies) > 0:
            for e in self.enemies:
                e.kill()
        self.game_window.blit(self.game_over_screen, (0, 0))
        self.game_window.blit(self.score_and_health_line, (0, 500))
        self.draw_score_and_health()

    def win(self):
        self.game_window.blit(self.win_screen, (0, 0))
        self.game_window.blit(self.score_and_health_line, (0, 500))
        self.draw_score_and_health()