"""Layout estático de aliens.
Cada entrada define:
  alien_type: tipo de alien
  mIndex: índice global (coincide con el usado en el juego)
  x: desplazamiento horizontal relativo al centro (WIDTH//2)
  y: número de fila lógica (se convertirá a píxeles con grid_size_y)
Modifica este archivo para cambiar rápidamente la formación.
"""

LAYOUT = [
    # Boss (4)
    {"alien_type": "alien_boss_green", "mIndex": 36, "x": -35,  "y": 4},
    {"alien_type": "alien_boss_green", "mIndex": 37, "x": 35,   "y": 4},
    {"alien_type": "alien_boss_green", "mIndex": 38, "x": -115, "y": 4},
    {"alien_type": "alien_boss_green", "mIndex": 39, "x": 115,  "y": 4},

    # Red fila superior (0-7)
    {"alien_type": "butterfly_red", "mIndex": 0, "x": 35,  "y": 5},
    {"alien_type": "butterfly_red", "mIndex": 1, "x": -35,   "y": 5},
    {"alien_type": "butterfly_red", "mIndex": 2, "x": 35,  "y": 6},
    {"alien_type": "butterfly_red", "mIndex": 3, "x": -35,   "y": 6},
    {"alien_type": "butterfly_red", "mIndex": 4, "x": 115, "y": 5},
    {"alien_type": "butterfly_red", "mIndex": 5, "x": -115,  "y": 5},
    {"alien_type": "butterfly_red", "mIndex": 6, "x": 115, "y": 6},
    {"alien_type": "butterfly_red", "mIndex": 7, "x": -115,  "y": 6},

    # Red fila inferior (8-15)
    {"alien_type": "butterfly_red", "mIndex": 8,  "x": -195,  "y": 5},
    {"alien_type": "butterfly_red", "mIndex": 9,  "x": -275,   "y": 5},
    {"alien_type": "butterfly_red", "mIndex": 10, "x": -195,  "y": 6},
    {"alien_type": "butterfly_red", "mIndex": 11, "x": -275,   "y": 6},
    {"alien_type": "butterfly_red", "mIndex": 12, "x": 195, "y": 5},
    {"alien_type": "butterfly_red", "mIndex": 13, "x": 275,  "y": 5},
    {"alien_type": "butterfly_red", "mIndex": 14, "x": 195, "y": 6},
    {"alien_type": "butterfly_red", "mIndex": 15, "x": 275,  "y": 6},

    # Blue fila 1 (16-25)
    {"alien_type": "butterfly_blue", "mIndex": 17, "x": 35,   "y": 7},
    {"alien_type": "butterfly_blue", "mIndex": 16, "x": -35,  "y": 7},
    {"alien_type": "butterfly_blue", "mIndex": 18, "x": -35,  "y": 8},
    {"alien_type": "butterfly_blue", "mIndex": 19, "x": 35,   "y": 8},
    {"alien_type": "butterfly_blue", "mIndex": 20, "x": 115, "y": 7},
    {"alien_type": "butterfly_blue", "mIndex": 21, "x": 195,  "y": 7},
    {"alien_type": "butterfly_blue", "mIndex": 22, "x": 115, "y": 8},
    {"alien_type": "butterfly_blue", "mIndex": 23, "x": 195,  "y": 8},
    {"alien_type": "butterfly_blue", "mIndex": 24, "x": -115, "y": 7},
    {"alien_type": "butterfly_blue", "mIndex": 25, "x": -195,  "y": 7},

    # Blue fila 2 (26-35)
    {"alien_type": "butterfly_blue", "mIndex": 26, "x": -115,  "y": 8},
    {"alien_type": "butterfly_blue", "mIndex": 27, "x": -195,   "y": 8},
    {"alien_type": "butterfly_blue", "mIndex": 28, "x": 275,  "y": 7},
    {"alien_type": "butterfly_blue", "mIndex": 29, "x": 355,   "y": 7},
    {"alien_type": "butterfly_blue", "mIndex": 30, "x": 275, "y": 8},
    {"alien_type": "butterfly_blue", "mIndex": 31, "x": 355,  "y": 8},
    {"alien_type": "butterfly_blue", "mIndex": 32, "x": -275, "y": 7},
    {"alien_type": "butterfly_blue", "mIndex": 33, "x": -355,  "y": 7},
    {"alien_type": "butterfly_blue", "mIndex": 34, "x": -275, "y": 8},
    {"alien_type": "butterfly_blue", "mIndex": 35, "x": -355,  "y": 8},
]

def to_pixels(entry, grid_size_y: float):
    """Convierte fila lógica (y) a píxeles aplicando grid_size_y."""
    x_rel = entry["x"]
    y_px = entry["y"] * grid_size_y - 90
    return x_rel, y_px
