import pygame as pg

import menu
from bonuses.bonus_abstract import Bonus
from button import Button
from enemies.armored_enemy import ArmoredEnemy
from enemies.rapidfire_enemy import RapidfireEnemy
from enemies.simple_enemy import SimpleEnemy
from enemies.supershoot_enemy import SupershootEnemy
from headquarter import Headquarter
from bonuses.heart_bonus import HeartBonus
from map_states import P, H, a, E, A, R, S, w, m, h, s
from player import Player
from projectile import Projectile
from bonuses.shield_bonus import ShieldBonus
from walls.armored_wall import ArmoredWall
from walls.mirror_wall import MirrorWall
from walls.unbroken_wall import UnbrokenWall
from walls.water_wall import WaterWall

all_sprites = pg.sprite.Group()
bullets = pg.sprite.Group()
all_walls = pg.sprite.Group()
unbroken_walls = pg.sprite.Group()
armored_walls = pg.sprite.Group()
enemies = pg.sprite.Group()
water_walls = pg.sprite.Group()
mirror_walls = pg.sprite.Group()
bonuses = pg.sprite.Group()


class Game(pg.sprite.Sprite):
    def __init__(self, map):
        pg.sprite.Sprite.__init__(self)
        self.game_window = pg.display.set_mode((500, 550))
        self.background = Game.load_sprite("bg", 500, 500)
        self.game_over_screen = Game.load_sprite('game_over_screen', 500, 500)
        self.win_screen = Game.load_sprite('win_screen', 500, 500)
        self.player = None
        self.headquarter = None
        self.score = 0
        self.init_map(map)
        self.score_and_health_line = Game.load_sprite('green_scale', 500, 50)
        self.is_running = True
        self.is_win = False
        self.keys = None

        self.main_loop()

    @staticmethod
    def register_sprite(sprite, *groups):
        all_sprites.add(sprite)
        for g in groups:
            g.add(sprite)

    @staticmethod
    def load_sprite(name, width, height):
        path = f"images/{name}.png"
        loaded_sprite = pg.transform.scale(pg.image.load(path), (width, height))
        return loaded_sprite

    def main_loop(self):
        while True:
            self.handle_input()
            self.process_game_logic()
            self.draw()

    def handle_input(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                quit()

        self.keys = pg.key.get_pressed()
        if self.keys[pg.K_UP]:
            if self.player.rect.y - self.player.speed >= 0:
                self.player.move(0, -self.player.speed)
        elif self.keys[pg.K_DOWN]:
            if self.player.rect.y + self.player.speed + self.player.height <= self.game_window.get_height():
                self.player.move(0, self.player.speed)
        elif self.keys[pg.K_RIGHT]:
            if self.player.rect.x + self.player.speed + self.player.width <= self.game_window.get_width():
                self.player.move(self.player.speed, 0)
        elif self.keys[pg.K_LEFT]:
            if self.player.rect.x - self.player.speed >= 0:
                self.player.move(-self.player.speed, 0)
        elif self.keys[pg.K_SPACE]:
            if not self.player.can_shoot:
                return
            if self.player.last_projectile_distance > self.player.shooting_interval:
                p = self.player.shoot()
                self.player.last_projectile_distance = 0
                self.register_sprite(p, bullets)

        if self.is_pressed(pg.K_LCTRL, pg.K_h, pg.K_l, pg.K_t):
            self.player.health = 100

        if self.is_pressed(pg.K_LCTRL, pg.K_s, pg.K_t, pg.K_p):
            for e in enemies:
                e: SimpleEnemy
                e.delta_x = 0
                e.delta_y = 0

        if self.is_pressed(pg.K_LCTRL, pg.K_s, pg.K_h, pg.K_t):
            self.player.shooting_interval = 25

    def process_game_logic(self):
        if not self.is_running:
            return
        if len(enemies) == 0:
            self.is_running = False
            self.is_win = True
            return

        for wall in pg.sprite.groupcollide(all_walls, bullets, False, True):
            if type(wall) is not ArmoredWall:
                continue
            wall: ArmoredWall
            wall.armor -= 1
            if wall.armor < 1:
                wall.kill()

        if pg.sprite.spritecollide(self.player, all_walls, False) or pg.sprite.spritecollide(self.player,
                                                                                             enemies, False):
            if pg.sprite.spritecollide(self.player, enemies, False):
                self.player.kill()
                self.is_running = False
            self.player.block_moving()

        for e in enemies:
            tmp_group = pg.sprite.Group([a for a in enemies if a != e])
            is_collision = pg.sprite.spritecollide(e, tmp_group, False)
            for e1 in is_collision:
                e: SimpleEnemy
                e1: SimpleEnemy
                e.delta_x, e.delta_y = -e.delta_x, -e.delta_y
                e1.delta_x, e1.delta_y = -e1.delta_x, -e1.delta_y
                e.move()
                e1.move()

        for e in pg.sprite.groupcollide(enemies, all_walls, False, False):
            e: SimpleEnemy
            while pg.sprite.spritecollide(e, all_walls, False):
                e.change_direction_of_moving()
                e.move(e.delta_x, e.delta_y)
                is_collision = pg.sprite.spritecollide(e, all_walls, False)
                if len(is_collision) == 0:
                    break
                e.move(-e.delta_x, -e.delta_y)

        for e in pg.sprite.groupcollide(enemies, water_walls, False, False):
            e: SimpleEnemy
            while pg.sprite.spritecollide(e, water_walls, False):
                e.change_direction_of_moving()
                e.move(e.delta_x, e.delta_y)
                is_collision = pg.sprite.spritecollide(e, water_walls, False)
                if len(is_collision) == 0:
                    break
                e.move(-e.delta_x, -e.delta_y)

        if pg.sprite.spritecollide(self.player, water_walls, False) or pg.sprite.spritecollide(self.player,
                                                                                               mirror_walls, False):
            self.player.block_moving()

        for e in pg.sprite.groupcollide(enemies, mirror_walls, False, False):
            e: SimpleEnemy
            while pg.sprite.spritecollide(e, mirror_walls, False):
                e.change_direction_of_moving()
                e.move(e.delta_x, e.delta_y)
                is_collision = pg.sprite.spritecollide(e, mirror_walls, False)
                if len(is_collision) == 0:
                    break
                e.move(-e.delta_x, -e.delta_y)

        for w, b in pg.sprite.groupcollide(mirror_walls, bullets, False, False).items():
            b = b[0]
            w: MirrorWall
            b: Projectile
            w.health -= 1
            b.delta_x, b.delta_y = -b.delta_x, -b.delta_y
            if w.health < 1:
                w.kill()

        for enemy, b in pg.sprite.groupcollide(enemies, bullets, False, True).items():
            enemy: SimpleEnemy
            b: [Projectile]
            if b[0].sender == "player":
                enemy.health -= 1
            if enemy.health < 1:
                enemy.kill()
                self.score += 1

        for bullet in pg.sprite.spritecollide(self.player, bullets, True):
            bullet: Projectile
            if bullet.sender == "enemy":
                if self.player.armor > 0:
                    self.player.armor -= 1
                else:
                    self.player.health -= 1
            if self.player.health < 1:
                self.player.kill()
                self.is_running = False

        if self.headquarter is not None and pg.sprite.spritecollide(self.headquarter, pg.sprite.GroupSingle(self.player), False):
            self.player.block_moving()

        if self.headquarter is not None:
            for e in pg.sprite.spritecollide(self.headquarter, bullets, True):
                self.headquarter: Headquarter
                self.headquarter.health -= 1
                if self.headquarter.health < 1:
                    self.headquarter.kill()
                    self.is_running = False

        for e in pg.sprite.spritecollide(self.headquarter, enemies, False):
            e: SimpleEnemy
            while pg.sprite.spritecollide(e, pg.sprite.GroupSingle(self.headquarter), False):
                e.change_direction_of_moving()
                e.move(e.delta_x, e.delta_y)
                is_collision = pg.sprite.spritecollide(e, pg.sprite.GroupSingle(self.headquarter), False)
                if len(is_collision) == 0:
                    break
                e.move(-e.delta_x, -e.delta_y)

        for e in pg.sprite.spritecollide(self.player, bonuses, True ):
            e: Bonus
            e.process(self.player)

    def draw(self):
        if not self.is_running:
            if self.is_win:
                self.draw_score_and_health()
                self.win()
            else:
                self.draw_score_and_health()
                self.game_over()
            pg.display.flip()
            return
        self.game_window.blit(self.background, (0, 0))
        self.game_window.blit(self.score_and_health_line, (0, 500))
        for e in all_sprites:
            self.game_window.blit(e.image, (e.rect.x, e.rect.y))
        self.draw_score_and_health()
        if self.player.armor > 0:
            self.game_window.blit(self.load_sprite('shield', 20, 20), (self.player.rect.x + 2, self.player.rect.y + 2))
        pg.display.flip()
        all_sprites.update()

    def init_map(self, map):
        for i in range(20):
            for j in range(20):
                if map[i][j] == 1:
                    wall = UnbrokenWall(j * 25, i * 25)
                    self.register_sprite(wall, all_walls, unbroken_walls)

                elif map[i][j] == P:
                    if self.player is not None:
                        raise ValueError
                    self.player = Player(j * 25, i * 25, health=5)
                    self.player.speed = 1
                    self.player.shooting_interval = 100
                    self.register_sprite(self.player)

                elif map[i][j] == a:
                    wall = ArmoredWall(j * 25, i * 25)
                    self.register_sprite(wall, all_walls, armored_walls)

                elif map[i][j] == E:
                    e = SimpleEnemy(j * 25, i * 25, -1, 0, 2)
                    self.register_sprite(e, enemies)

                elif map[i][j] == H:
                    e = Headquarter(j * 25, i * 25)
                    self.register_sprite(e)
                    self.headquarter = e

                elif map[i][j] == A:
                    e = ArmoredEnemy(j * 25, i * 25, -1, 0)
                    self.register_sprite(e, enemies)

                elif map[i][j] == R:
                    e = RapidfireEnemy(j * 25, i * 25, -1, 0)
                    self.register_sprite(e, enemies)

                elif map[i][j] == S:
                    e = SupershootEnemy(j * 25, i * 25, -1, 0)
                    self.register_sprite(e, enemies)

                elif map[i][j] == w:
                    e = WaterWall(j * 25, i * 25)
                    self.register_sprite(e, water_walls)

                elif map[i][j] == m:
                    e = MirrorWall(j * 25, i * 25)
                    self.register_sprite(e, mirror_walls)

                elif map[i][j] == h:
                    e = HeartBonus(j * 25, i * 25)
                    self.register_sprite(e, bonuses)

                elif map[i][j] == s:
                    e = ShieldBonus(j * 25, i * 25, self.player)
                    self.register_sprite(e, bonuses)

    def draw_score_and_health(self):
        f = pg.font.Font(pg.font.match_font('arial'), 32)
        if not self.is_running:
            self.player.health = 0
        score = f.render('Score:  ' + str(self.score), True, (0, 0, 0))
        text_rect = score.get_rect()
        text_rect.topleft = (2, 505)
        self.game_window.blit(score, text_rect)

        p_health = f.render('Health:  ' + str(self.player.health), True, (0, 0, 0))
        text_rect = p_health.get_rect()
        text_rect.topleft = (150, 505)
        self.game_window.blit(p_health, text_rect)

        h_health = f.render('Headquarter:  ' + str(self.headquarter.health), True, (0, 0, 0))
        text_rect = h_health.get_rect()
        text_rect.topleft = (298, 505)
        self.game_window.blit(h_health, text_rect)

    def game_over(self):
        if len(enemies) > 0:
            for e in enemies:
                e.kill()
        self.game_window.blit(self.game_over_screen, (0, 0))
        self.game_window.blit(self.score_and_health_line, (0, 500))
        self.draw_score_and_health()
        mb = Button(image=self.load_sprite('menu_button', 100, 50), x=10, y=440, event=self.goto_menu)
        self.game_window.blit(mb.image, (mb.rect.x, mb.rect.y))
        mb.update()

    def win(self):
        self.game_window.blit(self.win_screen, (0, 0))
        self.game_window.blit(self.score_and_health_line, (0, 500))
        self.draw_score_and_health()
        mb = Button(image=self.load_sprite('menu_button', 100, 50), x=10, y=440, event=self.goto_menu)
        self.game_window.blit(mb.image, (mb.rect.x, mb.rect.y))
        mb.update()

    def is_pressed(self, *keys_to_check):
        for k in keys_to_check:
            if not self.keys[k]:
                return False
        return True

    def goto_menu(self):
        global all_sprites
        global bullets
        global all_walls
        global unbroken_walls
        global armored_walls
        global enemies
        global water_walls
        global mirror_walls
        global bonuses
        all_sprites = pg.sprite.Group()
        bullets = pg.sprite.Group()
        all_walls = pg.sprite.Group()
        unbroken_walls = pg.sprite.Group()
        armored_walls = pg.sprite.Group()
        enemies = pg.sprite.Group()
        water_walls = pg.sprite.Group()
        mirror_walls = pg.sprite.Group()
        bonuses = pg.sprite.Group()
        menu.Menu()
        self.kill()
