from level import Level
import random
from surfaces import Water, Grass, Road
from log import Log
from car import Car

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 1000

class Level_01(Level):
    def __init__(self, player):
        Level.__init__(self, player)
        
        self.level_limit = -10000 #get here to win
        
        level = []
        
        for y in range(-10000, SCREEN_HEIGHT - 99, 50): 
            level.append([SCREEN_WIDTH, 50, 0, y])  #gets the y cooridinates of each surface
            
        for section in level:
            sType = random.randrange(3) #assigns a type of surface to each y cooridinate
            
            """WATER"""
            if sType == 0:
                logSeparation = random.randrange(80,400)
                speed = random.randrange(-3,3) #makes logs go at different speeds
                surface = Water()  #makes water
                
                if speed == 0:
                    speed = random.randrange(-1,2,2)
                    
                surface.rect.y = section[3] 
                surface.player = self.player
                self.water_list.add(surface)
                
                for d in range(0, SCREEN_WIDTH, logSeparation): #makes logs
                    log = Log(speed)
                    log.rect.y = surface.rect.y
                    log.rect.x = d
                    
                    self.log_list.add(log)                     
                                
                    """ROAD"""
            elif sType == 1:
                speed = random.randrange(-3,3) #gives cars different speeds
                carSeparation = random.randrange(190,400) # gives a distance between cars
                surface = Road() #makes a road
                
                if speed == 0:
                    speed = random.randrange(-1,2,2)
    
                surface.rect.y = section[3]
                surface.player = self.player
                self.road_list.add(surface) 
                
                for d in range(0, SCREEN_WIDTH, carSeparation): #makes some cars
                    car = Car(speed)
                    car.rect.y = surface.rect.y
                    car.rect.x = d
                    
                    self.car_list.add(car)                   
            
                    """GRASS"""    
            elif sType == 2:
                surface = Grass() #surface becomes grass
    
                surface.rect.y = section[3]
                surface.player = self.player
                self.grass_list.add(surface)