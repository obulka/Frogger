import pygame
import random
from surfaces import Water, Grass, Road
from log import Log
from car import Car

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 1000
SURF_HEIGHT = 50
SEC_OFFSET = 2*SURF_HEIGHT - 1
INITIAL_POS = -2*SURF_HEIGHT

GREEN = (34,171,15)


class Level():
    def __init__(self, player):
        self.car_list = pygame.sprite.Group() #each list keeps track of their respective sprites
        self.player = player
        self.log_list = pygame.sprite.Group()
        self.grass_list = pygame.sprite.Group()
        self.road_list = pygame.sprite.Group()
        self.water_list = pygame.sprite.Group()
        
        self.level = []
        
        for y in range(INITIAL_POS, SCREEN_HEIGHT, SURF_HEIGHT): 
            self.level.append([SCREEN_WIDTH, SURF_HEIGHT, 0, y])  #gets the y cooridinates of each surface
        
        for section in self.level:
            self.createSection(section)
        
    def createSection(self, section):
        sType = random.randrange(3) #assigns a type of surface to each y cooridinate
        
        if section[3] >= SCREEN_HEIGHT - SEC_OFFSET:
            sType = 2
        
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
        
    def update(self):
        self.car_list.update() #moves each respective sprite
        self.log_list.update()
        self.grass_list.update()
        self.road_list.update()
        self.water_list.update()
        
        for log in self.log_list:
            if log.rect.y > SCREEN_HEIGHT:
                log.rect.y = INITIAL_POS
        
        for car in self.car_list:
            if car.rect.y > SCREEN_HEIGHT:
                car.rect.y = INITIAL_POS
        
        for grass in self.grass_list:
            if grass.rect.y > SCREEN_HEIGHT:
                grass.rect.y = INITIAL_POS
        
        for water in self.water_list:
            if water.rect.y > SCREEN_HEIGHT:
                water.rect.y = INITIAL_POS
            
        for road in self.road_list:
            if road.rect.y > SCREEN_HEIGHT:
                road.rect.y = INITIAL_POS
                
                        
    def draw(self, screen):
        screen.fill(GREEN) #draws each respective sprite
        self.grass_list.draw(screen)
        self.road_list.draw(screen)
        self.water_list.draw(screen)
        self.car_list.draw(screen)
        self.log_list.draw(screen)
        
    def shiftWorld(self, shift_y):        
        for log in self.log_list:
            log.rect.y += shift_y
        
        for car in self.car_list:
            car.rect.y += shift_y
            
        for grass in self.grass_list:
            grass.rect.y += shift_y
        
        for water in self.water_list:
            water.rect.y += shift_y
            
        for road in self.road_list:
            road.rect.y += shift_y
