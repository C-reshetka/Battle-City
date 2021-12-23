import pygame as pg

import maps
from game import Game
from button import Button


class Menu(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        pg.init()
        pg.display.set_caption("Battle City")
        self.game_window = pg.display.set_mode((500, 550))
        self.background = Game.load_sprite('menu_background', 500, 500)
        self.title = Game.load_sprite('battle-city_picture', 500, 100)
        self.bl1 = Button(image=Game.load_sprite('bl1', 100, 50), x=200, y=250, event=self.b1_click)
        self.bl2 = Button(image=Game.load_sprite('bl2', 100, 50), x=200, y=325, event=self.b2_click)
        self.bl3 = Button(image=Game.load_sprite('bl3', 100, 50), x=200, y=400, event=self.b3_click)
        self.buttons = pg.sprite.Group([self.bl1, self.bl2, self.bl3])
        self.main_loop()

    def main_loop(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    quit()
            self.game_window.blit(self.background, (0, 0))
            self.game_window.blit(self.title, (0, 75))
            for e in self.buttons:
                self.game_window.blit(e.image, (e.rect.x, e.rect.y))
            self.buttons.update()
            pg.display.flip()

    def b1_click(self):
        Game(maps.map_1)
        self.kill()

    def b2_click(self):
        Game(maps.map_2)
        self.kill()

    def b3_click(self):
        Game(maps.map_3)
        self.kill()




