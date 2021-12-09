import pygame as pg


class Projectile(pg.sprite.Sprite):
    def __init__(self, x, y, delta_x, delta_y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.transform.scale(pg.image.load('tmp/projectile.png'), (15, 15))
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.delta_x = delta_x
        self.delta_y = delta_y

    def update(self):
        self.rect.x += self.delta_x
        self.rect.y += self.delta_y
        if self.rect.bottom < 0 or self.rect.right > 500 or self.rect.left < 0 or self.rect.top > 500:
            self.kill()

