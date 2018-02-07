import pygame
import random
from log import Log

"""
Water surface type
"""
class Water(pygame.sprite.Sprite):
    BLUE = (70,0,222)
    
    max_log_speed = 3
    min_log_speed = 1
    
    def __init__(self, width, height):
        super(Water, self).__init__()
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()
        self.image.fill(Water.BLUE)
        
        self.logs = pygame.sprite.Group()
        self.logSeparation = random.randrange(height*8/5,height*8)
        
        self.speed = (random.uniform(0,1)*(Water.max_log_speed - Water.min_log_speed) + Water.min_log_speed)*(-1)**random.randrange(2) #random speed and direction
                     
        for d in range(0, width, self.logSeparation): #makes logs
            log = Log(self.speed, height)
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