
import pygame
import sys
import time
import math
import random
from setting import *
#from background_3 import *
from background_2 import *
from laser import *
from aliens import *
from debug import *
from player import *
from explosion import *
from alien_laser import *
from grid import *
pygame.init()

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        #self.sprite_sheet = pygame.image.load("asset/Galaga_SpritesSheet.png").convert_alpha()

        # Background Setup
        #self.background = Background()
        self.background_2 = Background_2()

        # Player Setup
        self.player_group = pygame.sprite.GroupSingle()
        self.player_sprite = Player()
        self.player_group.add(self.player_sprite)

        self.current_group = 1
        self.phase_complete = False

        # Alien Setup
        self.alien_group = pygame.sprite.Group()
        self._setup_aliens()

        self.hit_count = 0

        # Explosion Setup
        self.explosion_group = pygame.sprite.Group()
        self.explosion_sprite = Explosion()
        self.explosion_group.add(self.explosion_sprite)

        # Laser Setup
        self.last_time = time.time()
        if self.alien_group.sprites():
            self.alien_group.sprites()[0].moving = True
        
        # Font Setup
        self.font = pygame.font.Font("asset/emulogic/emulogic.ttf", 50)
        
        self.score = 0 
        
        
       

    def _setup_aliens(self):
        grid_size = 5  # Define el tamaño de la cuadrícula
        alien_spacing = 45  # Espacio entre aliens

        def generate_grid_positions(rows, cols, x_start, y_start, spacing):
            return [(x_start + col * spacing, y_start + row * spacing) for row in range(rows) for col in range(cols)]

        # Generar posiciones de la cuadrícula para diferentes grupos de aliens
        positions_grid_0 = generate_grid_positions(1, 1, 270, 215, alien_spacing)
        positions_grid_1 = generate_grid_positions(1, 1, 315, 215, alien_spacing)
        positions_grid_0_0 = generate_grid_positions(1, 1, 315, 170, alien_spacing)
        positions_grid_1_1 = generate_grid_positions(1, 1, 270, 170, alien_spacing)
        
        positions_grid_2 = generate_grid_positions(1, 1, 270, 250, alien_spacing)
        positions_grid_3 = generate_grid_positions(1, 1, 315, 250, alien_spacing)
        positions_grid_2_2 = generate_grid_positions(1, 1, 270, 295, alien_spacing)
        positions_grid_3_3 = generate_grid_positions(1, 1, 315, 295, alien_spacing)
        
        
        positions_grid_4 = generate_grid_positions(2, 1, 360, 170, alien_spacing)
        positions_grid_5 = generate_grid_positions(2, 1, 225, 170, alien_spacing)
        
        positions_grid_6 = generate_grid_positions(1, 4, 225, 125, alien_spacing)
    
        positions_grid_7 = generate_grid_positions(2, 2, 400, 170, alien_spacing)
        positions_grid_8 = generate_grid_positions(2, 2, 140, 170, alien_spacing)
        
        positions_grid_9 = generate_grid_positions(2, 2, 185, 250, alien_spacing)
        positions_grid_10 = generate_grid_positions(2, 2, 355, 250, alien_spacing)
        positions_grid_11 = generate_grid_positions(2, 2, 95, 250, alien_spacing)
        positions_grid_12 = generate_grid_positions(2, 2, 445, 250, alien_spacing)
        
        

        # Configurar posiciones objetivo para cada grupo
        self.target_positions_1 = positions_grid_0 + positions_grid_1 + positions_grid_0_0 + positions_grid_1_1
        self.target_positions_2 = positions_grid_3_3 + positions_grid_2_2 + positions_grid_3 + positions_grid_2
        self.target_positions_3 = positions_grid_4 + positions_grid_5
        self.target_positions_4 = positions_grid_6
        self.target_positions_5 = positions_grid_8 + positions_grid_7
        self.target_positions_6 = positions_grid_9 + positions_grid_10
        self.target_positions_7 = positions_grid_12 + positions_grid_11

        # Crear aliens y asignarlos a posiciones objetivo
        for sprite_id in range(4):
            alien = AlienRojo(self, (80 * sprite_id + 220, 200), sprite_id, self.target_positions_1[sprite_id], t_offset=sprite_id * 40, group_id=1, speed_factor=2.7)
            self.alien_group.add(alien)

        for sprite_id in range(4):
            alien = AlienAzul(self, (80 * sprite_id + 220, -200), sprite_id, self.target_positions_2[sprite_id], t_offset=sprite_id * 40, group_id=2, speed_factor=2.7)
            self.alien_group.add(alien)

        for sprite_id in range(4):
            alien = AlienRojo(self, (80 * sprite_id + 220, 1000), sprite_id, self.target_positions_3[sprite_id], t_offset=sprite_id * -60, group_id=3, speed_factor=2.5)
            self.alien_group.add(alien)

        for sprite_id in range(4):
            alien = AlienGreen(self, (80 * sprite_id + 220, 1200), sprite_id, self.target_positions_4[sprite_id], t_offset=sprite_id * -60 - 30, group_id=4, speed_factor=2.5)
            self.alien_group.add(alien)

        for sprite_id in range(8):
            alien = AlienRojo(self, (80 * sprite_id + 220, 1000), sprite_id, self.target_positions_5[sprite_id], t_offset=sprite_id * -40, group_id=5, speed_factor=2.7)
            self.alien_group.add(alien)

        for sprite_id in range(8):
            alien = AlienAzul(self, (80 * sprite_id + 220, 1000), sprite_id, self.target_positions_6[sprite_id], t_offset=sprite_id * -60, group_id=6, speed_factor=2.5)
            self.alien_group.add(alien)

        for sprite_id in range(8):
            alien = AlienAzul(self, (80 * sprite_id + 220, 1000), sprite_id, self.target_positions_7[sprite_id], t_offset=sprite_id * -60, group_id=7, speed_factor=2.5)
            self.alien_group.add(alien)
        
    
            
  
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
   
    def printing (self): 
                start_y = 300
                offset_y = 70
                colors = {
                    1: (255, 0, 0),     # Red for group_id 1
                    2: (0, 255, 0),     # Green for group_id 2
                    3: (0, 0, 255),     # Blue for group_id 3
                    4: (255, 255, 0),   # Yellow for group_id 4
                }
                # for index, alien in enumerate(self.alien_group):
                #     text = f"ID: {alien.alien_id} Pos: {alien.rect.center}"
                #     color = colors.get(alien.group_id, (255, 255, 255))  # Default color white
                #     text_surface = self.font.render(text, True, color)
                #     text_rect = text_surface.get_rect(center=(alien.rect.centerx, start_y + index * offset_y))
                #     self.screen.blit(text_surface, text_rect)
                    
                
                for alien in self.alien_group:
                    text_surface = self.font.render(str(alien.alien_id), True, (255, 255, 255))
                    text_rect = text_surface.get_rect(center=alien.rect.center)
                    self.screen.blit(text_surface, text_rect)

    
    def get_phase_6_positions(self):
        positions = {}
        for alien in self.alien_group:
            if alien.phase == 6:
                positions[alien.alien_id] = {
                    'group_id': alien.group_id,
                    'position': alien.rect.center }
        return positions
                
    
    def run(self):
        
        while True:
            
            move_direction = 'right'
            
            dt = self.clock.tick(80) / 1000
            time_passed = pygame.time.get_ticks() / 1000
            offset = 15 * math.sin(time_passed * 2)

            # Draw
            self.background_2.draw()
            self.alien_group.draw(self.screen)
            self.player_group.draw(self.screen)
            self.player_sprite.laser_group.draw(self.screen)
            self.explosion_sprite.update()
            
            for alien_sprite in self.alien_group:
                alien_sprite.laser_group.draw(self.screen)
                debug(alien_sprite.group_id, 50)
            # debug
            debug(self.current_group, 130)
            
            #self.printing ()

            # Update
            self.player_group.update(dt)
            self.player_sprite.laser_group.update(dt)
            self.background_2.update(dt)
            self.alien_group.update(dt)
            self.explosion_sprite.update()
            #self.check_for_collision()
            for alien_sprite in self.alien_group:
                alien_sprite.laser_group.update(dt)
            
            for alien in self.alien_group:
                if alien.phase == 6:
            
                    phase_6_positions = self.get_phase_6_positions()
                    debug(phase_6_positions)
            
                
            # Verificación de colisiones
            #self.check_for_collision()
            #self.check_for_player_collision()    

            # Verifica y actualiza la fase completa para cada grupo en orden.
            
            if self.current_group == 1:
                self.phase_complete = all(alien.phase == 6 for alien in self.alien_group if alien.group_id == 1)
                
                if self.phase_complete:
                    self.current_group = 2
                    self.phase_complete = False  # Reset para el siguiente grupo
                    

            elif self.current_group == 2:
                self.phase_complete = all(alien.phase == 6 for alien in self.alien_group if alien.group_id == 2)
                
                if self.phase_complete:
                    self.current_group = 3
                    self.phase_complete = False  # Reset para el siguiente grupo
                    

            elif self.current_group == 3:
                self.phase_complete = all(alien.phase == 6 for alien in self.alien_group if alien.group_id == 3)
                
                if self.phase_complete:
                    self.current_group = 4
                    self.phase_complete = False  # Reset para el siguiente grupo
                   
            elif self.current_group == 4:
                self.phase_complete = all(alien.phase == 6 for alien in self.alien_group if alien.group_id == 4)
                
                if self.phase_complete:
                    self.current_group = 5
                    self.phase_complete = False  # Reset para el siguiente grupo
                    
            elif self.current_group == 5:
                self.phase_complete = all(alien.phase == 6 for alien in self.alien_group if alien.group_id == 5)
                if self.phase_complete:
                    self.current_group = 6
                    self.phase_complete = False  
                           
            elif self.current_group == 6:
                self.phase_complete = all(alien.phase == 6 for alien in self.alien_group if alien.group_id == 6)
                if self.phase_complete:
                    self.current_group = 7
                    self.phase_complete = False  
                           
            elif self.current_group == 7:
                self.phase_complete = all(alien.phase == 6 for alien in self.alien_group if alien.group_id == 7)
                if self.phase_complete:
                    self.current_group = 9
                    self.phase_complete = False  
            
   
           
            # Actualización de fases y grupos
            if self.phase_complete:
                if self.current_group < 8:
                    self.current_group += 1
                else:
                    self.current_group = 1            
                                     
            
            self.handle_events()
            pygame.display.update()

if __name__ == "__main__":
    game = Game()
    game.run()
