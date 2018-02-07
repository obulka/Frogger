import random
import pygame

"""
Represents a log that allows the user to cross water
"""
class Log(pygame.sprite.Sprite):
    BROWN = (107,45,0)
    
    """
    Initialize a log
    @param speed: the speed in pixels/frame of the car
    """
    def __init__(self, speed, surface_height):
        super(Log, self).__init__()
        self.speed = speed
        self.length = surface_height*8/5  
        self.image = pygame.Surface([self.length, surface_height])
        self.image.fill(Log.BROWN)
        #self.image.set_colorkey(BROWN)
        self.rect = self.image.get_rect()
    
    """
    Moves the log at a rate of self.speed
    The log will loop back if it goes off screen
    @param sw: the screen width in pixels
    """     
    def update(self, sw):
        self.rect.x -= self.speed
        
        if self.rect.x <= -self.length:
            self.rect.x = sw
            
        elif self.rect.x > sw + self.length:
            self.rect.x = -70