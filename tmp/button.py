import pygame as pg


class Button(pg.sprite.Sprite):
    def __init__(self, x, y, image, event):
        pg.sprite.Sprite.__init__(self)
        self.image = image
        self.event = event
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.rect.width
        self.height = self.rect.height

    def update(self):
        click = pg.mouse.get_pressed()
        mouse = pg.mouse.get_pos()
        if self.rect.x < mouse[0] < self.rect.x + self.width and self.rect.y < mouse[1] < self.rect.y + self.height and \
                click[0]:
            self.event()
