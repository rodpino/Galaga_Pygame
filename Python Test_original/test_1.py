import pygame, math, random
import sys
import time
import numpy as np
from pygame.locals import *
from debug import *

WIDTH = 650
HEIGHT = 840
FPS = 60
SPRITE_SIZE = 16
SPRITE_SIZE_32 = 32
SEPARACION_SPRITE = 2
INICIO_SPRITE_X = 1
INICIO_SPRITE_Y = 1
angulo_rotacion = 0
ALIENS_SIZE = (50, 50)
PLAYER_SIZE = (45, 45)
EXPLOSION_SIZE = (50, 50)


class Aliens(pygame.sprite.Sprite):
    global_animation_index = 0  # Variable global para la sincronización de animación
    global_velocity_move = 0
    
    def __init__(self):
        super().__init__()
        self.screen = pygame.display.get_surface()
        self.sprite_sheet = pygame.image.load("Python Test_original/asset/Galaga_SpritesSheet.png").convert_alpha()
        self._load_sprites()
        self._group_sprites()
        self.index = 0
        self.velocity_move = 1
        self.cambiar = True
        self.original_image = self.sprites[0]
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)   

        self.laser_group = pygame.sprite.Group()
        self.shoot_cooldown = 200  # Tiempo de enfriamiento entre disparos
        self.last_shot_time = 0
        
    def _load_sprites(self):
        sprite_coords = [
            (109, 37, SPRITE_SIZE, SPRITE_SIZE), (127, 37, SPRITE_SIZE, SPRITE_SIZE),  # alien_green
            (109, 55, SPRITE_SIZE, SPRITE_SIZE), (127, 55, SPRITE_SIZE, SPRITE_SIZE),  # alien_blue
            (109, 73, SPRITE_SIZE, SPRITE_SIZE), (127, 73, SPRITE_SIZE, SPRITE_SIZE),  # butterfly_red
            (109, 91, SPRITE_SIZE, SPRITE_SIZE), (127, 91, SPRITE_SIZE, SPRITE_SIZE),  # butterfly_blue
        ]

        # Escalar y aplicar color key a cada sprite
        self.sprites = []
        for coords in sprite_coords:
            sprite = self.sprite_sheet.subsurface(coords)
            sprite = pygame.transform.scale(sprite, ALIENS_SIZE)
            sprite.set_colorkey((0, 0, 0))
            self.sprites.append(sprite)

        
    def _group_sprites(self):    # Agrupar automáticamente usando nombres y slices
        self._sprite_groups = {
            'alien_green': self.sprites[0:2],
            'alien_blue': self.sprites[2:4],
            'alien_butterfly_red': self.sprites[4:6],
            'alien_butterfly_blue': self.sprites[6:8],
        }
        # También puedes asignarlos directamente si lo necesitas:
        self.alien_green = self._sprite_groups['alien_green']
        self.alien_blue = self._sprite_groups['alien_blue']
        self.alien_butterfly_red = self._sprite_groups['alien_butterfly_red']
        self.alien_butterfly_blue = self._sprite_groups['alien_butterfly_blue']
      
    def cambiar_sprite(self):
        self.cambiar = True
        
    def change_to_blue(self):
        self.original_image = self.alien_blue[0]
        self.image = self.original_image.copy()
        self.mask = pygame.mask.from_surface(self.image)  # Actualizar la máscara con la nueva imagen    
        
    
    def move_aliens(self):
        offset = 0.1
        separation_factor = 1  # Ajusta este factor para aumentar la separación
        self.t = (self.step / self.num_steps) * separation_factor + offset
        self.t = min(self.t, 1.0)  # Asegura que t no sea mayor a 1.0
    
        self.t = self.step / self.num_steps
        self.new_position = self.bezier_curve(self.t)
        self.velocity = self.new_position - self.position
        self.position = self.new_position
        self.rect.center = (int(self.position[0]), int(self.position[1]))
        self.angle = np.degrees(np.arctan2(-self.velocity[1], self.velocity[0]))
        self.image = pygame.transform.rotate(self.original_image, self.angle - 90)
        self.rect = self.image.get_rect(center=self.rect.center)
        self.step += 1
        self.last_position = self.position.copy()
        self.step += self.speed_factor  
        #self.update_animation() 
    def bezier_curve(self, t):
        P0, P1, P2, P3 = self.points
        return (1-t)**3 * np.array(P0) + 3*(1-t)**2 * t * np.array(P1) + 3*(1-t) * t**2 * np.array(P2) + t**3 * np.array(P3)

    def move_towards_target(self, speed=4):
        target_x, target_y = self.target
        dx = target_x - self.rect.x
        dy = target_y - self.rect.y
        distance = math.hypot(dx, dy)

        if distance != 0:
            dx /= distance
            dy /= distance

        self.rect.x += dx * speed
        self.rect.y += dy * speed
        self.update_animation ()
        if distance != 0:
            self.angle = np.degrees(np.arctan2(-dy, dx))

            self.image = pygame.transform.rotate(self.original_image, self.angle - 90)
            self.rect = self.image.get_rect(center=self.rect.center)

        if abs(self.rect.x - target_x) < speed and abs(self.rect.y - target_y) < speed:
            self.rect.x = target_x
            self.rect.y = target_y
            self.moving = False
            self.phase = 6
              
            self.image = pygame.transform.rotate(self.original_image, 0)
            self.rect = self.image.get_rect(center=self.rect.center)
            
            return True
        return False
       
    @classmethod
    def animar_los_bichos(cls):
        cls.global_velocity_move += 1
        if cls.global_velocity_move >= 250:
            cls.global_velocity_move = 1
            cls.global_animation_index += 1
            if cls.global_animation_index >= 2:
                cls.global_animation_index = 0
        
        return cls.global_animation_index

    def update_animation(self):
        self.index = Aliens.animar_los_bichos()
        
        self.image = self.original_image.copy()
        self.mask = pygame.mask.from_surface(self.image)
        
    def update(self, dt):
        self.update_animation()


