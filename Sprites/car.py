import pygame

"""
Represents a hazardous car
"""
class Car(pygame.sprite.Sprite):
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    TURQ = (0,191,172)
    PURP = (174,0,255)
    WINDOW = (0,0,255)
    
    """
    Initialize a race car, a different image will display depending
    on the direction of travel
    @param speed: the speed in pixels/frame of the car
    """
    def __init__(self, speed, surface_height):
        super(Car, self).__init__()
        self.speed = speed
        self.length = surface_height*7/5
        self.image = pygame.Surface([self.length,surface_height])
        self.image.fill(Car.WHITE)
        self.image.set_colorkey(Car.WHITE)
        self.rect = self.image.get_rect()
        
        self.colour = Car.TURQ if self.speed < 0 else Car.PURP

        #draw code                    
        pygame.draw.ellipse(self.image, self.colour, [0 ,surface_height*9/25,self.length,surface_height*3/10])
        pygame.draw.rect(self.image, self.colour, [0,surface_height*6/25,self.length/14,surface_height*13/25])
        pygame.draw.ellipse(self.image, Car.WINDOW, [self.length/2,surface_height*2/5,self.length*4/35,surface_height/5])
        pygame.draw.rect(self.image, Car.BLACK, [self.length*53/70, surface_height*13/50, self.length*6/35, surface_height*3/25])
        pygame.draw.rect(self.image, Car.BLACK, [self.length*53/70, surface_height*31/50, self.length*6/35, surface_height*3/25])
        pygame.draw.rect(self.image, Car.BLACK, [self.length/14, surface_height/5, self.length*13/70, surface_height*9/50])
        pygame.draw.rect(self.image, Car.BLACK, [self.length/14, surface_height*31/50, self.length*13/70, surface_height*9/50])
        
        #point in the direction of travel
        if self.speed > 0:        
            orig_rect = self.image.get_rect()
            rot_image = pygame.transform.rotate(self.image, 180)
            rot_rect = orig_rect.copy()
            rot_rect.center = rot_image.get_rect().center
            self.image = rot_image.subsurface(rot_rect).copy()  
    
    """
    Moves the car at a rate of self.speed
    The car will loop back if it goes off screen
    @param sw: the screen width in pixels
    """       
    def update(self, sw):
        self.rect.x -= self.speed
        
        if self.rect.x <= -self.length:
            self.rect.x = sw + self.length
            
        elif self.rect.x > sw + self.length:
            self.rect.x = -self.length
            