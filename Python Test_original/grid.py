import pygame
import sys

class Grid:
    def __init__(self, rows, cols, cell_size, color, screen_width, screen_height):
        self.rows = rows
        self.cols = cols
        self.base_cell_size = cell_size
        self.cell_size = cell_size
        self.color = color
        self.center_x = screen_width // 2
        self.center_y = screen_height // 2
        self.offset = 0
        self.direction = 1  # 1 para derecha, -1 para izquierda
        self.screen_width = screen_width
        self.cell_size_change = 0
        self.cell_size_direction = 1
        self.border_distance = 120  # Distancia desde el centro de la pantalla

    def update_lateral_movement(self, move_pixels):
        # Actualizar el desplazamiento horizontal
        self.offset += self.direction * move_pixels
        if abs(self.offset) > self.border_distance:
            self.direction *= -1

    def update_separation(self, max_size_change):
        # Actualizar el tamaño de las celdas desde el centro
        self.cell_size_change += self.cell_size_direction
        if abs(self.cell_size_change) >= max_size_change:
            self.cell_size_direction *= -1
        self.cell_size = self.base_cell_size + self.cell_size_change

    def get_cell_center(self, row, col):
        # Calcular la posición central de la celda
        x = self.center_x - (self.cols * self.cell_size // 2) + col * self.cell_size + self.cell_size // 2 + self.offset
        y = self.center_y - (self.rows * self.cell_size // 2) + row * self.cell_size + self.cell_size // 2
        return x, y

class Alien(pygame.sprite.Sprite):
    def __init__(self, color, grid, row, col, group_id, alien_id, start_pos=None):
        super().__init__()
        self.image = pygame.Surface((40, 40))  # Placeholder para la imagen del alien
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.grid = grid
        self.row = row
        self.col = col
        self.group_id = group_id
        self.alien_id = alien_id
        self.target_x, self.target_y = self.grid.get_cell_center(row, col)
        if start_pos:
            self.rect.x, self.rect.y = start_pos
        else:
            self.rect.x, self.rect.y = self.target_x, self.target_y
        self.speed = 5  # Velocidad de movimiento hacia la posición final

    def move(self):
        self.target_x, self.target_y = self.grid.get_cell_center(self.row, self.col)

        if self.rect.x < self.target_x:
            self.rect.x += min(self.speed, self.target_x - self.rect.x)
        elif self.rect.x > self.target_x:
            self.rect.x -= min(self.speed, self.rect.x - self.target_x)

        if self.rect.y < self.target_y:
            self.rect.y += min(self.speed, self.target_y - self.rect.y)
        elif self.rect.y > self.target_y:
            self.rect.y -= min(self.speed, self.rect.y - self.target_y)

    def update(self):
        self.move()

class Game:
    def __init__(self, settings):
        pygame.init()
        self.settings = settings
        self.screen = pygame.display.set_mode((settings.width, settings.height))
        self.clock = pygame.time.Clock()
        self.grid = Grid(settings.rows, settings.cols, settings.cell_size, settings.color, settings.width, settings.height)
        self.aliens = self.create_aliens()
        self.all_sprites = pygame.sprite.Group(self.aliens)
        self.speed = settings.speed
        self.move_pixels = settings.move_pixels
        self.max_cell_size_change = settings.max_cell_size_change
        self.running = True

    def create_aliens(self):
        aliens = []
        empty_cells = {0, 1, 2, 9, 8, 7, 10, 19, 20, 29}

        # Diccionarios de posiciones específicas para los aliens según su color y grupo
        green_aliens_positions = {0: 3, 1: 4, 2: 5, 3: 6}

        red_aliens_group_2_positions = {0: 11, 1: 12, 2: 13, 3: 14}
        red_aliens_group_3_positions = {0: 15, 1: 16, 2: 17, 3: 18}
        red_aliens_group_4_positions = {i: 21 + i for i in range(8)}

        blue_aliens_group_5_positions = {i: 30 + i for i in range(4)}
        blue_aliens_group_6_positions = {i: 34 + i for i in range(8)}
        blue_aliens_group_7_positions = {i: 42 + i for i in range(8)}

        # Crear aliens verdes
        for alien_id, pos in green_aliens_positions.items():
            row, col = divmod(pos, self.settings.cols)
            aliens.append(Alien((0, 255, 0), self.grid, row, col, group_id=1, alien_id=alien_id, start_pos=(212, 463)))  # Verde

        # Crear aliens rojos grupo 2
        for alien_id, pos in red_aliens_group_2_positions.items():
            row, col = divmod(pos, self.settings.cols)
            aliens.append(Alien((255, 0, 0), self.grid, row, col, group_id=2, alien_id=alien_id))  # Rojo grupo 2

        # Crear aliens rojos grupo 3
        for alien_id, pos in red_aliens_group_3_positions.items():
            row, col = divmod(pos, self.settings.cols)
            aliens.append(Alien((255, 0, 0), self.grid, row, col, group_id=3, alien_id=alien_id))  # Rojo grupo 3

        # Crear aliens rojos grupo 4
        for alien_id, pos in red_aliens_group_4_positions.items():
            row, col = divmod(pos, self.settings.cols)
            aliens.append(Alien((255, 0, 0), self.grid, row, col, group_id=4, alien_id=alien_id))  # Rojo grupo 4

        # Crear aliens azules grupo 5
        for alien_id, pos in blue_aliens_group_5_positions.items():
            row, col = divmod(pos, self.settings.cols)
            aliens.append(Alien((0, 0, 255), self.grid, row, col, group_id=5, alien_id=alien_id))  # Azul grupo 5

        # Crear aliens azules grupo 6
        for alien_id, pos in blue_aliens_group_6_positions.items():
            row, col = divmod(pos, self.settings.cols)
            aliens.append(Alien((0, 0, 255), self.grid, row, col, group_id=6, alien_id=alien_id))  # Azul grupo 6

        # Crear aliens azules grupo 7
        for alien_id, pos in blue_aliens_group_7_positions.items():
            row, col = divmod(pos, self.settings.cols)
            aliens.append(Alien((0, 0, 255), self.grid, row, col, group_id=7, alien_id=alien_id))  # Azul grupo 7

        return aliens

    def run(self, lateral_movement=True, separation_movement=True):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill((0, 0, 0))  # Fondo negro
            
            if lateral_movement:
                self.grid.update_lateral_movement(self.move_pixels)
            if separation_movement:
                self.grid.update_separation(self.max_cell_size_change)
            
            self.all_sprites.update()
            self.all_sprites.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(self.speed)

        pygame.quit()
        sys.exit()

class Settings:
    def __init__(self):
        self.width = 650
        self.height = 840
        self.rows = 5
        self.cols = 10  # Cambiado a 10 columnas
        self.cell_size = 50
        self.color = (255, 0, 0)  # Rojo
        self.speed = 20
        self.move_pixels = 2
        self.max_cell_size_change = 10

if __name__ == "__main__":
    settings = Settings()
    game = Game(settings)
    game.run(lateral_movement=True, separation_movement=True)