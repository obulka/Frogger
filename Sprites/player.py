import pygame

"""
Represents the frog/turtle that the user plays as
"""
class Player(pygame.sprite.Sprite):
    WHITE = (255,255,255)
    FROG = (252,255,214)
    SHELL = (214,34,101)
    
    def __init__(self, surface_height):
        super(Player, self).__init__()
        
        self.change_x = 0
        self.change_y = 0
        self.change_log = 3
        
        self.rotation = 0 #track the player rotation
        self.surface_height = surface_height
        self.size = self.surface_height*4/5
                
        self.image = pygame.Surface([self.size,self.size])
        self.image.fill(Player.WHITE)
        self.image.set_colorkey(Player.WHITE)
        self.rect = self.image.get_rect()
        
        #draw code 
        pygame.draw.circle(self.image, Player.FROG, [self.size/2,self.size/8], self.size/8)
        pygame.draw.line(self.image, Player.FROG, [self.size/10,self.size/10],[self.size,self.size], self.size/5)
        pygame.draw.line(self.image, Player.FROG, [self.size*9/10,self.size/10],[0,self.size], self.size/5)
        pygame.draw.ellipse(self.image, Player.SHELL, [self.size/8,self.size/4,self.size*3/4,self.size*3/4])
    
    """
    Rotates the image of our player by angle ccw
    @param angle: the angle in degrees to rotate counter clockwise
    """
    def rot_center(self, angle):
        self.rotation += angle
        
        orig_rect = self.image.get_rect()
        rot_image = pygame.transform.rotate(self.image, angle)
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        self.image = rot_image.subsurface(rot_rect).copy()
    
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

        if self.rotation != 90:
            self.rot_center(90 - self.rotation)
    
    """
    Prepares the player to move right
    """    
    def go_right(self, sw):
        if self.rect.x > (sw - self.surface_height):
            self.rect.x = sw - self.surface_height
            
        else:
            self.change_x = 3

        if self.rotation != -90:
            self.rot_center(-(90 + self.rotation))
        
    """
    Move the player forward
    """        
    def go_forward(self):
        self.rect.y -= self.surface_height
        
        if self.rotation != 0:
            self.rot_center(-self.rotation)
    
    """
    Stop the players movement
    """   
    def stop(self):
        self.change_x = 0          