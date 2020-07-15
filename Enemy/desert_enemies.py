from Enemy.enemies import Enemy
import pygame
import os


class HammerGoblin(Enemy):
    images = []
    for _ in range(20):
        add_str = str(_)
        if _ < 10:
            add_str = "0" + add_str
        images.append(pygame.transform.scale(
            pygame.image.load(
                os.path.join("Game/Enemies/Monsters/Dessert/BigGoblin", "9_enemies_1_run_0" +
                             add_str + ".png")).convert_alpha(),
            (100, 100)))

    def __init__(self):
        super().__init__()
        self.name = "HammerGoblin"
        self.imgs = self.images[:]
        self.full_health = 40
        self.curr_health = self.full_health
        self.vel = 3
        self.if_killed_money_earned = 5
