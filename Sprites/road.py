import pygame
import random
from car import Car

"""
Road surface type
"""
class Road(pygame.sprite.Sprite):
    GRAY = (74,74,74)
    
    max_car_speed = 3
    min_car_speed = 1
    
    def __init__(self, width, height):
        super(Road, self).__init__()
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()
        self.image.fill(Road.GRAY)
        
        self.cars = pygame.sprite.Group()
        
        self.speed = (random.uniform(0,1)*(Road.max_car_speed - Road.min_car_speed) + Road.min_car_speed)*(-1)**random.randrange(2) #random speed and direction
        self.carSeparation = random.randrange(190,400) # gives a distance between cars
        
        for d in range(0, width, self.carSeparation): #makes some cars
            car = Car(self.speed, height)
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