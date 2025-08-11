import pygame
import random

class Background_2:
    def __init__(self, game):
        self.game = game
        self.screen = pygame.display.get_surface()
        self.scroll_speed = 0.2
        self.toggle_interval = 40  # Intervalo para cambiar entre mitades del fondo
        self.toggle_timer = 0
        self.show_first_half = True
        self.background_y = 0

        # Lista de colores posibles para los rectángulos del fondo
        self.colors = [
            (255, 0, 0),     # rojo
            (0, 0, 255),     # azul
            (0, 255, 0),     # verde
            (128, 128, 128)  # gris
        ]

        # Generar los rectángulos aleatorios
        self.rects = self.generate_rects(80)
        # Separar en dos mitades para alternar
        self.first_half, self.second_half = self.split_rects()

        # --- Crea y almacena surfaces reutilizables por tamaño y color ---
        self.color_surface_cache = {}
        for rect, color in self.rects:
            key = (rect.size, color)
            if key not in self.color_surface_cache:
                surf = pygame.Surface(rect.size)
                surf.fill(color)
                surf.set_colorkey((0, 0, 0))  # Transparente si lo necesitas
                self.color_surface_cache[key] = surf

    def generate_rects(self, num_rects):
        """
        Genera una lista de tuplas (rect, color) con posiciones y tamaños aleatorios.
        """
        rects = []
        for _ in range(num_rects):
            width = random.choice([2, 3, 4])      # Puedes variar los tamaños si quieres
            height = random.choice([1, 2])
            x = random.randint(0, self.game.WINDOW_WIDTH - width)
            y = random.randint(0, self.game.WINDOW_HEIGHT - height)
            color = random.choice(self.colors)
            rect = pygame.Rect(x, y, width, height)
            rects.append((rect, color))  # Cada elemento es (pygame.Rect, color)
        return rects

    def split_rects(self):
        """
        Divide la lista de rectángulos en dos mitades para alternar el fondo.
        """
        half_index = len(self.rects) // 2
        return self.rects[:half_index], self.rects[half_index:]

    def update(self, delta_time):
        """
        Actualiza el estado del fondo animado: scroll vertical y alternancia.
        """
        self.background_y += self.scroll_speed
        if self.background_y >= self.game.WINDOW_HEIGHT:
            self.background_y = 0

        self.toggle_timer += delta_time * 200
        if self.toggle_timer >= self.toggle_interval:
            self.show_first_half = not self.show_first_half
            self.toggle_timer = 0

    def draw(self):
        """
        Dibuja los rectángulos del fondo en la pantalla, usando surfaces en caché.
        """
        self.screen.fill((0, 0, 0))  # Fondo negro
        rects_to_draw = self.first_half if self.show_first_half else self.second_half
        for rect, color in rects_to_draw:
            surf = self.color_surface_cache[(rect.size, color)]
            # Dibuja dos veces para crear efecto de loop continuo
            self.screen.blit(surf, (rect.x, rect.y + self.background_y - self.game.WINDOW_HEIGHT))
            self.screen.blit(surf, (rect.x, rect.y + self.background_y))
