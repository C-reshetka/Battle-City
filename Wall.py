import pygame as pg


class Wall(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.transform.scale(pg.image.load('tmp/uncrashed_wall.png'), (25, 25))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

