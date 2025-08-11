import pygame
import sys

# Inicialización de Pygame
pygame.init()

# Configuración básica de la ventana
ANCHO = 800
ALTO = 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Breakout")

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
AMARILLO = (255, 255, 0)

# Configuración del juego
FPS = 60
reloj = pygame.time.Clock()

# Clases para los elementos del juego
class Barra(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((100, 20))
        self.image.fill(AZUL)
        self.rect = self.image.get_rect()
        self.rect.midbottom = (ANCHO // 2, ALTO - 30)
        self.velocidad = 10

    def update(self):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.velocidad
        if teclas[pygame.K_RIGHT] and self.rect.right < ANCHO:
            self.rect.x += self.velocidad


class Pelota(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((15, 15))
        self.image.fill(ROJO)
        self.rect = self.image.get_rect()
        self.rect.center = (ANCHO // 2, ALTO // 2)
        self.vel_x = 4
        self.vel_y = -4

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        # Rebotar en los bordes de la ventana
        if self.rect.left <= 0 or self.rect.right >= ANCHO:
            self.vel_x *= -1
        if self.rect.top <= 0:
            self.vel_y *= -1
        # Si la pelota toca la parte inferior, el juego termina
        if self.rect.bottom >= ALTO:
            pygame.quit()
            sys.exit()


class Ladrillo(pygame.sprite.Sprite):
    def __init__(self, x, y, golpes, color):
        super().__init__()
        self.image = pygame.Surface((80, 30))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.golpes = golpes  # Cuántos golpes soporta el ladrillo


# Crear sprites
barra = Barra()
pelota = Pelota()

# Crear un grupo para los ladrillos
ladrillos = pygame.sprite.Group()
colores = [ROJO, AZUL, BLANCO, VERDE, AMARILLO]  # Colores para cada fila
for fila in range(5):  # 5 filas de ladrillos
    for columna in range(10):  # 10 ladrillos por fila
        golpes = 1 if fila == 4 else 2  # Última fila (fila 4) desaparece al primer golpe
        ladrillo = Ladrillo(columna * 82 + 10, fila * 32 + 10, golpes, colores[fila])
        ladrillos.add(ladrillo)

# Crear grupos de sprites
todos_los_sprites = pygame.sprite.Group()
todos_los_sprites.add(barra, pelota)
todos_los_sprites.add(ladrillos)

# Bucle principal
while True:
    # Manejo de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Actualizar objetos
    todos_los_sprites.update()

    # Comprobar colisiones
    if pygame.sprite.collide_rect(pelota, barra):
        pelota.vel_y *= -1

    ladrillos_golpeados = pygame.sprite.spritecollide(pelota, ladrillos, dokill=False)
    for ladrillo in ladrillos_golpeados:
        ladrillo.golpes -= 1
        if ladrillo.golpes <= 0:
            ladrillos.remove(ladrillo)
            todos_los_sprites.remove(ladrillo)
        pelota.vel_y *= -1

    # Dibujar en la pantalla
    ventana.fill(NEGRO)
    todos_los_sprites.draw(ventana)
    pygame.display.flip()

    # Controlar la velocidad del juego
    reloj.tick(FPS)