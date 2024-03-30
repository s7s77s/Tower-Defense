import pygame
import os
import sys
from random import randint

pygame.init()
current_path = os.path.dirname(__file__)
os.chdir(current_path)
WIDTH = 1280
HEIGHT = 800
FPS = 60
sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption('TD')
lvlgame = 1

from load import *


def drawMaps(nameFile):
    maps = []
    source = "game_lvl/" + str(nameFile)
    with open(source, "r") as file:
        for i in range(0, 10):
            maps.append(file.readline().replace("\n", "").split(",")[0: -1])

    pos = [0, 0]
    for i in range(0, len(maps)):
        pos[1] = i * 80
        for j in range(0, len(maps[0])):
            pos[0] = 80 * j
            if maps[i][j] == '1':
                bush = Block(bush_image, pos)
                bush_group.add(bush)
            if maps[i][j] == '2':
                grass = Block(grass_image, pos)
                grass_group.add(grass)
            if maps[i][j] == '3':
                bush_lite = Block(bush_tower_image, pos)
                bush_tower_group.add(bush_lite)
            if maps[i][j] == '4':
                bottom = Edit_dir_tile(bottom_image, pos, 'bottom')
                edit_dir_group.add(bottom)
            if maps[i][j] == '6':
                right = Edit_dir_tile(rigth_image, pos, 'right')
                edit_dir_group.add(right)
            if maps[i][j] == '7':
                top = Edit_dir_tile(top_image, pos, 'top')
                edit_dir_group.add(top)


class Enemy(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.dir = 'right'
        self.speedx = 2
        self.speedy = 0

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if pygame.sprite.spritecollide(self, edit_dir_group, False):
            tile = pygame.sprite.spritecollide(self, edit_dir_group, False)[0]
            if abs(self.rect.centerx - tile.rect.centerx) <= 5 and abs(self.rect.centery - tile.rect.centery) <= 5:
                self.dir = tile.dir
        if self.dir == 'right':
            self.speedx = 2
            self.speedy = 0
            self.image = pygame.transform.rotate(enemy_image, 0)
        if self.dir == 'top':
            self.speedy = -2
            self.speedx = 0
            self.image = pygame.transform.rotate(enemy_image, 90)
        if self.dir == 'bottom':
            self.speedy = 2
            self.speedx = 0
            self.image = pygame.transform.rotate(enemy_image, 260)


class Block(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]


class Edit_dir_tile(pygame.sprite.Sprite):
    def __init__(self, image, pos, dir):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.dir = dir


class Spawn():
    def __init__(self):
        self.timer_spawn = 0

    def update(self):
        self.timer_spawn += 1
        if self.timer_spawn / FPS > 1:
            enemy = Enemy(enemy_image, (-70, 570))
            enemy_group.add(enemy)
            self.timer_spawn = 0


class TowerB(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect
        self.rect.x = pos[0]
        self.rect.y = pos[0]
        self.buy = False
        self.timer_click = 0


def lvl_game():
    sc.fill('gray')
    bush_group.update()
    bush_group.draw(sc)
    bush_tower_group.update()
    bush_tower_group.draw(sc)
    grass_group.update()
    grass_group.draw(sc)
    edit_dir_group.update()
    edit_dir_group.draw(sc)
    enemy_group.update()
    enemy_group.draw(sc)
    sc.blit(panel_image, (1, 700))
    spawn.update()
    pygame.display.update()


def restart():
    global edit_dir_group, bush_group, bush_tower_group, grass_group, enemy_group, spawn, towerb_group
    bush_group = pygame.sprite.Group()
    bush_tower_group = pygame.sprite.Group()
    grass_group = pygame.sprite.Group()
    enemy_group = pygame.sprite.Group()
    edit_dir_group = pygame.sprite.Group()
    spawn = Spawn()
    towerb_group = pygame.sprite.Group()


restart()
drawMaps('1.txt')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    lvl_game()
    clock.tick(FPS)