class Alien_verde (Aliens):
    def __init__(self, game, position, alien_id, target_pos, t_offset=0, group_id=0, speed_factor=1):
        super().__init__()
        self.alien_blue = [self.alien_butterfly_blue
                           ]
        self.speed_factor = speed_factor
        self.game = game
        self.alien_id = alien_id
        self.original_image = self.alien_green[self.index]
        self.group_id = group_id
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.t = t_offset / 100.0 
        self.step = t_offset
        self.hit_count = 0
        self.points = self.control_points()
        self.num_steps = 200
        self.position = np.array(self.points[0], dtype=float)
        self.velocity = np.array([0, 0], dtype=float)
        self.angle = 0
        self.phase = 1
        self.moving = False
        self.target = target_pos
        self.mask = pygame.mask.from_surface(self.image)  # Crear la máscara inicial
        if self.alien_id == 3:
            self.rect.center = self.target
            self.position = np.array(self.target, dtype=float)
    def control_points(self):
        return np.array([-5, 706]), np.array([205, 659]), np.array([263, 524]), np.array([212, 463])
    def control_points_2(self):
        return np.array([212, 463]), np.array([163, 356]), np.array([15, 410]), np.array([56, 517])
    def control_points_3(self):
        return np.array([56, 517]), np.array([123, 619]), np.array([248, 561]), np.array([212, 463])
   
    def control_points_4(self, start_pos):
        debug(start_pos, 50)
        return np.array((start_pos[0] + 23, start_pos[1] + 23)), np.array([177, 194]), np.array([135, 225]), np.array([170, 251])
    def control_points_5(self):
        return np.array([170, 251]), np.array([476, 438]), np.array([152, 527]), np.array([360, 621])
    def control_points_6(self):
        return np.array([360, 621]), np.array([463, 730]), np.array([302, 736]), np.array([430, 830])
    
    def update(self, dt):
        super().update(dt)
        self.update_animation()  
        self.original_image = self.alien_green[self.index]
        if self.hit_count == 1:  # Si no ha sido golpeado, usar la imagen original
            self.original_image = self.alien_blue[self.index]
        self.image = self.original_image.copy()
        self.mask = pygame.mask.from_surface(self.image)  # Actualizar la máscara con la nueva imagen
        if self.game.current_group == 4:
            self.execute_phases_group_1()
        if self.game.current_group == 4:
            self.execute_phases_group_2()
        

    

    def execute_phases_group_1(self):
        if self.group_id == 4:
            if self.phase == 1:
                self.num_steps = 130
                self.points = self.control_points()
                self.move_aliens()
                if self.t >= 1:
                    self.phase = 2
                    self.step = 0

            elif self.phase == 2:
                self.num_steps = 130
                self.points = self.control_points_2()
                self.move_aliens()
                if self.t >= 1:
                    self.phase = 3
                    self.moving = True
                    self.step = 0

            elif self.phase == 3:
                self.num_steps = 130
                self.points = self.control_points_3()
                self.move_aliens()
                if self.t >= 1:
                    self.phase = 4
                    self.moving = True
                    self.step = 0

            elif self.phase == 4:
                if self.move_towards_target():
                    self.phase = 6
                    self.execute_phases_group_2 ()
                   
    
    def execute_phases_group_2(self):
        
        if self.group_id == 4 and self.alien_id == 0:
            if self.phase == 6:
                self.num_steps = 170
                self.points = self.control_points_4(self.target) 
                self.move_aliens()
                if self.t >= 1:
                    self.phase = 7
                    self.moving = True
                    self.step = 0

            elif self.phase == 7:
                self.num_steps = 430
                self.points = self.control_points_5()
                self.move_aliens()
                if self.t >= 1:
                    self.phase = 8
                    self.moving = True
                    self.step = 0

            elif self.phase == 8:
                self.num_steps = 430
                self.points = self.control_points_6()
                self.move_aliens()
                if self.t >= 1:
                    self.phase = 9
                    self.moving = False
                    self.step = 0

           
                             
    
