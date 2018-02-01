import pygame

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (34,171,15)
BLUE = (70,0,222)
TURQ = (0,191,172)
PURP = (174,0,255)
GRAY = (74,74,74)
BROWN = (107,45,0)
FROG = (252,255,214)
SHELL = (214,34,101)
WINDOW = (0,0,255)
SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 1000

class Car(pygame.sprite.Sprite):
    """DRAW A RACE CAR"""
    def __init__(self, speed):
        super(Car, self).__init__()
        self.speed = speed
        self.image = pygame.Surface([70,50])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        
        if self.speed > 0:  #draws purple cars going right and blue going left
            pygame.draw.ellipse(self.image, PURP, [0 ,18,70,15])
            pygame.draw.ellipse(self.image, WINDOW, [30,20,8,10])

            for i in range(13, 32, 18):
                pygame.draw.rect(self.image, BLACK, [12, i, 12, 6])
        
            for i in range(10, 32, 21):
                pygame.draw.rect(self.image, BLACK, [55, i, 13, 9])
        
            pygame.draw.rect(self.image, PURP, [65,12,5,26])     
            
        else:
            pygame.draw.ellipse(self.image, TURQ, [0 ,18,70,15])
            pygame.draw.ellipse(self.image, WINDOW, [35,20,8,10])

            for i in range(13, 32, 18):
                pygame.draw.rect(self.image, BLACK, [53, i, 12, 6])
        
            for i in range(10, 32, 21):
                pygame.draw.rect(self.image, BLACK, [5, i, 13, 9])
        
            pygame.draw.rect(self.image, TURQ, [0,12,5,26])   
            
    def update(self):
        """MOVE THE RACE CAR"""
        self.rect.x -= self.speed
        
        if self.rect.x <= -80:
            self.rect.x = SCREEN_WIDTH + 100
            
        elif self.rect.x > SCREEN_WIDTH + 101:
            self.rect.x = -70