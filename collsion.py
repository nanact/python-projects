import pygame as game
import random

SCREEN_WIDTH, SCREEN_HEIGHT = 500, 100

MOVEMENT_SPEED = 10

FONT_SIZE = 75

game.init()

background_image = game.transform.scale(game.image.load("download.jpeg"), (SCREEN_WIDTH, SCREEN_HEIGHT))

font = game.font.SysFont("Tixes how Roman",FONT_SIZE)

class Sprite(game.sprite.Sprite):
    
    def __init__(self, color, height, width):
        super().__init__()
        
        self.image = game.Surface([width, height])
        
        self.image.fill(game.Color("dodgerblue"))
        
        game.draw.rect(self.image, color, game.Rect(0, 0, width,height))
        
        self.rect = self.image.get_rect()
        
    def move(self, x_change, y_change):
        self.rect.x = max(
            min(self.rect.x + x_change, SCREEN_WIDTH - self.rect.width),0)
        self.rect.y = max(
            min(self.rect.y + y_change, SCREEN_HEIGHT - self.rect.width),0)
    
screen = game.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

game.display.set_caption("sprite collsion")

all_sprites = game.sprite.Group()

sprite1 = Sprite(game.Color("black"),20, 30)

sprite1.rect.x, sprite1.rect.y = random.randint(
    0,SCREEN_WIDTH - sprite1.rect.width), random.randint(
        0,SCREEN_HEIGHT-sprite1.rect.height)
all_sprites.add(sprite1)
sprite2 = Sprite(game.Color("red"),20, 30)

sprite2.rect.x, sprite2.rect.y = random.randint(
    0,SCREEN_WIDTH - sprite2.rect.width), random.randint(
        0,SCREEN_HEIGHT-sprite2.rect.height)
all_sprites.add(sprite2)

running, won = True, False
clock = game.time.Clock()

while running:
    for event in game.event.get():
        if event.type == game.QUIT or (event.type == game.KEYDOWN and event.key == game.K_x):
            running = False
            
    if not won:
       keys = game.key.get_pressed()
       x_change = (keys[game.K_RIGHT] - keys[game.K_LEFT]) * MOVEMENT_SPEED
       y_change = (keys[game.K_DOWN] - keys[game.K_UP]) * MOVEMENT_SPEED
       sprite1.move(x_change, y_change)
    
       if sprite1.rect.colliderect(sprite2.rect):
           all_sprites.remove(sprite2)
           won = True

    screen.blit(background_image,(0,0))
    all_sprites.draw(screen)

    if won:
       text = font.render("You win!", True, game.Color("black"))
       screen.blit(text,((SCREEN_WIDTH - text.get_width()) // 2,
       (SCREEN_HEIGHT - text.get_height()) // 2))
    game.display.flip()

    clock.tick(90)