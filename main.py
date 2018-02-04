#!/usr/bin/env python
import pygame
from player import Player
from level import Level

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 1000


#Colors
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (34,171,15)
BLUE = (70,0,222)
TURQ = (0,191,172)
PURP = (174,0,255)
GRAY = (74,74,74)
BROWN = (107,45,0)
FROG = (252,255,214)
SHELL = (214,34,101)
WINDOW = (0,0,255)

SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT) #screen size in pixels
FRAME_RATE = 60

pygame.init()

splash = pygame.mixer.Sound("splash.wav")
honk = pygame.mixer.Sound("honk.wav")
theme = pygame.mixer.Sound("bongos.wav")

screen = pygame.display.set_mode(SIZE)

pygame.display.set_caption("Frogger")

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


def main():
    done = False #loop until the user clicks the close button

    f = open("highscore.dat", "r+")
    highscore = int(f.read())

    while not done:
        #theme.play() #bongos

        gameOver = False #resets when player loses
        speed_x = 0
        score = 0

        player = Player(speed_x) 

        level = Level(player)

        spriteList = pygame.sprite.Group()
        player.level = level


        player.rect.x = SCREEN_WIDTH/2 - 25 #start position
        player.rect.y = SCREEN_HEIGHT - 50
        spriteList.add(player)
        
        while not gameOver:
            """THE MAGIC"""
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    gameOver = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        done = True
                        gameOver = True

                        """single step up but smooth R/L"""
                    elif event.key == pygame.K_RIGHT:
                        player.go_right()
                    elif event.key == pygame.K_LEFT:
                        player.go_left()
                    elif event.key == pygame.K_UP: #add score on up arrow
                        player.go_forward()
                        score += 1
                        if score > highscore:
                            highscore = score
                            f.seek(0)
                            f.truncate()
                            f.write(str(highscore))

                elif event.type == pygame.KEYUP: #stop on key up
                    player.stop()

        #---logic to follow---                
            if player.rect.x < 0:
                player.rect.x = 0
            elif player.rect.x > SCREEN_WIDTH - 40:
                player.rect.x = SCREEN_WIDTH - 40

            if player.rect.y < SCREEN_HEIGHT - 145: #moves the world if player moves above a point
                diff = player.rect.y - SCREEN_HEIGHT + 145
                player.rect.y = SCREEN_HEIGHT - 145
                level.shiftWorld(-diff)            

                player.level = level

            spriteList.update() #updates to move things
            level.update()

            #Check For Loss
            car_hit_list = pygame.sprite.spritecollide(player, level.car_list, False)  #check for collisions with car, log, water
            water_hit_list = pygame.sprite.spritecollide(player, level.water_list, False)
            log_hit_list = pygame.sprite.spritecollide(player, level.log_list, False) 

            if len(log_hit_list) > 0:   #moves with the log you are on
                log = log_hit_list[0]
                player.rect.x -= log.speed

            if len(car_hit_list) != 0: #lose if you hit a car
                gameOver = True 
                honk.play()

            elif len(water_hit_list) != 0 and len(log_hit_list) == 0: #if you are touching water and not a log you lose
                gameOver = True
                splash.play()
 
        #Draw 
            if not gameOver:
                level.draw(screen)
                spriteList.draw(screen)
                font = pygame.font.SysFont('Calibri', 40, True, False)
                scoreText = font.render("Score: " + str(score) + "  Highscore: " + str(highscore), True, WHITE)
                screen.blit(scoreText, [5,5])      
        
            pygame.display.flip()
 
        clock.tick(FRAME_RATE)
    f.close()
    pygame.quit()
  
    
if __name__ == "__main__":
    main()
