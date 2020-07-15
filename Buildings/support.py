from Buildings.tower import Tower
import pygame
import os
import math

range_imgs = pygame.transform.scale(pygame.image.load(os.path.join("Game/Buildings/Support", "6.png")).
                                    convert_alpha(), (90, 90))


class RangeTower(Tower):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.range = 75
        self.effect = 0.4
        self.tower_imgs = range_imgs
        self.width = self.height = 90
        self.name = "range"
        self.price = 1000

    def draw(self, win):
        """
        Draws support tower onto the screen.
        :param win: pygame surface
        :return: None
        """
        super().draw_range(win)
        super().draw(win)

    def support(self, towers):
        """
        Modify towers based on their ability.
        :param towers: list
        :return: None
        """
        effected = []
        for tower in towers:
            x = tower.x
            y = tower.y
            dis = math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)

            if dis <= self.range + tower.width / 2:
                effected.append(tower)

        for tower in effected:
            tower.range = tower.original_range + round(tower.range * self.effect)


damage_imgs = pygame.transform.scale(pygame.image.load(os.path.join("Game/Buildings/Support", "9.png")).
                                     convert_alpha(), (90, 90))


class DamageTower(RangeTower):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.range = 100
        self.tower_imgs = damage_imgs
        self.effect = 2.3
        self.name = "damage"
        self.price = 1400

    def support(self, towers):
        """
        Modify towers based on their ability.
        :param towers: list
        :return: None
        """
        effected = []
        for tower in towers:
            x = tower.x
            y = tower.y

            dis = math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)

            if dis <= self.range + tower.width / 2:
                effected.append(tower)

        for tower in effected:
            tower.damage = tower.original_damage + round(tower.original_damage * self.effect)


tower_imgs = pygame.image.load("Game/Buildings/Stone/7.png")
tower_imgs = pygame.transform.scale(tower_imgs, (100, 100))
stone_imgs = pygame.image.load("Game/Buildings/Stone/35.png")
stone_imgs = pygame.transform.scale(stone_imgs, (40, 40))


class StoneTower(DamageTower):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.range = 100
        self.tower_imgs = tower_imgs
        self.effect = 4.0
        self.name = "stone"
        self.price = 2000
        self.in_range = False

    def support(self, towers):
        """
        Modifies towers based on their ability.
        :param towers: list
        :return: None
        """
        effected = []
        for tower in towers:
            x = tower.x
            y = tower.y

            dis = math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)

            if dis <= self.range + tower.width / 2:
                effected.append(tower)

        for tower in effected:
            tower.damage = tower.original_damage + round(tower.original_damage * self.effect)

    def draw(self, win):
        """
        Draws Stone Tower onto the screen.
        :param win:
        :return:
        """
        super().draw_range(win)
        super().draw(win)
        # Fireballs
        win.blit(stone_imgs, (self.x, self.y - 60))
        win.blit(stone_imgs, (self.x - 54, self.y - 60))
