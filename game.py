from Enemy.bosses import *
from Enemy.desert_enemies import *
from Enemy.field_enemies import *
from Enemy.graveyard_enemies import *
from Enemy.magic_enemies import *
from Enemy.moon_enemies import *
from Enemy.winter_enemies import *
from Enemy.fire_enemies import *
from menu import VerticalMenu
from Buildings.archer import ArcherTower
from Buildings.support import DamageTower, RangeTower, StoneTower
from button import PlayGameBtn, MusicBtn, PlayPauseBtn
import random
import pygame
import time

# Setup/initialization

bg = pygame.image.load("Game/Backgrounds/graveyard_bg.png")
bg = pygame.transform.scale(bg, (1350, 700))

width = bg.get_width()
height = bg.get_height()

pygame.init()
pygame.font.init()

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tower Defense Game")

# Music
music = pygame.mixer_music.load('Game/music3.mp3')
pygame.mixer_music.play(-1)

play = pygame.image.load("Game/Utils/button_sound.png")
play = pygame.transform.scale(play, (100, 100))

pause = pygame.image.load("Game/Utils/button_sound_off.png")
pause = pygame.transform.scale(pause, (100, 100))

# Play Pause Btn
play2 = pygame.image.load("Game/Utils/button_start.png")
play2 = pygame.transform.scale(play2, (100, 100))

pause2 = pygame.image.load("Game/Utils/button_pause.png")
pause2 = pygame.transform.scale(pause2, (100, 100))

# Archer/support tower set up
buy_archer = pygame.transform.scale(pygame.image.load(os.path.join("Game/Shop", "ico_7.png")).
                                    convert_alpha(), (75, 75))
buy_damage = pygame.transform.scale(pygame.image.load(os.path.join("Game/Shop", "ico_4.png")).
                                    convert_alpha(), (75, 75))
buy_range = pygame.transform.scale(pygame.image.load(os.path.join("Game/Buildings", "14.png")).
                                   convert_alpha(), (75, 75))
buy_stone = pygame.transform.scale(pygame.image.load(os.path.join("Game/Shop", "ico_9.png")).convert_alpha(), (75, 75))

attack_tower_names = ["archer"]
support_tower_names = ["range", "damage", "stone"]

side_img = pygame.transform.scale(pygame.image.load(os.path.join("Game/Shop/", "window_1.png"))
                                  .convert_alpha(), (120, 500))

# Clock
clock = pygame.time.Clock()

# Path for enemies
path = [(-10, 477),
        (0, 477), (171, 481), (315, 528), (464, 529), (631, 532), (802, 532), (846, 358), (673, 323), (533, 301),
        (513, 209),
        (491, 118), (661, 102), (826, 99), (1003, 100), (1179, 97), (1346, 96)]

