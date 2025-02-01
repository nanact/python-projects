import math
import pygame as game
import random

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 600
PLAYER_START_X = 300
PLAYER_START_Y = 300
ENEMY_START_X_MIN = 50
ENEMY_START_X_MAX = 200
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 200
ENEMY_SPEED_X = 30
ENEMY_SPEED_Y = 30
BULLET_SPEED = 20
COLLSION_DISTANCE = 27

game.init()

screen = game.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

Background = game.image.load("background.png")

game.display.set_caption("Space_invader")

icon = game.image.load("icon.png")

game.display.set_icon(icon)

playerIMG = game.image.load("rocket.png")

playerX = PLAYER_START_X

playerY = PLAYER_START_Y

playerX_change = 0

enemyIMG = []
enemyY = []
enemyX = []
enemyX_change = []
enemyY_change = []
num_of_emenies = 0

for _i in range(num_of_emenies):
    enemyIMG.append(game.image.load("enemy.png"))
    enemyX.append(random.randint(0, SCREEN_WIDTH - 64)) 
    
    enemyY.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
    enemyX_change.append(ENEMY_SPEED_X)
    enemyY_change.append(ENEMY_SPEED_Y)
    
    

    