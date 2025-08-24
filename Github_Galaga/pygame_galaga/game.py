import os

def get_asset_path(*path_parts):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    asset_dir = os.path.join(base_dir, "asset")
    return os.path.join(asset_dir, *path_parts)

import pygame
import sys
import time
import os

from settings import Settings
from entities.player import *
from entities.explosion import Explosion
from entities.background import Background
from entities.formation import Formation
from entities.alien import Alien
from utils.resources import Resources
from entities.capture_light import CaptureLight
from entities.curvas_control import Grid_formation_curves
from entities.curvas_control import Alien_attack_curves


class Game():

    def __init__(self):
        # Inicializar Pygame y configuraciones
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.WIDTH, self.settings.HEIGHT))
        pygame.display.set_caption("Galaga Pygame")
        
        # Inicializar componentes del juego
        self.sprite_sheet = pygame.image.load(get_asset_path("Galaga_SpritesSheet.png")).convert_alpha()
        self.grid_formation_curves = Grid_formation_curves(self)
        self.background = Background(self)
        self.resources = Resources(self)
        self.formation = Formation(self)
        self.explosion_size = (70, 70)
        self.explosion = Explosion(self)
        self.explosion_group = pygame.sprite.Group()
        # self.explosion_group.add(self.explosion)
        # Player Setup
        self.player = Player(self, self.sprite_sheet)
        self.player_group = pygame.sprite.GroupSingle()
        self.player_group.add(self.player)
        self.hit_count = 0
        self.capture_light = CaptureLight(self, 400, 200)
        self.capture_light_group = pygame.sprite.Group(self.capture_light)
        # Puntaje
        self.score = 0  # Iniciar el puntaje en 0
        self.high_score = self.resources.load_high_score()

        # Fuente para mostrar el mIndex
        self.FONT = pygame.font.SysFont(None, 39)
        self.font = pygame.font.Font(get_asset_path("fonts", "emulogic.ttf"), 138)

        # Fuente para mostrar el puntaje
        self.FONT_score = pygame.font.Font(get_asset_path("fonts", "emulogic.ttf"), 190)
        self.clock = pygame.time.Clock()

    def calculate_delta_time(self) -> float:
        """Calcula y devuelve el delta_time usando time.time()"""

        # Inicializa `self.last_time` la primera vez que se llama a la función
        if not hasattr(self, "last_time"):
            self.last_time = time.time()

        current_time = time.time()
        delta_time = current_time - self.last_time
        self.last_time = current_time  # Actualiza `last_time` para el próximo ciclo
        return delta_time

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.resources.save_high_score()
                self.running = False

    def update_game_state(self, delta_time):
        self.formation.update(delta_time)
        self.background.update(delta_time)
        self.player_group.update(delta_time)
        self.resources.check_for_collision()
        self.explosion.update(delta_time)
        self.resources.check_high_score()  # Verificar si el score actual supera el high score
        for alien_sprite in self.formation.aliens:
            alien_sprite.laser_group.update(delta_time)
        Alien.sprite_animation(delta_time)
        # self.capture_light.update()

    def render(self, fps):
        self.screen.fill(self.settings.BLACK)
        self.background.draw()
        self.formation.draw(self.screen)
        self.player_group.draw(self.screen)
        self.player.laser_group.draw(self.screen)
        self.resources.draw_score()
        self.player.draw_life_player()
        self.explosion_group.draw(self.screen)
        self.resources.show_fps(fps)
        for alien_sprite in self.formation.aliens:
            alien_sprite.laser_group.draw(self.screen)
            if alien_sprite.alien_type == "alien_boss_green" and alien_sprite.mIndex== 37:
                self.resources.debug(alien_sprite.rect.x)
                
        
        #self.resources.draw_path_attack(self.screen)
        #self.resources.draw_path_formation(self.screen)
        
        #self.resources.debug(self.formation)
        pygame.display.flip()

    def run(self):
        # Bucle principal del juego
        self.running = True
        
        
        while self.running:
            delta_time = self.calculate_delta_time()
            fps = self.clock.get_fps()
            self.clock.tick()
            self.handle_events()
            self.update_game_state(delta_time)
            self.render(fps)
            
        # Salir de Pygame
        pygame.quit()
        sys.exit()
game = Game()
game.run()