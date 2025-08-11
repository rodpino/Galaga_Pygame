

class Settings():
    def __init__(self):
        # Nuevo tamaño de display (aumentado ~23%)
        factor = 1.5
        self.WIDTH = 975
        self.HEIGHT = 1425
        self.FPS = 60
        
        self.SPRITE_SIZE = int(16 * factor)
        self.SPRITE_SIZE_32 = int(32 * factor)
        self.SEPARACION_SPRITE = int(2 * factor)
        self.INICIO_SPRITE_X = int(1 * factor)
        self.INICIO_SPRITE_Y = int(1 * factor)
        self.angulo_rotacion = 0
        self.ALIENS_SIZE = (int(40 * factor), int(40 * factor))
        self.PLAYER_SIZE = (int(45 * factor), int(45 * factor))
        self.EXPLOSION_SIZE = (int(50 * factor), int(50 * factor))
        self.CAPTURE_SIZE = (int(60 * factor), int(190 * factor))
        # Colores
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.RED = (255, 0, 0)

