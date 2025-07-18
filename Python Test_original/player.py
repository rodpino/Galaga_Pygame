import pygame
from setting import *
from laser import *
from debug import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.screen = pygame.display.get_surface()
        self.laser_group = pygame.sprite.Group()
        self.sprite_sheet = pygame.image.load("Python Test_original/asset/Galaga_SpritesSheet.png").convert_alpha()
        self.nave_1 = self.sprite_sheet.subsurface(109, 1, SPRITE_SIZE, SPRITE_SIZE)
        self.nave_2 = self.sprite_sheet.subsurface(109, 19, SPRITE_SIZE, SPRITE_SIZE)
        self.nave_1 = pygame.transform.scale(self.nave_1, (PLAYER_SIZE)) 
        self.nave_2 = pygame.transform.scale(self.nave_2, (PLAYER_SIZE)) 
        self.index = 0

        self.image = self.nave_1
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect(center=(WIDTH / 2, HEIGHT - 55))
        self.direction = pygame.math.Vector2()
        self.position = pygame.math.Vector2(self.rect.center)
        self.velocity = 380
        self.shoot_ready = True
        self.shoot_cooldown = 800  # Tiempo de enfriamiento entre ráfagas
        self.shoot_time = 0
        self.shots_fired = 0  # Contador de disparos en la ráfaga
        self.rafaga_cooldown = 200  # Pausa entre los dos disparos de la ráfaga
        self.last_shot_time = 0
        self.laser_collided = False  # Indicador de colisión del láser
        self.sound_shoot = pygame.mixer.Sound ("Python Test_original/asset/sound_shoot_3.wav")
        
    def player_input(self):
        self.keys = pygame.key.get_pressed()
        current_time = pygame.time.get_ticks()
        
        if self.keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.direction.x = 1
        elif self.keys[pygame.K_LEFT] and self.rect.left > 0:
            self.direction.x = -1
        else:
            self.direction.x = 0

        if self.keys[pygame.K_SPACE]:
            
            if self.shots_fired < 2:
                if current_time - self.last_shot_time > self.rafaga_cooldown or self.laser_collided:
                    self.player_shoot()
                    self.last_shot_time = current_time
                    self.shots_fired += 1
                    self.laser_collided = False  # Restablecer el indicador de colisión
            elif self.shots_fired >= 2 and current_time - self.shoot_time > self.shoot_cooldown:
                self.shots_fired = 0
                self.shoot_time = current_time

    def player_shoot(self):
        laser = Laser(self.rect.center)
        self.laser_group.add(laser)
        self.sound_shoot.play()
    def draw(self):
        for laser in self.laser_group:
            laser.draw()

    def update(self, dt):
        self.player_input()
        self.position.x += self.direction.x * self.velocity * dt
        self.rect.x = round(self.position.x)
        self.laser_group.update(dt)
        # Debugging the player state
        # self.debug(f"Shots fired: {self.shots_fired}", 10, 10)
        # self.debug(f"Shoot cooldown: {self.shoot_cooldown}", 30, 10)
        # self.debug(f"Laser collided: {self.laser_collided}", 50, 10)

    def debug(self, info, y=100, x=50):
        self.screen = pygame.display.get_surface()
        debug_surf = font.render(str(info), True, "white")
        debug_rect = debug_surf.get_rect(topleft=(x, y))
        pygame.draw.rect(self.screen, "black", debug_rect)
        self.screen.blit(debug_surf, debug_rect)
