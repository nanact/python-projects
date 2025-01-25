import pygame as game  

def main():
    game.init()
    screen_height = 400
    
    screen_width = 600
    
    screen = game.display.set_mode((screen_width,screen_height))
    
    game.display.set_caption("MY game")
    
    colour = {
        "red":game.Color("red"),
        "yellow":game.Color("yellow"),
        "green":game.Color("green"),
        "blue":game.Color("blue"),
        "white":game.Color("white")
    }
    
    current_color = colour["white"]
    
    x, y = 30,30
    
    spritewidth, spriteheight = 60, 60
    
    clock = game.time.Clock()
    
    done = False
    
    while not done:
        for event in game.event.get():
            if event.type == game.QUIT:
                done = True
                
            pressend = game.key.get_pressed()
            
            if pressend[game.K_LEFT]: x -= 3
            if pressend[game.K_RIGHT]: x += 3
            if pressend[game.K_UP]: y += 3
            if pressend[game.K_DOWN]: y -= 3
            
            x = min (max(0 , x) , screen_width - spritewidth)
            
            y = min(max(0, y), screen_height - spriteheight)
            
            if x == 0 : current_color = colour["blue"]
            
            elif x == screen_width - spritewidth: colour["red"]
            
            elif y == 0: colour["green"]
            
            elif y == screen_height - spriteheight: colour["yellow"]
            
            else: colour["white"]
            
            screen.fill((0,0,0))
            
            game.draw.rect(screen, current_color, (x , y , spritewidth, spriteheight))
            
            game.display.flip()
            
            clock.tick(90)
        game.quit()
        
main()
            
            