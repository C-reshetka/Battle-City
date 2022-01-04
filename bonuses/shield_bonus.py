import pygame as pg

import game
from bonuses.bonus_abstract import Bonus
from player import Player


class ShieldBonus(pg.sprite.Sprite, Bonus):
    def __init__(self, x, y, player):
        pg.sprite.Sprite.__init__(self)
        self.image = game.Game.load_sprite('shield', 25, 25)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.player = player

    def process(self, player):
        player: Player
        player.armor += 1


