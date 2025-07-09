import pygame
import sys
import time
import math
import random
from setting import *
from background_3 import *
from laser import *
from aliens import *
from debug import *
from player import *
from explosion import *

pygame.init()

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.sprite_sheet = pygame.image.load("Python Test_original/asset/Galaga_SpritesSheet.png").convert_alpha()

        # Background Setup
        self.background = Background()

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
        self.alien_group.sprites()[0].moving = True

    def _setup_aliens(self):
        self.target_positions = [(220 + 55 * (i % 2), 170 + 50 * (i // 2)) for i in range(4)]
        self.target_positions_2 = [(220 + 55 * (i % 2), 260 + 50 * (i // 2)) for i in range(4)]
        self.target_positions_3 = [
            (120 + 55 * (i % 2), 170 + 50 * (i // 2)) if i < 4 else (340 + 55 * ((i - 4) % 2), 170 + 50 * ((i - 4) // 2))
            for i in range(8)
        ]

        for sprite_id in range(4):
            alien = AlienRojo(self, (80 * sprite_id + 220, 200), sprite_id, self.target_positions[sprite_id], t_offset=sprite_id * 20, group_id=1)
            self.alien_group.add(alien)

        for sprite_id in range(8):
            alien = AlienRojo(self, (80 * sprite_id + 220, 1000), sprite_id, self.target_positions_3[sprite_id], t_offset=sprite_id * 25, group_id=2)
            self.alien_group.add(alien)

        for sprite_id in range(4):
            alien = AlienAzul(self,(80 * sprite_id + 220, 200), sprite_id, self.target_positions_2[sprite_id], t_offset=sprite_id * 20, group_id=3)
            self.alien_group.add(alien)

    def check_for_collision(self):
        for laser_sprite in self.player_group.sprite.laser_group:
            collisions = pygame.sprite.spritecollide(laser_sprite, self.alien_group, False)
            for sprite in collisions:
                self.hit_count += 1
                if self.hit_count == 1:
                    sprite.cambiar_sprite()
                    laser_sprite.kill()
                elif self.hit_count >= 3:
                    sprite.kill()
                    laser_sprite.kill()
                    self.explosion_sprite.update(sprite.rect)
                    self.hit_count = 0

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()

    def run(self):
        while True:
            dt = self.clock.tick(80) / 1000
            time_passed = pygame.time.get_ticks() / 1000
            offset = 15 * math.sin(time_passed * 2)

            # Draw
            self.background.draw()
            self.alien_group.draw(self.screen)
            self.player_group.draw(self.screen)
            self.player_sprite.laser_group.draw(self.screen)

            debug(self.phase_complete, 90)
            debug(self.current_group, 130)

            # Update
            self.player_group.update(dt)
            self.player_sprite.laser_group.update(dt)
            self.background.update(dt)
            self.alien_group.update(dt)

            self.check_for_collision()

            if self.current_group == 1:
                self.phase_complete = all(alien.phase == 6 for alien in self.alien_group if alien.group_id == 1)
            if self.phase_complete:
                self.current_group = 2
            elif self.current_group == 2:
                self.phase_complete = all(alien.phase == 6 for alien in self.alien_group if alien.group_id == 2)

            self.handle_events()
            pygame.display.update()

if __name__ == "__main__":
    game = Game()
    game.run()
