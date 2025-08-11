
import pygame

class TractorBeam(pygame.sprite.Sprite):
    def __init__(self, alien):
        super().__init__()
        self.alien = alien
        self.game = alien.formation.game
        self.image = pygame.Surface((60, 80), pygame.SRCALPHA)  # Superficie transparente
        self.draw_beam()
        self.rect = self.image.get_rect()
        self.update()  # Posicionar inicialmente

    def draw_beam(self):
        # Dibuja un cono semitransparente
        points = [(0, 0), (self.image.get_width(), 0), (self.image.get_width() // 2, self.image.get_height())]
        pygame.draw.polygon(self.image, (200, 200, 255, 100), points) # Azul-blanco, 100/255 de opacidad

    def update(self):
        # Mantener el rayo debajo del alien que lo emite
        self.rect.midtop = self.alien.rect.midbottom
