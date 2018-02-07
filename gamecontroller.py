import pygame
from Sprites.player import Player
from Sprites.road import Road
from Sprites.water import Water
import random

"""
Frogger Game Controller
"""
class GC():
    debugMode = True
    
    NAME = "Frogger"
    
    SCREEN_WIDTH = 1400
    SCREEN_HEIGHT = 1000
    
    NUM_SURFACES = 20
    PLAYER_HEIGHT_LIMIT = 3 #spaces plaer can move before world moves
    
    SURF_HEIGHT = SCREEN_HEIGHT/NUM_SURFACES
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
    
    FRAME_RATE = 60
    
    """
    Initializes the game's data
    """
    def __init__(self):
        pygame.init()
        
        self.splash = pygame.mixer.Sound("Audio/splash.wav")
        self.honk = pygame.mixer.Sound("Audio/honk.wav")
        self.theme = pygame.mixer.Sound("Audio/bongos.wav")
        
        self.screen = pygame.display.set_mode((GC.SCREEN_WIDTH, GC.SCREEN_HEIGHT))
        
        pygame.display.set_caption(GC.NAME)
        
        # Used to manage how fast the screen updates
        self.clock = pygame.time.Clock()
        
        self.done = False #loop until the user clicks the close button

        self.f = open("highscore.dat", "r+")
        self.highscore = int(self.f.read())
        
        self.playerList = pygame.sprite.Group()
        self.spriteList = pygame.sprite.Group()
        self.waters = pygame.sprite.Group()
        self.logs = pygame.sprite.Group()
        self.cars = pygame.sprite.Group()
        self.surfaces = pygame.sprite.Group()
    
    """
    Contains the main game loop, will continue while done is set False
    """                    
    def play(self):
        while not self.done:
            self.theme.play() #bongos
            self.gameOver = False #resets when player loses
            self.score = 0
            self.player = Player()
            self.playerList.add(self.player)
            self.spriteList.add(self.player)
            
            for yLoc in range(-3*GC.SURF_HEIGHT, GC.SCREEN_HEIGHT - 2*GC.SURF_HEIGHT, GC.SURF_HEIGHT):
                self.getNewSurface(yLoc) 
                yLoc += GC.SURF_HEIGHT
            
            self.player.rect.x = GC.SCREEN_WIDTH/2 - Player.size/2 #start position
            self.player.rect.y = GC.SCREEN_HEIGHT - 50

            while not self.gameOver:
                self.processInputs()   
                self.processLogic()
                self.draw()
            self.spriteList.empty()
            self.playerList.empty()
            self.logs.empty()
            self.cars.empty()
            self.surfaces.empty()
            self.waters.empty()
            
            self.clock.tick(GC.FRAME_RATE)
        self.f.close()
        pygame.quit()
    
    """
    Process the user's input
    Increments the score every time the player moves forward
    In Use:
        Escape: quit
        Arrows: move
    """    
    def processInputs(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
                self.gameOver = True
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.done = True
                    self.gameOver = True

                #single step up but smooth R/L
                elif event.key == pygame.K_RIGHT:
                    self.player.go_right(GC.SCREEN_WIDTH)
                elif event.key == pygame.K_LEFT:
                    self.player.go_left()
                    
                elif event.key == pygame.K_UP: #add score on up arrow
                    self.player.go_forward()
                    self.score += 1
                    if self.score > self.highscore:
                        highscore = self.score
                        self.f.seek(0)
                        self.f.truncate()
                        self.f.write(str(highscore))

            elif event.type == pygame.KEYUP: #stop on key up
                self.player.stop()
    
    """
    Contains all the game logic that does not directly depend upon user input
    """
    def processLogic(self):
        if self.player.rect.x < 0:
            self.player.rect.x = 0
        elif self.player.rect.x > GC.SCREEN_WIDTH - Player.size:
            self.player.rect.x = GC.SCREEN_WIDTH - Player.size

        if self.player.rect.y < GC.SCREEN_HEIGHT - 3*GC.SURF_HEIGHT: #moves the world if player moves above a point
            self.shiftWorld()           
        
        self.logs.update(GC.SCREEN_WIDTH)
        self.cars.update(GC.SCREEN_WIDTH)
        self.playerList.update()

        #Check For Loss
        water_hit = pygame.sprite.spritecollide(self.player, self.waters, False)  #check for collisions with car, log, water
        log_hit = pygame.sprite.spritecollide(self.player, self.logs, False) 
        car_hit = pygame.sprite.spritecollide(self.player, self.cars, False)
        
        if len(log_hit) > 0:   #moves with the log you are on
            log = log_hit[0]
            self.player.rect.x -= log.speed

        elif len(water_hit) != 0 and len(log_hit) == 0: #lose if you hit a car
            self.gameOver = True
            self.splash.play()
        elif len(car_hit) != 0:
            self.gameOver = True
            self.honk.play()
    
    """
    Puts a new surface of random type to y
    @param y: the y position to set the new surface
    """
    def getNewSurface(self, y):    
        sType = random.randrange(3)
        surface = -1
        if sType == 0:
            surface = Water(GC.SCREEN_WIDTH, GC.SURF_HEIGHT)
            self.surfaces.add(surface)
            self.waters.add(surface)
            self.logs.add(surface.logs)
        elif sType == 1:
            surface = Road(GC.SCREEN_WIDTH, GC.SURF_HEIGHT)
            self.surfaces.add(surface)
            self.cars.add(surface.cars)
        else:
            return surface
        surface.rect.y = y
        surface.rect.x = 0
        surface.update()
    
    """
    Scrolls the world by one surface height
    Deletes any surface that goes off screen and initializes a new, random one
    @param delY: the number of pixels to shift the world
    """    
    def shiftWorld(self):
        delY = -(self.player.rect.y - GC.SCREEN_HEIGHT + GC.PLAYER_HEIGHT_LIMIT*GC.SURF_HEIGHT)
        self.player.rect.y = GC.SCREEN_HEIGHT - GC.PLAYER_HEIGHT_LIMIT*GC.SURF_HEIGHT
        
        for s in self.surfaces:
            s.rect.y += delY
            
            if s.rect.y > self.player.rect.y + 2 * GC.SURF_HEIGHT:
                s.delete()
                s.kill()
            
        self.getNewSurface(self.player.rect.y - GC.SCREEN_HEIGHT - GC.SURF_HEIGHT)
                
        self.surfaces.update()
    
    """
    Draws all the sprites and the score to the screen
    """    
    def draw(self):    
        if not self.gameOver:
            self.screen.fill(GC.GREEN)
            self.surfaces.draw(self.screen)
            self.logs.draw(self.screen)
            self.cars.draw(self.screen)
            self.playerList.draw(self.screen)
            
            font = pygame.font.SysFont('Calibri', 40, True, False)
            scoreText = font.render("Score: " + str(self.score) + "  Highscore: " + str(self.highscore), True, GC.WHITE)
            self.screen.blit(scoreText, [5,5])      
    
        pygame.display.flip()       