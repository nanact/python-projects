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
BULLET_SPEED_Y = 30
BULLENT_SPEED_X = 30
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
    
bulletImg = game.image.load('bullet.png')

bulletX = 0

bulletY = PLAYER_START_Y

bulletX_change = 0

bulletY_change = BULLET_SPEED_Y

bullent_state = "ready"

score_value = 0

font = game.font.Font('freesansbold.ttf', 32)

textX = 10

textY = 10

over_font = game.font.Font('freesansbold.ttf', 64)

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))
    
def game_over_text():
    
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))
    
def player(x, y):
    screen.blit(playerIMG, (x, y))
    
def enemy(x, y, i):
    screen.blit(enemyIMG[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))
    
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((enemyX - bulletX) ** 2 + (enemyY - bulletY) ** 2)
    return distance < COLLSION_DISTANCE
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(Background, (0, 0))

    for event in game.event.get():
        if event.type == game.QUIT:
            running = False
            
        if event.type == game.KEYDOWN:
            if event.key == game.K_LEFT:
                playerX_change = -5
            if event.key == game.K_RIGHT:
                playerX_change = 5
            if event.key == game.K_SPACE and bullet_state == "ready":
                bulletX = playerX
                fire_bullet(bulletX, bulletY)
        if event.type == game.KEYUP and event.key in [game.K_LEFT, game.K_RIGHT]:
            playerX_change = 0
    playerX += playerX_change
    
    playerX = max(0, min(playerX , SCREEN_WIDTH - 64)) 
    
    for i in range(num_of_emenies):
        if enemyY[i] > 340:  
           for j in range(num_of_emenies):
            enemyY[j] = 2000
        game_over_text()
        break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0 or enemyX[i] >= SCREEN_WIDTH:
            enemyX_change[i] *= -1
            enemyY[i] += enemyY_change[i]
            
        if isCollision(enemyX[i], enemyY[i], playerX, playerY):
            bulletY = PLAYER_START_Y
            bullent_state = "ready"
            score_value += 1
            enemyX = random.randint(0, SCREEN_WIDTH- 64)
            enemyY[i] =  random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX)
            
        enemy(enemyx[i],enemyY[i],en)       
        
    if bulletY > 0:
        bulletY = PLAYER_START_Y
        bullent_state = "ready"
    elif bullent_state == "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change
        
    player(playerX,playerX)
    show_score(textX,textY)
    game.display.update()
            



    





    