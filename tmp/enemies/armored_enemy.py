import enemies.simple_enemy
import game


class ArmoredEnemy(enemies.simple_enemy.SimpleEnemy):
    def __init__(self, x, y, delta_x=0, delta_y=0):
        super().__init__(x, y, delta_x, delta_y)
        self.enemy_sprite_left = game.Game.load_sprite('ae_left', 24, 24)
        self.enemy_sprite_right = game.Game.load_sprite('ae_right', 24, 24)
        self.enemy_sprite_up = game.Game.load_sprite('ae_up', 24, 24)
        self.enemy_sprite_down = game.Game.load_sprite('ae_down', 24, 24)
        self.health = 5
