import pygame as pg


class ArmoredWall(pg.sprite.Sprite):
    def __init__(self, x, y, armor=1):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.transform.scale(pg.image.load('images/wall.png'), (25, 25))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.armor = armor

