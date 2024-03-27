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
                bottom = Block(bottom_image, pos)
                bottom_group.add(bottom)
            if maps[i][j] == '5':
                left = Block(left_image, pos)
                left_group.add(left)
            if maps[i][j] == '6':
                right = Block(rigth_image, pos)
                right_group.add(right)
            if maps[i][j] == '7':
                top = Block(top_image, pos)
                top_group.add(top)


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


def lvl_game():
    sc.fill('gray')
    bush_group.update()
    bush_group.draw(sc)
    bottom_group.update()
    bottom_group.draw(sc)
    bush_tower_group.update()
    bush_tower_group.draw(sc)
    grass_group.update()
    grass_group.draw(sc)
    left_group.update()
    left_group.draw(sc)
    right_group.update()
    right_group.draw(sc)
    top_group.update()
    top_group.draw(sc)
    pygame.display.update()


def restart():
    global bottom_group, bush_group, bush_tower_group, grass_group, left_group, right_group, top_group
    bottom_group = pygame.sprite.Group()
    bush_group = pygame.sprite.Group()
    bush_tower_group = pygame.sprite.Group()
    grass_group = pygame.sprite.Group()
    left_group = pygame.sprite.Group()
    right_group = pygame.sprite.Group()
    top_group = pygame.sprite.Group()


restart()
drawMaps('1.txt')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    lvl_game()
    clock.tick(FPS)
