import pygame
from setting import *

class AlienLaser(pygame.sprite.Sprite):
    def __init__(self, alien_position, player_position):
        super().__init__()
        self.position = pygame.math.Vector2(alien_position)
        self.screen = pygame.display.get_surface()
        self.sprite_sheet = pygame.image.load("asset/Galaga_SpritesSheet.png").convert_alpha()
        self.image = self.sprite_sheet.subsurface(307, 118, SPRITE_SIZE, SPRITE_SIZE)
        self.image = pygame.transform.scale(self.image, (30, 30)) 
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect(center=alien_position)
        
        # Calcular la dirección hacia el jugador
        player_vector = pygame.math.Vector2(player_position)
        self.direction = (player_vector - self.position).normalize()
        
        self.velocity = 300

    def draw(self):
        self.screen.blit(self.image, self.rect)
    
    def update(self, dt):
        self.position += self.direction * self.velocity * dt
        self.rect.center = self.position
        if self.rect.y > HEIGHT or self.rect.y < 0 or self.rect.x > WIDTH or self.rect.x < 0:
            self.kill()