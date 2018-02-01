import pygame

GREEN = (34,171,15)


class Level():
    def __init__(self, player):
        self.car_list = pygame.sprite.Group() #each list keeps track of their respective sprites
        self.player = player
        self.log_list = pygame.sprite.Group()
        self.grass_list = pygame.sprite.Group()
        self.road_list = pygame.sprite.Group()
        self.water_list = pygame.sprite.Group()
        self.world_shift = 0           
        
    def update(self):
        self.car_list.update() #moves each respective sprite
        self.log_list.update()
        self.grass_list.update()
        self.road_list.update()
        self.water_list.update() 
                        
    def draw(self, screen):
        screen.fill(GREEN) #draws each respective sprite
        self.grass_list.draw(screen)
        self.road_list.draw(screen)
        self.water_list.draw(screen)
        self.car_list.draw(screen)
        self.log_list.draw(screen)
        
    def shiftWorld(self, shift_y):
        self.world_shift += shift_y #shifts the whole screen down
        
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
