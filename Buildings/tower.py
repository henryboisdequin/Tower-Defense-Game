import pygame
from menu import Menu
import os
import math

menu_bg = pygame.transform.scale(pygame.image.load(os.path.join("Game/Shop", "window_1.png")).convert_alpha(),
                                 (120, 70))


class Tower(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 0
        self.height = 0
        self.sell_price = 0
        self.price = 0
        self.selected = False
        self.range = 0
        self.menu = Menu(self, self.x, self.y, menu_bg, 2000)
        self.tower_imgs = None
        self.damage = 1
        self.place_color = (0, 0, 255, 100)

    def draw(self, win):
        """
        Draws tower on screen.
        :param win: pygame surface
        :return: None
        """
        img = self.tower_imgs
        win.blit(img, (self.x - img.get_width() // 2, self.y - img.get_height() // 2))

        if self.selected:
            self.menu.draw(win)

    def clicked(self, x_pos, y_pos):
        """
        Returns if tower if clicked on
        :param x_pos: int
        :param y_pos: int
        :return: bool
        """
        img = self.tower_imgs
        if self.x - img.get_width() // 2 + self.width >= x_pos >= self.x - img.get_width() // 2:
            if self.y + self.height - img.get_height() // 2 >= y_pos >= self.y - img.get_height() // 2:
                return True
        return False

    def draw_range(self, win):
        """
        Draws range of tower if clicked on.
        :param win: pygame surface
        :return: None
        """
        if self.selected:
            surface = pygame.Surface((self.range * 4, self.range * 4), pygame.SRCALPHA, 32)
            pygame.draw.circle(surface, (128, 128, 128, 100), (self.range, self.range), self.range, 0)

            win.blit(surface, (self.x - self.range, self.y - self.range))

    def draw_placement(self, win):
        """
        Draws placement range.
        :param win: pygame surface
        :return: None
        """
        surface = pygame.Surface((self.range * 4, self.range * 4), pygame.SRCALPHA, 32)
        pygame.draw.circle(surface, self.place_color, (50, 50), 50, 0)

        win.blit(surface, (self.x - 50, self.y - 50))

    def click(self, X, Y):
        """
        Returns if tower has been clicked on.
        :param X: int
        :param Y: int
        :return: bool
        """
        img = self.tower_imgs
        if self.x - img.get_width() // 2 + self.width >= X >= self.x - img.get_width() // 2:
            if self.y + self.height - img.get_height() // 2 >= Y >= self.y - img.get_height() // 2:
                return True
        return False

    def buy_and_pay(self):
        """
        Returns price of tower.
        :return: int
        """
        return self.price

    def move_tower(self, x, y):
        """
        Enables ability to move tower if desired.
        :param x: int
        :param y: int
        :return: None
        """
        self.x = x
        self.y = y
        self.menu.x = x
        self.menu.y = y
        self.menu.update()

    def collide_other_tower(self, other_tower):
        """
        Returns if tower has collided with other towers.
        :param other_tower: list
        :return: bool
        """
        x2 = other_tower.x
        y2 = other_tower.y

        dis = math.sqrt((x2 - self.x) ** 2 + (y2 - self.y) ** 2)
        if dis >= 100:
            return False
        else:
            return True
