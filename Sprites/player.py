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
        
        self.change_x = 0
        self.change_y = 0
        self.change_log = 3
        
        self.rotation = 0 #track the player rotation
        
        self.image = pygame.Surface([Player.size,Player.size])
        self.image.fill(Player.WHITE)
        self.image.set_colorkey(Player.WHITE)
        self.rect = self.image.get_rect()
        
        #draw code 
        pygame.draw.circle(self.image, Player.FROG, [Player.size/2,Player.size/8], Player.size/8)
        pygame.draw.line(self.image, Player.FROG, [Player.size/10,Player.size/10],[Player.size,Player.size], Player.size/5)
        pygame.draw.line(self.image, Player.FROG, [Player.size*9/10,Player.size/10],[0,Player.size], Player.size/5)
        pygame.draw.ellipse(self.image, Player.SHELL, [Player.size/8,Player.size/4,Player.size*3/4,Player.size*3/4])
    
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
        if self.rect.x > (sw - 50):
            self.rect.x = sw - 50
            
        else:
            self.change_x = 3

        if self.rotation != -90:
            self.rot_center(-(90 + self.rotation))
        
    """
    Move the player forward
    """        
    def go_forward(self):
        self.rect.y -= 50
        
        if self.rotation != 0:
            self.rot_center(-self.rotation)
    
    """
    Stop the players movement
    """   
    def stop(self):
        self.change_x = 0          