import pygame as game  

game.init()

window = game.display.set_mode((600,500))

game.display.set_caption("My first game")

background_image = game.transform.scale(
    game.image.load("cookie catch.png").convert(),
    (600,500)
)


done = False

while not done:
    window.blit(background_image, (0,0))  
    for event in game.event.get():
        if event.type == game.QUIT:
            game.quit()

    game.display.flip()