import pygame

WHITE = (255,255,255)
FROG = (252,255,214)
SHELL = (214,34,101)

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 1000

class Player(pygame.sprite.Sprite):
    """DRAW THE TURTLE FROG THING"""
    def __init__(self, speed):
        super(Player, self).__init__()
        
        self.image = pygame.Surface([40,40])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.change_x = 0
        self.change_y = 0
        self.change_log = 3
        self.level = None
        self.speed = speed
            
        pygame.draw.circle(self.image, FROG, [20,6], 6)
        pygame.draw.line(self.image, FROG, [4,4],[40,40], 7)
        pygame.draw.line(self.image, FROG, [36,4],[0,40], 7)
        pygame.draw.ellipse(self.image, SHELL, [5,10,30,30])
        
    def update(self):
        """MOVE THE TURTLE FROG THING"""
        self.rect.x += self.change_x        
    
    def go_left(self):
        if self.rect.x < 0: #doesn't let player go off screen
            self.rect.x = 0
            
        else:
            self.change_x = -3
        
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
           
        pygame.draw.circle(self.image, FROG, [6,20], 6)
        pygame.draw.line(self.image, FROG, [4,4],[40,40], 7)
        pygame.draw.line(self.image, FROG, [4,36],[40,0], 7)
        pygame.draw.ellipse(self.image, SHELL, [10,5,30,30])
        
    def go_right(self):
        if self.rect.x > (SCREEN_WIDTH - 50):
            self.rect.x = SCREEN_WIDTH - 50
            
        else:
            self.change_x = 3

        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        
        pygame.draw.circle(self.image, FROG, [34,20], 6)
        pygame.draw.line(self.image, FROG, [0,0],[36,36], 7)
        pygame.draw.line(self.image, FROG, [0,40],[36,4], 7)
        pygame.draw.ellipse(self.image, SHELL, [0,5,30,30])
            
    def go_forward(self):
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        
        pygame.draw.circle(self.image, FROG, [20,6], 6)
        pygame.draw.line(self.image, FROG, [4,4],[40,40], 7)
        pygame.draw.line(self.image, FROG, [36,4],[0,40], 7)
        pygame.draw.ellipse(self.image, SHELL, [5,10,30,30])
        
        self.rect.y -= 50
        
    def stop(self):
        self.change_x = 0          