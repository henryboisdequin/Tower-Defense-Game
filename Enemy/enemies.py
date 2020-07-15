import pygame
import math


class Enemy(object):
    def __init__(self):
        self.alive = True
        self.height = 64
        self.width = 64
        self.vel = 0
        self.full_health = 0
        self.curr_health = self.full_health
        self.enemies = []
        self.imgs = None
        self.path = [(-10, 477),
        (0, 477), (171, 481), (315, 528), (464, 529), (631, 532), (802, 532), (846, 358), (673, 323), (533, 301),
        (513, 209),
        (491, 118), (661, 102), (826, 99), (1003, 100), (1179, 97), (1346, 96)]
        self.x = self.path[0][0]
        self.y = self.path[0][1]
        self.path_pos = 0
        self.an_count = 0
        self.flipped = False
        self.name = None
        self.if_killed_money_earned = 0

    def draw(self, win):
        """
        Draws enemies on the screen.
        :param win: pygame surface
        :return: None
        """
        self.img = self.imgs[self.an_count]

        win.blit(self.img, (self.x - self.img.get_width() / 2, self.y - self.img.get_height() / 2 - 35))
        self.draw_health_bar(win)

    def draw_health_bar(self, win):
        """
        :param win: pygame surface
        :return: None
        """
        length = 50
        move_by = length / self.full_health
        health_bar = round(move_by * self.curr_health)

        pygame.draw.rect(win, (255, 0, 0), (self.x - 30, self.y - 75, length, 10), 0)
        pygame.draw.rect(win, (0, 255, 0), (self.x - 30, self.y - 75, health_bar, 10), 0)

    def move(self):
        """
        How enemy will move on the screen.
        :return: None
        """
        try:
            self.an_count += 1
            if self.an_count >= len(self.imgs):
                self.an_count = 0

            x1, y1 = self.path[self.path_pos]

            if self.path_pos + 1 >= len(self.path):
                x2, y2 = (-10, 10)
            else:
                x2, y2 = self.path[self.path_pos + 1]

            dirn = ((x2 - x1), (y2 - y1))
            length = math.sqrt((dirn[0] ** 2) + (dirn[1]) ** 2)
            dirn = (dirn[0] / length * self.vel, dirn[1] / length * self.vel)

            move_x, move_y = ((self.x + dirn[0]), (self.y + dirn[1]))

            self.x = move_x
            self.y = move_y

            if dirn[0] < 0 and not self.flipped:
                self.flipped = True
                for x, img in enumerate(self.imgs):
                    self.imgs[x] = pygame.transform.flip(img, True, False)

            # Go to next point
            if dirn[0] >= 0:  # moving right
                if dirn[1] >= 0:  # moving down
                    if self.x >= x2 and self.y >= y2:
                        self.path_pos += 1
                else:
                    if self.x >= x2 and self.y <= y2:
                        self.path_pos += 1
            else:  # moving left
                if dirn[1] >= 0:  # moving down
                    if self.x <= x2 and self.y >= y2:
                        self.path_pos += 1
                else:
                    if self.x <= x2 and self.y >= y2:
                        self.path_pos += 1
        except Exception as err:
            print(f"[ERROR] {err}.")

    def collide(self, x_pos, y_pos):
        """
        Returns if position has hit enemy.
        :param x_pos: int
        :param y_pos: int
        :return: Bool
        """
        if self.x + self.width >= x_pos >= self.x:
            if self.y + self.height >= y_pos >= self.y:
                return True
        return False

    def health(self, damage):
        """
        Removes health and returns if enemy is alive.
        :param damage: int
        :return: bool
        """
        self.curr_health -= damage
        if self.curr_health <= 0:
            return True
        return False
