import pygame as pg


class Headquarter(pg.sprite.Sprite):
    def __init__(self, x, y, health=10):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.transform.scale(pg.image.load('images/headquartes.png'), (25, 25))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.health = health


