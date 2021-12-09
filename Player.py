import pygame as pg


class Player(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.player_sprite_right = pg.transform.scale(pg.image.load('tmp/pl_right.png'), (25, 25))
        self.player_sprite_left = pg.transform.scale(pg.image.load('tmp/pl_left.png'), (25, 25))
        self.player_sprite_up = pg.transform.scale(pg.image.load('tmp/pl_up.png'), (25, 25))
        self.player_sprite_down = pg.transform.scale(pg.image.load('tmp/pl_down.png'), (25, 25))
        self.image = self.player_sprite_up
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x = self.rect.x
        self.y = self.rect.y
        self.is_left, self.is_right, self.is_down, self.is_up = 0, 0, 0, 1
        self.width, self.height = 25, 25

    def move(self, delta_x, delta_y):
        if delta_x > 0:
            self.rect.x += delta_x
            self.image = self.player_sprite_right
            self.is_left, self.is_right, self.is_down, self.is_up = 0, 1, 0, 0
        elif delta_x < 0:
            self.rect.x += delta_x
            self.image = self.player_sprite_left
            self.is_left, self.is_right, self.is_down, self.is_up = 1, 0, 0, 0
        elif delta_y > 0:
            self.rect.y += delta_y
            self.image = self.player_sprite_down
            self.is_left, self.is_right, self.is_down, self.is_up = 0, 0, 1, 0
        elif delta_y < 0:
            self.rect.y += delta_y
            self.image = self.player_sprite_up
            self.is_left, self.is_right, self.is_down, self.is_up = 0, 0, 0, 1