# Waves in Skeleton, Monster, Bat, Goblin, SnowMan, Knight, MaskedMan, Yeti, Tree, Golem, Guard, SuperBoss (12 enemies)
waves = [  # 30 waves + 3 bonus rounds
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 2],  # for testing
    [20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # wave 1
    [30, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # wave 2
    [30, 20, 10, 0, 0, 0, 0, 0, 0, 0, 0],  # wave 3
    [50, 40, 20, 5, 0, 0, 0, 0, 0, 0, 0],  # wave 4
    [100, 20, 20, 20, 0, 0, 0, 0, 0, 0, 0],  # wave 5
    [0, 0, 0, 0, 30, 0, 0, 1, 0, 0, 0],  # wave 6 (winter special)
    [100, 40, 30, 20, 10, 2, 0, 0, 0, 0, 0],  # wave 7
    [100, 100, 50, 50, 30, 10, 0, 0, 0, 0, 0],  # wave 8
    [100, 100, 75, 75, 40, 20, 5, 0, 0, 0, 0],  # wave 9
    [0, 0, 0, 0, 0, 0, 0, 10, 10, 7, 7],  # wave 10 (boss round)
    [150, 100, 100, 100, 50, 50, 20, 0, 0, 0, 0],  # wave 11
    [150, 150, 150, 150, 40, 40, 40, 0, 0, 0, 0],  # wave 12
    [200, 200, 150, 150, 50, 50, 50, 0, 0, 0, 0],  # wave 13
    [200, 200, 150, 150, 50, 50, 50, 1, 1, 0, 0],  # wave 14
    [200, 200, 200, 200, 100, 75, 75, 2, 2, 1, 1],  # wave 15
    [200, 200, 200, 200, 100, 100, 100, 2, 2, 2, 2],  # wave 16
    [1000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # wave 17
    [300, 200, 200, 200, 150, 150, 100, 3, 3, 2, 2],  # wave 18
    [300, 200, 200, 200, 200, 200, 150, 4, 4, 4, 4],  # wave 19
    [0, 0, 0, 0, 0, 0, 0, 12, 12, 10, 10],  # wave 20 (boss round)
    [400, 300, 300, 300, 300, 300, 200, 5, 5, 5, 5],  # wave 21
    [400, 300, 300, 300, 300, 300, 300, 0, 0, 0, 0],  # wave 22
    [1300, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # wave 23
    [500, 300, 300, 300, 300, 300, 300, 5, 5, 5, 5],  # wave 24
    [100, 300, 300, 300, 300, 300, 300, 10, 10, 7, 7],  # wave 25
    [500, 400, 400, 400, 400, 400, 400, 7, 7, 7, 7],  # wave 26
    [0, 1300, 100, 0, 0, 0, 0, 0, 0, 0, 0],  # wave 27
    [600, 500, 500, 500, 500, 500, 500, 6, 6, 6, 6],  # wave 28
    [1700, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # wave 29
    [0, 0, 0, 0, 0, 0, 0, 50, 50, 50, 50],  # wave 30 (last before bonus)
    [2000, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0],  # bonus 1
    [700, 500, 500, 500, 500, 500, 500, 10, 10, 10, 10],  # bonus 2
    [0, 0, 0, 0, 0, 0, 0, 100, 100, 100, 100, 1],  # bonus 3
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],  # bonus 4
    [0, 0, 0, 0, 0, 0, 0, 20, 20, 20, 20, 5]
]


def point_to_line(tower):
    """
    Returns if you can place tower based on distance from.
    path
    :param tower: Tower class object
    :return: Bool
    """
    return True, tower


class MainLoop:
    def __init__(self):
        self.clicks = []
        self.running = True
        self.in_start = True
        self.money = 3000
        self.lives = 30
        self.wave = 1
        self.enemies = []
        self.path = path
        self.bg = bg
        self.timer = time.time()
        self.paused = True
        self.selected_tower = None
        self.attack_towers = []
        self.support_towers = []
        self.menu = VerticalMenu(width - side_img.get_width() + 70, 250, side_img)
        self.menu.add_btn(buy_archer, "buy_archer", 500)
        self.menu.add_btn(buy_damage, "buy_damage", 1000)
        self.menu.add_btn(buy_range, "buy_range", 1000)
        self.menu.add_btn(buy_stone, "buy_stone", 1500)
        self.moving_object = None
        self.curr_wave = waves[self.wave][:]
        self.pl_pa_btn = PlayPauseBtn(play2, pause2, 120, 600)
        self.music_btn = MusicBtn(play, pause, 20, 600)
        self.music = True
        self.font = pygame.font.SysFont("comicsans", 40, bold=True)
        self.msg_mode = False
        self.msg_clicked = False
        self.lose = False
        self.win = False

    def start_screen(self):
        """
        Start screen for tower defense game.
        :return: None
        """
        while self.in_start:
            for ev in pygame.event.get():
                if ev == pygame.QUIT:
                    pygame.quit()
                    break

            # Title
            logo = pygame.image.load("Game/Start Screen/logo2.png")
            win.blit(self.bg, (0, 0))
            win.blit(logo, (850 - width // 2, 400 - height // 2))

            # Show characters for a e s t h e t i c s
            en = pygame.image.load("Game/Enemies/Bosses/Golem/0_boss_run_000.png")
            win.blit(en, (450 - width // 2, 370 - height // 2))
            en2 = pygame.image.load("Game/Enemies/Bosses/Guard/0_boss_run_000.png")
            en2 = pygame.transform.flip(en2, True, False)
            win.blit(en2, (1150 - width // 2, 400 - height // 2))

            # Button to play
            btn1 = pygame.image.load("Game/Start Screen/button_play.png")
            start_screen_btn = PlayGameBtn(btn1, 1150 - width // 2, 720 - height // 2)

            start_screen_btn.draw(win)

            if pygame.mouse.get_pressed()[0] == 1:
                self.in_start = False
                self.msg_mode = True
                self.main()
                break

            pygame.display.update()

        self.main()

    def add_tower(self, name):
        x, y = pygame.mouse.get_pos()
        name_list = ["buy_archer", "buy_damage", "buy_range", "buy_stone"]
        object_list = [ArcherTower(x, y), DamageTower(x, y), RangeTower(x, y), StoneTower(x, y)]

        try:
            obj = object_list[name_list.index(name)]
            self.moving_object = obj
            obj.moving = True
        except Exception as err:
            print(f"[ERROR]: {str(err)}.")

    def enemy_wave(self):
        """
        Chooses the appropriate enemies to put on the screen.
        :return: list
        """
        if sum(self.curr_wave) == 0:
            if len(self.enemies) == 0:
                self.wave += 1
                self.curr_wave = waves[self.wave]
                self.paused = True
        else:
            wave_enemies = [Skeleton(), PurpleMonster(), Bat(), HammerGoblin(), SnowMan(), Knight(), MaskedMan(),
                            Yeti(), Tree(), Golem(), Guard(), SuperBoss()]

            for x in range(len(self.curr_wave)):
                if self.curr_wave[x] != 0:
                    self.enemies.append(wave_enemies[x])
                    self.curr_wave[x] = self.curr_wave[x] - 1
                    break

    def redraw_game_window(self):
        """
        Draws everything needed for the game onto the screen.
        :return: None
        """
        win.blit(self.bg, (0, 0))  # background

        # Buttons
        self.music_btn.draw(win)
        self.pl_pa_btn.draw(win)

        # draw placement rings
        if self.moving_object:
            for tower in self.attack_towers:
                tower.draw_placement(win)

            for tower in self.support_towers:
                tower.draw_placement(win)

            self.moving_object.draw_placement(win)

        # draw attack towers
        for tw in self.attack_towers:
            tw.draw(win)

        # draw support towers
        for tw in self.support_towers:
            tw.draw(win)

        # redraw selected tower
        if self.selected_tower:
            self.selected_tower.draw(win)

        # draw moving object
        if self.moving_object:
            self.moving_object.draw(win)

        # draw menu
        self.menu.draw(win)

        # Lives Left
        life = pygame.image.load("Game/Utils/heart.png")
        pygame.transform.scale(life, (70, 70))
        lives = self.font.render(str(self.lives), 2, (255, 255, 255))
        win.blit(lives, (1300, 20))
        win.blit(life, (1260, 15))
        # Money Left
        money = pygame.image.load("Game/Utils/star.png")
        pygame.transform.scale(money, (70, 70))
        money_text = self.font.render(str(self.money), 2, (255, 255, 255))
        win.blit(money_text, (1160, 20))
        win.blit(money, (1110, 15))
        # Wave Number
        background = pygame.image.load("Game/Utils/table_2.png")
        background = pygame.transform.scale(background, (150, 100))
        txt = self.font.render(f"Wave #{str(self.wave)}", 2, (0, 0, 0))
        win.blit(background, (10, 10))
        win.blit(txt, (16, 34))

#         for click in self.clicks:
#             pygame.draw.circle(win, (255, 0, 0), click, 5, 0)

        # draws enemies
        for en in self.enemies:
            en.draw(win)

        pygame.display.update()

    def lose_screen(self):
        """
        Screen that appears if one has lost.
        :return: None
        """
        while self.lose:
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    pygame.quit()
                    break

            # Title
            logo = pygame.image.load("Game/Start Screen/logo2.png")
            win.blit(self.bg, (0, 0))
            win.blit(logo, (850 - width // 2, 400 - height // 2))

            # You lose logo
            lose_img = pygame.image.load("Game/Utils/header_failed.png")
            win.blit(lose_img, (450, 370))

            # Best wave
            background = pygame.image.load("Game/Utils/table.png")
            background = pygame.transform.scale(background, (250, 100))
            txt = self.font.render(f"Best Wave #{str(self.wave)}", 2, (255, 255, 255))
            win.blit(background, (520, 570))
            win.blit(txt, (533, 606))

            pygame.display.update()

        pygame.quit()

    def win_screen(self):
        """
        If player completes all the levels.
        :return: None
        """
        while self.win:
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    break

            # Title
            logo = pygame.image.load("Game/Start Screen/logo2.png")
            win.blit(self.bg, (0, 0))
            win.blit(logo, (850 - width // 2, 400 - height // 2))

            # You win logo
            lose_img = pygame.image.load("Game/Utils/header_win.png")
            win.blit(lose_img, (450, 370))

        pygame.quit()

    def main(self):
        """
        Main loop of the game.
        :return: None
        """
        while self.running:

            clock.tick(700)

            pos = pygame.mouse.get_pos()

            # check for moving object
            if self.moving_object:
                self.moving_object.move_tower(pos[0], pos[1])
                tower_list = self.attack_towers[:] + self.support_towers[:]
                collide = False
                for tower in tower_list:
                    if tower.collide_other_tower(self.moving_object):
                        collide = True
                        tower.place_color = (255, 0, 0, 100)
                        self.moving_object.place_color = (255, 0, 0, 100)
                    else:
                        tower.place_color = (0, 0, 255, 100)
                        if not collide:
                            self.moving_object.place_color = (0, 0, 255, 100)

            # Music Button & Playing Music
            if pygame.mouse.get_pressed()[0] == 1 or pygame.mouse.get_pressed()[1] == 1 or \
                    pygame.mouse.get_pressed()[2] == 1:
                if self.music_btn.clicked(pos[0], pos[1]):
                    self.music = not self.music
                    self.music_btn.music = self.music
                    if self.music:
                        pygame.mixer_music.unpause()
                    else:
                        pygame.mixer_music.pause()

            # Main event loop
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    pygame.quit()
                    break

                if ev.type == pygame.MOUSEBUTTONUP:
                    # if you're moving an object and click
                    if self.moving_object:
                        not_allowed = False
                        tower_list = self.attack_towers[:] + self.support_towers[:]
                        for tower in tower_list:
                            if tower.collide_other_tower(self.moving_object):
                                not_allowed = True

                        if not not_allowed and point_to_line(self.moving_object):
                            if self.moving_object.name in attack_tower_names:
                                self.attack_towers.append(self.moving_object)
                            elif self.moving_object.name in support_tower_names:
                                self.support_towers.append(self.moving_object)

                            self.moving_object.moving = False
                            self.moving_object = None

                    else:
                        # look if you click on side menu
                        side_menu_button = self.menu.get_clicked(pos[0], pos[1])
                        if side_menu_button:
                            cost = self.menu.get_item_cost(side_menu_button)
                            if self.money >= cost:
                                self.money -= cost
                                self.add_tower(side_menu_button)

                        # look if you clicked on attack tower or support tower
                        btn_clicked = None
                        if self.selected_tower:
                            btn_clicked = self.selected_tower.menu.get_clicked(pos[0], pos[1])
                            if btn_clicked:
                                cost = self.selected_tower.get_upgrade_cost()
                                if self.money >= cost:
                                    self.money -= cost
                                    self.selected_tower.upgrade()

                        if not btn_clicked:
                            for tw in self.attack_towers:
                                if tw.click(pos[0], pos[1]):
                                    tw.selected = True
                                    self.selected_tower = tw
                                else:
                                    tw.selected = False

                            # look if you clicked on support tower
                            for tw in self.support_towers:
                                if tw.click(pos[0], pos[1]):
                                    tw.selected = True
                                    self.selected_tower = tw
                                else:
                                    tw.selected = False

            # Play Pause
            if pygame.mouse.get_pressed()[0] == 1 or pygame.mouse.get_pressed()[1] == 1 or \
                    pygame.mouse.get_pressed()[2] == 1:
                if self.pl_pa_btn.clicked(pos[0], pos[1]):
                    self.paused = not self.paused
                    self.pl_pa_btn.paused = self.paused

            # If lose the game
            if self.lives <= 0:
                self.lose = True
                self.lives = 15
                self.money = 2000
                self.enemies = []
                self.support_towers = []
                self.attack_towers = []
                print("[END] You Lose, no more lives!")
                self.lose_screen()

            # If you beat the game
            if self.wave == 34:
                self.win = True
                self.lives = 15
                self.money = 2000
                self.enemies = []
                self.support_towers = []
                self.attack_towers = []
                print("[END] You Win, congrats!")
                self.win_screen()

#             keys = pygame.key.get_pressed()  # for finding path

#             if keys[pygame.K_SPACE]:
#                 self.clicks.append(pos)
#                 print(self.clicks)

            # Generate and handle enemies
            if not self.paused:
                if time.time() - self.timer >= random.randrange(1, 6) / 3:
                    self.timer = time.time()
                    self.enemy_wave()

            if not self.paused:
                en_to_del = []
                for en in self.enemies:
                    en.move()
                    if en.x < -15:
                        en_to_del.append(en)

                for enemy in en_to_del:
                    self.lives -= 1
                    self.enemies.remove(enemy)

                # loop through attack towers
                for tw in self.attack_towers:
                    self.money += tw.attack(self.enemies)

                # loop through attack towers
                for tw in self.support_towers:
                    tw.support(self.attack_towers)

            self.redraw_game_window()

        pygame.quit()
