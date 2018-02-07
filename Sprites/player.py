import pygame

"""
Represents the frog/turtle that the user plays as
"""
class Player(pygame.sprite.Sprite):
    WHITE = (255,255,255)
    FROG = (252,255,214)
    SHELL = (214,34,101)
    
    size = 40
    
    def __init__(self):
        super(Player, self).__init__()
        
        self.image = pygame.Surface([Player.size,Player.size])
        self.image.fill(Player.WHITE)
        self.image.set_colorkey(Player.WHITE)
        self.rect = self.image.get_rect()
        self.change_x = 0
        self.change_y = 0
        self.change_log = 3
            
        pygame.draw.circle(self.image, Player.FROG, [Player.size/2,Player.size/8], Player.size/8)
        pygame.draw.line(self.image, Player.FROG, [Player.size/10,Player.size/10],[Player.size,Player.size], Player.size/5)
        pygame.draw.line(self.image, Player.FROG, [Player.size*9/10,Player.size/10],[0,Player.size], Player.size/5)
        pygame.draw.ellipse(self.image, Player.SHELL, [Player.size/8,Player.size/4,Player.size*3/4,Player.size*3/4])
    
    """
    Moves the player by the amount contained in self.change_x
    """    
    def update(self):
        self.rect.x += self.change_x        
    
    """
    Prepares the player to move left
    """
    def go_left(self):
        if self.rect.x < 0: #doesn't let player go off screen
            self.rect.x = 0
            
        else:
            self.change_x = -3
        
        self.image.fill(Player.WHITE)
        self.image.set_colorkey(Player.WHITE)
        pygame.draw.circle(self.image, Player.FROG, [6,20], 6)
        pygame.draw.line(self.image, Player.FROG, [4,4],[40,40], 7)
        pygame.draw.line(self.image, Player.FROG, [4,36],[40,0], 7)
        pygame.draw.ellipse(self.image, Player.SHELL, [10,5,30,30])
    
    """
    Prepares the player to move right
    """    
    def go_right(self, sw):
        if self.rect.x > (sw - 50):
            self.rect.x = sw - 50
            
        else:
            self.change_x = 3

        self.image.fill(Player.WHITE)
        self.image.set_colorkey(Player.WHITE)
        
        pygame.draw.circle(self.image, Player.FROG, [34,20], 6)
        pygame.draw.line(self.image, Player.FROG, [0,0],[36,36], 7)
        pygame.draw.line(self.image, Player.FROG, [0,40],[36,4], 7)
        pygame.draw.ellipse(self.image, Player.SHELL, [0,5,30,30])
    
    """
    Move the player forward
    """        
    def go_forward(self):
        self.image.fill(Player.WHITE)
        self.image.set_colorkey(Player.WHITE)
        
        pygame.draw.circle(self.image, Player.FROG, [20,6], 6)
        pygame.draw.line(self.image, Player.FROG, [4,4],[40,40], 7)
        pygame.draw.line(self.image, Player.FROG, [36,4],[0,40], 7)
        pygame.draw.ellipse(self.image, Player.SHELL, [5,10,30,30])
        
        self.rect.y -= 50
    
    """
    Stop the players movement
    """   
    def stop(self):
        self.change_x = 0          