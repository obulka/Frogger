import pygame

GREEN = (34,171,15)
BLUE = (70,0,222)
GRAY = (74,74,74)

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 1000

class Water(pygame.sprite.Sprite):
    """BASIC WATER"""
    def __init__(self):
        super(Water, self).__init__()
        
        self.image = pygame.Surface([SCREEN_WIDTH, 50]) 
        self.image.fill(BLUE)
        
        self.rect = self.image.get_rect()
        
         
        
class Road(pygame.sprite.Sprite):
    """BASIC ROAD"""
    def __init__(self):
        super(Road, self).__init__()
        
        self.image = pygame.Surface([SCREEN_WIDTH, 50])
        self.image.fill(GRAY)
        
        self.rect = self.image.get_rect()
            
 
class Grass(pygame.sprite.Sprite):
    """BASIC GRASS"""
    def __init__(self):
        super(Grass, self).__init__()
        
        self.image = pygame.Surface([SCREEN_WIDTH, 50])
        self.image.fill(GREEN)
        
        self.rect = self.image.get_rect()