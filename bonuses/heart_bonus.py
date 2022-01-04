import pygame as pg

import game
from bonuses.bonus_abstract import Bonus
from player import Player


class HeartBonus(pg.sprite.Sprite, Bonus):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = game.Game.load_sprite('heart', 25, 25)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def process(self, player):
        player: Player
        player.health += 2
