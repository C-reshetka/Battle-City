import game
import simple_enemy
from projectile import Projectile


class SupershootEnemy(simple_enemy.SimpleEnemy):
    def __init__(self, x, y, delta_x=0, delta_y=0):
        super().__init__(x, y, delta_x, delta_y)
        self.enemy_sprite_left = game.Game.load_sprite('ss_left', 24, 24)
        self.enemy_sprite_right = game.Game.load_sprite('ss_right', 24, 24)
        self.enemy_sprite_up = game.Game.load_sprite('ss_up', 24, 24)
        self.enemy_sprite_down = game.Game.load_sprite('ss_down', 24, 24)
        self.shooting_interval = 75
        self.health = 3

    def shoot(self):
        result = []
        p = Projectile(self.rect.x - 0.5 * self.width,
                       self.rect.y + 0.2 * self.height, -2, 0, "enemy")
        result.append(p)
        p = Projectile(self.rect.x + self.width,
                       self.rect.y + 0.2 * self.height, 2, 0, "enemy")
        result.append(p)
        p = Projectile(self.rect.x + 0.25 * self.width,
                       self.rect.y - 0.7 * self.height, 0, -2, "enemy")
        result.append(p)
        p = Projectile(self.rect.x + 0.25 * self.width,
                       self.rect.y + self.height, 0, 2, "enemy")
        result.append(p)
        return result
