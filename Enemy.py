import pygame as pg


class Enemy(pg.sprite.Sprite):
    def __init__(self, x, y, delta_x=0, delta_y=0):
        pg.sprite.Sprite.__init__(self)
        self.enemy_sprite_right = pg.transform.scale(pg.image.load('tmp/enemy_right.png'), (25, 25))
        self.enemy_sprite_left = pg.transform.scale(pg.image.load('tmp/enemy_left.png'), (25, 25))
        self.enemy_sprite_up = pg.transform.scale(pg.image.load('tmp/enemy_up.png'), (25, 25))
        self.enemy_sprite_down = pg.transform.scale(pg.image.load('tmp/enemy_down.png'), (25, 25))
        self.image = self.enemy_sprite_up
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.delta_x = delta_x
        self.delta_y = delta_y

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
