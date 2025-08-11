import pygame
import os
from test_13 import *

pygame.init()

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
FONT_PATH = os.path.join(PROJECT_ROOT, "asset", "emulogic", "emulogic.ttf")

font = pygame.font.Font(FONT_PATH, 16)

def debug(info, y=180, x=20):
    screen = pygame.display.get_surface()
    if screen:  # Protección contra None
        debug_surf = font.render(str(info), True, "white")
        debug_rect = debug_surf.get_rect(topleft=(x, y))
        # pygame.draw.rect(screen, "black", debug_rect)
        screen.blit(debug_surf, debug_rect)

# Esta función debería estar en una clase si usas self
def debug_boss_state(surface):
    if self.alien_type == 'boss_green':
            debug_info = [
                f"curve_attack_idx: {self.curve_attack_index}",
                f"reached_end: {self.reached_curve_end}",
                f"pausing: {self.pausing}",
                f"pause_start: {self.pause_start_time}",
                f"is_capture: {self.is_capture_formation}"
            ]

            font = self.formation.game.FONT

            text_x = int(self.x) - 250 + (self.mIndex % 4) * 80 
            text_y = int(self.y) + 250 + (self.mIndex % 4) * 150

            for i, line in enumerate(debug_info):
                text_surface = font.render(line, True, (255, 255, 255))
                surface.blit(text_surface, (text_x, text_y + i * 25))
