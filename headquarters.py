import pygame as pg
from game import Game


class Headquarters(pg.sprite.Sprite):
    def __init__(self, x, y, health=10):
        pg.sprite.Sprite.__init__(self)
        self.image = Game.load_sprite('headquarters', 25, 25)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.health = health