class Game:
    def __init__(self):
        
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()  
        self.current_group = 4
        self.phase_complete = False

        # Alien Setup
        self.alien_group = pygame.sprite.Group()
        self._setup_aliens()

        self.hit_count = 0
        self.font = pygame.font.Font("Python Test_original/emulogic.ttf", 40)

    def _setup_aliens(self):
        

        self.target_positions_4 = self.create_target_position (sprite_id)
        
        for sprite_id in range(4):
            alien = Alien_verde(self, (50,800), sprite_id, self.target_positions_4[sprite_id], t_offset=sprite_id * - 60 -30, group_id=4, speed_factor=2.5)
            self.alien_group.add(alien)   

    def create_target_position (self):

            
            
        self.target_positions_4 = [(235 + 45 * (i - 1), 219)  if i < 2 else (235 + 45 * (i - 1), 219) for i in range(4)]



    def eliminate_alien(self, alien):
        """Elimina un alien y aumenta la puntuación según su tipo."""
        if isinstance(alien, Alien_verde):
            self.score += 150
        alien.kill()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
                for alien in self.alien_group:
                    text_surface = self.font.render(str(alien.alien_id), True, (255, 255, 255))
                    text_rect = text_surface.get_rect(center=alien.rect.center)
                    self.screen.blit(text_surface, text_rect)
                    
    def printing (self): 
                start_y = 300
                offset_y = 70
                colors = {
                    1: (255, 0, 0),     # Red for group_id 1
                    2: (0, 255, 0),     # Green for group_id 2
                    3: (0, 0, 255),     # Blue for group_id 3
                    4: (255, 255, 0),   # Yellow for group_id 4
                }
               
                    
                
                # for alien in self.alien_group:
                #     text_surface = self.font.render(str(alien.target_position_4), True, (255, 255, 255))
                #     text_rect = text_surface.get_rect(center=alien.rect.midbottom)
                #     self.screen.blit(text_surface, text_rect)                

    def run(self):
        self.clock = pygame.time.Clock()
        while True:
            move_direction = 'right'
            dt = self.clock.tick(80) / 1000
            time_passed = pygame.time.get_ticks() / 1000
            offset = 15 * math.sin(time_passed * 2)

            # Draw
            self.alien_group.draw(self.screen)
            for alien_sprite in self.alien_group:
                alien_sprite.laser_group.draw(self.screen)
            
            self.screen.fill ((0,0,0))
            self.alien_group.draw(self.screen)
            self.alien_group.update(dt)
            

            self.printing ()
            
            self.handle_events()
            pygame.display.update()
        
if __name__ == "__main__":
    game = Game()
    game.run()