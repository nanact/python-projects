import pygame as game

game.init()

window = game.display.set_mode((400,300))

color = (30,30,30)

done = True

while done:
    game.draw.rect(window,color,game.Rect(30,30,30,60))
    game.display.flip()
    for event in game.event.get():
     if event.type == game.QUIT:
        done = False
        
    