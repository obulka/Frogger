import pygame
import random
from log import Log

"""
Water surface type
"""
class Water(pygame.sprite.Sprite):
    BLUE = (70,0,222)
    
    def __init__(self, width, height):
        super(Water, self).__init__()
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()
        self.image.fill(Water.BLUE)
        
        self.logs = pygame.sprite.Group()
        self.logSeparation = random.randrange(80,400)
        self.speed = random.randrange(-3,3) #makes logs go at different speeds
        
        if self.speed == 0:
            self.speed = random.randrange(-1,2,2)
                     
        for d in range(0, width, self.logSeparation): #makes logs
            log = Log(self.speed)
            log.rect.y = self.rect.y
            log.rect.x = d
            
            self.logs.add(log)
    
    """
    Deletes all entry's to self.logs
    """        
    def delete(self):
        for log in self.logs:
            log.kill()
    
    """
    Updates the positions of the logs floating on this water to move as it scrolls
    """     
    def update(self):
        for log in self.logs:
            log.rect.y = self.rect.y