import pygame
from Enemy.enemies import Enemy
import os

pygame.init()
pygame.display.set_mode((1350, 700))


class Golem(Enemy):
    images = []
    for _ in range(10):
        add_str = str(_)
        images.append(pygame.transform.scale(
            pygame.image.load(
                os.path.join("Game/Enemies/Bosses/Golem", "0_boss_run_00" + add_str + ".png")).convert_alpha(),
            (150, 150)))

    def __init__(self):
        super().__init__()
        self.name = "Golem"
        self.imgs = self.images[:]
        self.full_health = 100
        self.vel = 3
        self.if_killed_money_earned = 100
        self.curr_health = self.full_health


class Guard(Enemy):
    images = []
    for _ in range(10):
        add_str = str(_)
        images.append(pygame.transform.scale(
            pygame.image.load(
                os.path.join("Game/Enemies/Bosses/Guard", "0_boss_run_00" + add_str + ".png")).convert_alpha(),
            (150, 150)))

    def __init__(self):
        super().__init__()
        self.name = "Guard"
        self.imgs = self.images[:]
        self.full_health = 80
        self.vel = 4
        self.curr_health = self.full_health
        self.if_killed_money_earned = 90


class Tree(Enemy):
    images = []
    for _ in range(10):
        add_str = str(_)
        images.append(pygame.transform.scale(
            pygame.image.load(
                os.path.join("Game/Enemies/Bosses/Tree", "0_boss_run_00" + add_str + ".png")).convert_alpha(),
            (100, 100)))

    def __init__(self):
        super().__init__()
        self.name = "Tree"
        self.imgs = self.images[:]
        self.full_health = 70
        self.vel = 6
        self.curr_health = self.full_health
        self.if_killed_money_earned = 100


class Yeti(Enemy):
    images = []
    for _ in range(10):
        add_str = str(_)
        images.append(pygame.transform.scale(
            pygame.image.load(
                os.path.join("Game/Enemies/Bosses/Yeti", "0_boss_run_00" + add_str + ".png")).convert_alpha(),
            (150, 150)))

    def __init__(self):
        super().__init__()
        self.name = "Yeti"
        self.imgs = self.images[:]
        self.full_health = 90
        self.curr_health = self.full_health
        self.vel = 4
        self.if_killed_money_earned = 90


class SuperBoss(Enemy):
    images = []
    for _ in range(20):
        add_str = str(_)
        if _ < 10:
            add_str = "0" + add_str
        images.append(pygame.transform.scale(
            pygame.image.load(
                os.path.join("Game/Enemies/Bosses/SuperBoss", "2_enemies_1_walk_0" + add_str + ".png")).convert_alpha(),
            (200, 200)))

    def __init__(self):
        super().__init__()
        self.name = "superboss"
        self.imgs = self.images[:]
        self.full_health = 500
        self.curr_health = self.full_health
        self.vel = 10
        self.if_killed_money_earned = 1000
