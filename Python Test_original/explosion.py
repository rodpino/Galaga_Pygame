import pygame
from setting import *

class Explosion(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.index = 0
        self.velocity_move = 1
        self.screen = pygame.display.get_surface()
        self.sprite_sheet = pygame.image.load("Python Test_original/asset/Galaga_SpritesSheet.png").convert_alpha()
        
        self.explosion_1 = self.sprite_sheet.subsurface(289, 1, SPRITE_SIZE_32, SPRITE_SIZE_32)
        self.explosion_2 = self.sprite_sheet.subsurface(323, 1, SPRITE_SIZE_32, SPRITE_SIZE_32)
        self.explosion_3 = self.sprite_sheet.subsurface(357, 1, SPRITE_SIZE_32, SPRITE_SIZE_32)
        self.explosion_4 = self.sprite_sheet.subsurface(391, 1, SPRITE_SIZE_32, SPRITE_SIZE_32)
        self.explosion_5 = self.sprite_sheet.subsurface(425, 1, SPRITE_SIZE_32, SPRITE_SIZE_32)
        
        self.explosion_1 = pygame.transform.scale(self.explosion_1, (EXPLOSION_SIZE))
        self.explosion_2 = pygame.transform.scale(self.explosion_2, (EXPLOSION_SIZE))
        self.explosion_3 = pygame.transform.scale(self.explosion_3, (EXPLOSION_SIZE))
        self.explosion_4 = pygame.transform.scale(self.explosion_4, (EXPLOSION_SIZE))
        self.explosion_5 = pygame.transform.scale(self.explosion_5, (EXPLOSION_SIZE))
        
        self.explosion_1.set_colorkey((0, 0, 0))
        self.explosion_2.set_colorkey((0, 0, 0))
        self.explosion_3.set_colorkey((0, 0, 0))
        self.explosion_4.set_colorkey((0, 0, 0))
        self.explosion_5.set_colorkey((0, 0, 0))
        
        self.lista_explosion = [self.explosion_1, self.explosion_2, self.explosion_3, self.explosion_4, self.explosion_5]
        self.image = self.lista_explosion[self.index]
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect(center=(300, 400))
        self.active = False  # Añadir estado activo para controlar la animación

    def update(self, pos=None):
        if self.active:  # Solo actualizar si está activo
            if pos:
                self.rect.center = pos
            self.explosion_index()
            self.image = self.lista_explosion[self.index]
            self.screen.blit(self.image, self.rect)

    def explosion_index(self):
        self.velocity_move += 1
        if self.velocity_move >= 10:  # Aumentar velocidad para hacer la animación más rápida
            self.velocity_move = 1
            self.index += 1
            if self.index >= len(self.lista_explosion):
                self.index = 0
                self.active = False  # Detener la animación al final
        return self.index

    def start_explosion(self, pos):
        self.active = True  # Activar la animación
        self.index = 0
        self.velocity_move = 1
        self.rect.center = pos