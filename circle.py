import pygame as game

game.init()

window = game.display.set_mode((400,300))

color = (30,30,30)

done = True

window.fill((20,20,40))

Green = (0,255,0)

game.draw.circle(window,color,(100,100),50)

game.draw.circle(window,Green,(100,60),50,3)

game.display.update()

running = True

while running:
    for event in game.event.get():
     if event.type == game.QUIT:
        running = False