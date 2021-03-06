import pygame as pg

import game
from projectile import Projectile


class Player(pg.sprite.Sprite):
    def __init__(self, x, y, health=1):
        pg.sprite.Sprite.__init__(self)
        self.player_sprite_right = pg.transform.scale(pg.image.load('images/pl_right.png'), (25, 25))
        self.player_sprite_left = pg.transform.scale(pg.image.load('images/pl_left.png'), (25, 25))
        self.player_sprite_up = pg.transform.scale(pg.image.load('images/pl_up.png'), (25, 25))
        self.player_sprite_down = pg.transform.scale(pg.image.load('images/pl_down.png'), (25, 25))
        self.image = self.player_sprite_up
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x = self.rect.x
        self.y = self.rect.y
        self.is_left, self.is_right, self.is_down, self.is_up = 0, 0, 0, 1
        self.width, self.height = 25, 25
        self.change_sprite_on_move = True
        self.speed = 0
        self.last_delta_x = 0
        self.last_delta_y = 0
        self.last_projectile_distance = 0
        self.shooting_interval = 0
        self.can_shoot = True
        self.health = health
        self.armor = 0

    def move(self, delta_x, delta_y):
        self.can_shoot = True
        if delta_x > 0:
            self.rect.x += delta_x
            self.last_delta_y = 0
            self.last_delta_x = delta_x
            if self.change_sprite_on_move:
                self.image = self.player_sprite_right
                self.is_left, self.is_right, self.is_down, self.is_up = 0, 1, 0, 0
        elif delta_x < 0:
            self.rect.x += delta_x
            self.last_delta_y = 0
            self.last_delta_x = delta_x
            if self.change_sprite_on_move:
                self.image = self.player_sprite_left
                self.is_left, self.is_right, self.is_down, self.is_up = 1, 0, 0, 0
        elif delta_y > 0:
            self.rect.y += delta_y
            self.last_delta_x = 0
            self.last_delta_y = delta_y
            if self.change_sprite_on_move:
                self.image = self.player_sprite_down
                self.is_left, self.is_right, self.is_down, self.is_up = 0, 0, 1, 0
        elif delta_y < 0:
            self.rect.y += delta_y
            self.last_delta_x = 0
            self.last_delta_y = delta_y
            if self.change_sprite_on_move:
                self.image = self.player_sprite_up
                self.is_left, self.is_right, self.is_down, self.is_up = 0, 0, 0, 1

    def block_moving(self):
        self.change_sprite_on_move = False
        self.move(-self.last_delta_x, -self.last_delta_y)
        self.change_sprite_on_move = True

    def update(self):
        self.last_projectile_distance += 1

    def shoot(self):
        p = None
        if self.is_left:
            p = Projectile(self.rect.x - 0.6 * self.width,
                           self.rect.y + 0.2 * self.height, -1, 0, "player")
        elif self.is_right:
            p = Projectile(self.rect.x + self.width,
                           self.rect.y + 0.2 * self.height, 1, 0, "player")
        elif self.is_up:
            p = Projectile(self.rect.x + 0.25 * self.width,
                           self.rect.y - 0.7 * self.height, 0, -1, "player")
        elif self.is_down:
            p = Projectile(self.rect.x + 0.25 * self.width,
                           self.rect.y + self.height, 0, 1, "player")
        return p
