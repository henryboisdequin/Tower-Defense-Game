import pygame
import os
from Enemy.enemies import Enemy


class MaskedMan(Enemy):
    images = []
    for _ in range(10):
        add_str = str(_)
        if _ < 10:
            add_str = "0" + add_str
        images.append(pygame.transform.scale(
            pygame.image.load(
                os.path.join("Game/Enemies/Monsters/Magic/Masked Man", "2_enemies_1_run_0" +
                             add_str + ".png")).convert_alpha(),
            (100, 100)))

    def __init__(self):
        super().__init__()
        self.name = "MaskedMan"
        self.imgs = self.images[:]
        self.full_health = 50
        self.curr_health = self.full_health
        self.vel = 5
        self.if_killed_money_earned = 8
