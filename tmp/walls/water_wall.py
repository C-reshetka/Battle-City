import pygame as pg

import game


class WaterWall(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = game.Game.load_sprite('water', 25, 25)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y