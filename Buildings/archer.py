import pygame
import os
from Buildings.tower import Tower
import math
from menu import Menu

menu_bg = pygame.transform.scale(pygame.image.load(os.path.join("Game/Shop", "window_1.png")).convert_alpha(),
                                 (120, 70))

archer_imgs1 = []

# load archer tower images
tower_imgs1 = pygame.transform.scale(
    pygame.image.load(os.path.join("Game/Buildings/Archer", "4.png")).convert_alpha(),
    (90, 90))

# load archer images
for _ in range(64, 69):
    archer_imgs1.append(pygame.image.load(os.path.join("Game/Buildings/Archer/", str(_) + '.png')))


class ArcherTower(Tower):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.tower_imgs = tower_imgs1
        self.archer_imgs = archer_imgs1[:]
        self.archer_count = 0
        self.range = 200
        self.original_range = self.range
        self.in_range = False
        self.left = True
        self.damage = 30
        self.width = self.height = 90
        self.original_damage = self.damage
        self.moving = False
        self.name = "archer"
        self.menu = Menu(self, self.x, self.y, menu_bg, 2000)

    def get_cost(self):
        """
        Returns cost of the tower.
        :return: int
        """
        return self.menu.get_item_cost()

    def draw(self, win):
        """
        Draws tower, animated archer onto the screen.
        :param win: pygame surface
        :return: None
        """
        super().draw_range(win)
        super().draw(win)

        if self.in_range and not self.moving:
            self.archer_count += 1
            if self.archer_count >= len(self.archer_imgs) * 10:
                self.archer_count = 0
        else:
            self.archer_count = 0

        archer = self.archer_imgs[self.archer_count // 10]
        if self.left is True:
            add = -25
        else:
            add = -archer.get_width() + 10

        win.blit(archer, ((self.x + add), (self.y - archer.get_height() - 25)))  # archer

    def attack(self, enemies):
        """
        How archer attacks enemy in the enemy list and modifies the list accordingly.
        :param enemies: list
        :return: None
        """
        money = 0
        self.in_range = False
        enemy_closest = []
        for enemy in enemies:
            x = enemy.x
            y = enemy.y

            dis = math.sqrt((self.x - 100 / 2 - x) ** 2 + (self.y - 100 / 2 - y) ** 2)
            if dis < self.range:
                self.in_range = True
                enemy_closest.append(enemy)

        enemy_closest.sort(key=lambda i: i.path_pos)
        enemy_closest = enemy_closest[::-1]

        if len(enemy_closest) > 0:
            first_enemy = enemy_closest[0]
            if self.archer_count == 14 or self.archer_count == 24 or self.archer_count == 33 or self.archer_count == 49:
                if first_enemy.health(self.damage) is True:
                    money = first_enemy.if_killed_money_earned * 2
                    enemies.remove(first_enemy)

            if first_enemy.x > self.x and not self.left:
                self.left = True
                for x, img in enumerate(self.archer_imgs):
                    self.archer_imgs[x] = pygame.transform.flip(img, True, False)
            elif self.left and first_enemy.x < self.x:
                self.left = False
                for x, img in enumerate(self.archer_imgs):
                    self.archer_imgs[x] = pygame.transform.flip(img, True, False)

        return money
