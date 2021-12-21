import pygame as pg

from Projectile import Projectile


class Enemy(pg.sprite.Sprite):
    def __init__(self, x, y, bullets, all_sprites, delta_x=0, delta_y=0, health=2):
        pg.sprite.Sprite.__init__(self)
        self.enemy_sprite_right = pg.transform.scale(pg.image.load('tmp/enemy_right.png'), (25, 25))
        self.enemy_sprite_left = pg.transform.scale(pg.image.load('tmp/enemy_left.png'), (25, 25))
        self.enemy_sprite_up = pg.transform.scale(pg.image.load('tmp/enemy_up.png'), (25, 25))
        self.enemy_sprite_down = pg.transform.scale(pg.image.load('tmp/enemy_down.png'), (25, 25))
        self.image = self.enemy_sprite_up
        self.rect = self.image.get_rect()
        self.width, self.height = 25, 25
        self.rect.x = x
        self.rect.y = y
        self.delta_x = delta_x
        self.delta_y = delta_y
        self.health = health
        self.shooting_interval = 100
        self.shooting_time = 0
        self.bullets = bullets
        self.all_sprites = all_sprites

    def move(self, delta_x=0, delta_y=0):
        if delta_x == delta_y == 0:
            delta_x, delta_y = self.delta_x, self.delta_y
        self.delta_x = delta_x
        self.delta_y = delta_y
        self.rect.x += delta_x
        self.rect.y += delta_y
        self.change_image()

    def change_image(self):
        if self.delta_y > 0:
            self.image = self.enemy_sprite_down
        elif self.delta_y < 0:
            self.image = self.enemy_sprite_up
        elif self.delta_x > 0:
            self.image = self.enemy_sprite_right
        elif self.delta_x < 0:
            self.image = self.enemy_sprite_left

    def update(self):
        self.move(self.delta_x, self.delta_y)
        self.shooting_time += 1
        if self.shooting_time > self.shooting_interval:
            self.shooting_time = 0
            p = self.shoot()
            self.all_sprites.add(p)
            self.bullets.add(p)

    def shoot(self):
        p = None
        if self.image == self.enemy_sprite_left:
            p = Projectile(self.rect.x - 0.5 * self.width,
                           self.rect.y + 0.2 * self.height, -2, 0, "enemy")
        elif self.image == self.enemy_sprite_right:
            p = Projectile(self.rect.x + self.width,
                           self.rect.y + 0.2 * self.height, 2, 0, "enemy")
        elif self.image == self.enemy_sprite_up:
            p = Projectile(self.rect.x + 0.25 * self.width,
                           self.rect.y - 0.7 * self.height, 0, -2, "enemy")
        elif self.image == self.enemy_sprite_down:
            p = Projectile(self.rect.x + 0.25 * self.width,
                           self.rect.y + self.height, 0, 2, "enemy")
        return p
