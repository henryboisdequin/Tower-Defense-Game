import pygame
from Enemy.enemies import Enemy
import os


class Bat(Enemy):
    images = []
    for _ in range(10):
        add_str = str(_)
        if _ < 10:
            add_str = "0" + add_str
        images.append(pygame.transform.scale(
            pygame.image.load(
                os.path.join("Game/Enemies/Monsters/Graveyard/Bat", "1_enemies_1_RUN_0" +
                             add_str + ".png")).convert_alpha(),
            (100, 100)))

    def __init__(self):
        super().__init__()
        self.name = "Bat"
        self.imgs = self.images[:]
        self.full_health = 20
        self.curr_health = self.full_health
        self.vel = 7
        self.if_killed_money_earned = 5
