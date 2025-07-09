import pygame
from setting import *
from debug import *

class Laser (pygame.sprite.Sprite):
    
    def __init__(self, position ):
        super().__init__()
        #self.game = game
        self.position = position
        self.screen = pygame.display.get_surface()
        self.sprite_sheet = pygame.image.load ("asset/Galaga_SpritesSheet.png").convert_alpha()        
        self.image = self.sprite_sheet.subsurface ( 307, 118, SPRITE_SIZE, SPRITE_SIZE)
        self.image = pygame.transform.scale (self.image, (30, 30)) 
        self.image.set_colorkey ((0, 0, 0))
        self.rect= self.image.get_rect (center = position)
        self.position = pygame.math.Vector2(self.rect.midtop)
        self.direction = pygame.math.Vector2()
        self.velocity = 180
        self.direction.y = -2        
    
 
    
    def draw (self):
        self.screen.blit (self.image, self.position)
            
    def update (self, dt):
          
        self.position.y += self.direction.y * self.velocity * dt
        self.rect.y = round(self.position.y)
        if self.rect.y < -10:
            self.kill ()
       
       
        
    
    