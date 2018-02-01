import random
import pygame

BROWN = (107,45,0)
SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 1000

class Log(pygame.sprite.Sprite):
    """DRAW A LOG"""
    def __init__(self, speed):
        super(Log, self).__init__()
        self.speed = speed   
        self.image = pygame.Surface([80, 50])
        self.image.fill(BROWN)
        #self.image.set_colorkey(BROWN)
        self.rect = self.image.get_rect()
         
    def update(self):
        """MOVE THE LOG"""
        self.rect.x -= self.speed
        
        if self.rect.x <= -80:
            self.rect.x = random.randrange(SCREEN_WIDTH, SCREEN_WIDTH + 300)
            
        elif self.rect.x > SCREEN_WIDTH + 350:
            self.rect.x = -70