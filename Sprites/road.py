import pygame
import random
from car import Car

"""
Road surface type
"""
class Road(pygame.sprite.Sprite):
    GRAY = (74,74,74)
    
    def __init__(self, width, height):
        super(Road, self).__init__()
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()
        self.image.fill(Road.GRAY)
        
        self.cars = pygame.sprite.Group()
        self.speed = random.randrange(-3,3) #gives cars different speeds
        self.carSeparation = random.randrange(190,400) # gives a distance between cars
        
        if self.speed == 0:
            self.speed = random.randrange(-1,2,2)
        
        for d in range(0, width, self.carSeparation): #makes some cars
            car = Car(self.speed)
            car.rect.y = self.rect.y
            car.rect.x = d
            
            self.cars.add(car)
    
    """
    Deletes all entry's to self.cars
    """
    def delete(self):
        for car in self.cars:
            car.kill()
    
    """
    Updates the positions of the cars driving on this road to follow the road as it scrolls
    """               
    def update(self):
        for car in self.cars:
            car.rect.y = self.rect.y