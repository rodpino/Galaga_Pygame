import numpy as np
import random


class Grid_formation_curves:
    def __init__(self, game):
        self.game = game
        self.width = self.game.settings.WIDTH

    def control_points_1(self):
        """ superior izquierdo """
        return np.array([
            [350, -10],
            [445, 390],
            [907, 400],
            [900, 620]
        ])

    def control_points_2(self):
        """ superior izquierdo """
        return np.array([
            [900, 620],
            [925, 850],
            [657, 879],
            [610, 710]
        ])

    def control_points_3(self):
        """ loop izquierdo """
        return np.array([
            ([ -5, 1305]),
            ([315, 1180]),
            ([480,  1000]),
            ([490,  765])
        ])

    def control_points_4(self):
        """ loop izquierdo """
        return np.array([
            ([490, 765]),
            ([470, 605]),
            ([245, 625]),
            ([230, 790])
        ])

    def control_points_5(self):
        """ loop izquierdo """
        return np.array([
            ([230, 790]),
            ([200, 970]),
            ([550,1040]),
            ([480, 690])
        ])

    def control_points_6(self):
        """ loop derecho """
        return np.array([
            ([self.width   -5, 1305]),
            ([self.width - 315, 1180]),
            ([self.width - 480,  1000]),
            ([self.width - 490,  765])
        ])

    def control_points_7(self):
        """ loop derecho """
        return np.array([
            ([self.width - 490, 765]),
            ([self.width - 470, 605]),
            ([self.width - 245, 625]),
            ([self.width - 230, 790])
        ])

    def control_points_8(self):
        """ loop derecho """
        return np.array([
            ([self.width - 230, 790]),
            ([self.width - 200, 970]),
            ([self.width - 550,1040]),
            ([self.width - 480, 690])
        ])

    def control_points_10(self):
        """ superior oblicuo izquierdo """
        return np.array([
            [570, -10],
            [540, 190],
            [ 35, 490],
            [ 30, 680]
        ])

    def control_points_11(self):
        """ superior oblicuo izquierdo """
        return np.array([
            [ 30, 680],
            [ 30, 865],
            [245, 945],
            [365, 725]
        ])

    def control_points_12(self):
        """ superior derecho """
        return np.array([
            [self.width - 350, -10],
            [self.width - 445, 390],
            [self.width - 907, 400],
            [self.width - 900, 620]
        ])

    def control_points_13(self):
        """ superior derecho """
        return np.array([
            [self.width - 900, 620],
            [self.width - 925, 850],
            [self.width - 657, 879],
            [self.width - 610, 710]
        ])

    def control_points_14(self):
        """ superior oblicuo derecho """
        return np.array([
            [self.width - 570, -10],
            [self.width - 540, 190],
            [self.width -  35, 490],
            [self.width -  30, 680]
        ])

    def control_points_15(self):
        """ superior oblicuo derecho """
        return np.array([
            [self.width -  30, 680],
            [self.width -  30, 865],
            [self.width - 245, 945],
            [self.width - 365, 725]
        ])


class Alien_attack_curves:
    def __init__(self, alien):
        self.alien = alien
        self.width = self.alien.game.settings.WIDTH
    
    def attack_control_points_1_1(self, offset_x=0):
        return np.array([
            [self.alien.x, self.alien.y],  # Comienza desde la posición actual
            [174, 96],  # Un ejemplo de punto intermedio
            [50, 250],  # Otro punto
            [300, 395]  # Final en una posición aleatoria
        ])
        
    def attack_control_points_1_2(self, offset_x=0):
        return np.array([
            [300, 395] ,  # Comienza desde la posición actual
            [480, 455],  # Un ejemplo de punto intermedio
            [470, 620],  # Otro punto
            [370, 650]  # Final en una posición aleatoria
        ])
        
    def attack_control_points_1_3(self, offset_x=0):
        player_x = self.alien.game.player.rect.centerx  # Obtener la posición en X del jugador
        return np.array([
            [370, 650],     # Comienza desde la posición actual
            [130, 775],     # Punto intermedio
            [495, 815],     # Otro punto
            [player_x, 1000]  # Final en la posición X del jugador
        ])   
            
    def attack_control_points_1_4(self, offset_x=0):
        
        random_x = random.randint(350, 600)
        return np.array([
            [240, -10] ,  # Comienza desde la posición actual
            [150, 55],  # Un ejemplo de punto intermedio
            [270, 85],  # Otro punto
            [self.alien.x, self.alien.y]  # Final en una posición aleatoria
        ]) 
    def attack_control_points_2_1(self, offset_x=0):
        
        return np.array([
            [self.x, self.y],  # Comienza desde la posición actual
            [self.width - 174, 96],  # Un ejemplo de punto intermedio
            [self.width - 50, 250],  # Otro punto
            [self.width - 300, 395]  # Final en una posición aleatoria
        ])
        self.width
    def attack_control_points_2_2(self, offset_x=0):
        
        return np.array([
            [self.width - 300, 395] ,  # Comienza desde la posición actual
            [self.width - 480, 455],  # Un ejemplo de punto intermedio
            [self.width - 470, 620],  # Otro punto
            [self.width - 370, 650]  # Final en una posición aleatoria
        ])
        
    def attack_control_points_2_3(self, offset_x=0):
       
        player_x = self.formation.game.player.rect.centerx  # Obtener la posición en X del jugador
        return np.array([
            [self.width - 370, 650],     # Comienza desde la posición actual
            [self.width - 130, 775],     # Punto intermedio
            [self.width - 495, 815],     # Otro punto
            [player_x, 1000]  # Final en la posición X del jugador
        ])   
            
    def attack_control_points_2_4(self, offset_x=0):
        
        random_x = random.randint(350, 600)
        return np.array([
            [self.width - 240, -10] ,  # Comienza desde la posición actual
            [self.width - 150, 55],  # Un ejemplo de punto intermedio
            [self.width - 270, 85],  # Otro punto
            [self.x, self.y]  # Final en una posición aleatoria
        ]) 
        
    
    def attack_control_points_2(self, offset_x=0):
        width = self.formation.game.settings.WIDTH
        player_x = self.formation.game.player.rect.centerx  # Obtener la posición en X del jugador
        return np.array([
            [200, 660],  # Comienza desde la posición actual
            [300, 760],  # Un ejemplo de punto intermedio
            [330, 780],  # Otro punto
            [player_x, 1000]  # Final en una posición aleatoria
        ])

    def attack_control_points_3(self, offset_x=0):
        width = self.formation.game.settings.WIDTH
        random_x = random.randint(120, 130)
        return np.array([
            
            [120, -10],
            #[random_x, -10],  # Comienza desde la posición actual
            [110, 115],  # Un ejemplo de punto intermedio
            [365, 80],  # Otro punto
            [self.x, self.y]  # Final en una posición aleatoria
        ])

    def attack_control_points_4(self, random_xx, offset_x=0) :
        return np.array([
            
            [self.alien.x, self.alien.y],  # Comienza desde la posición actual
            [110 + random_xx, 270],  # Punto intermedio ajustado
            [10 + random_xx, 340],  # Otro punto ajustado
            [170 + random_xx, 430]   # Final ajustado
        ])

    def attack_control_points_5(self, random_xx, offset_x=0):
        random_x = random.randint(150, 160)
        return np.array([
            
            [170 + random_xx, 430], 
            [470 + random_xx, 605],
            [435 + random_xx, 920],
            [325 + random_xx, 925]
    ])

    def attack_control_points_6(self, random_xx, offset_x=0):
        return np.array([
            
            [325 + random_xx, 925],
            [195 + random_xx, 920],  # Un ejemplo de punto intermedio
            [150 + random_xx, 895],  # Otro punto
            [self.alien.x, self.alien.y] # Final en una posición aleatoria
        ])
        
    def attack_control_points_7(self, offset_x=0):
        random_x = random.randint(350, 600)
        return np.array([
            
            [135, 340],
            [150, 895],  # Un ejemplo de punto intermedio
            [195, 920],  # Otro punto
            [self.alien.x, self.alien.y]  # Final en una posición aleatoria
        ])       

    def attack_control_points_8(self, random_xx, offset_x=0):
        
        return np.array([
            [self.x, self.y],  # Comienza desde la posición actual
            [self.width - 110 + random_xx, 270],  # Punto intermedio ajustado
            [self.width - 10 + random_xx, 340],  # Otro punto ajustado
            [self.width - 170 + random_xx, 430]   # Final en una posición aleatoria
        ])

    def attack_control_points_9(self, random_xx, offset_x=0):
        width = self.formation.game.settings.WIDTH
        random_x = random.randint(155, 165)
        return np.array([
            [self.width - 170 + random_xx, 430], 
            [self.width - 470 + random_xx, 605],
            [self.width - 435 + random_xx, 920],
            [self.width - 325 + random_xx, 925]
        ])

    def attack_control_points_10(self, random_xx, offset_x=0):
                
        return np.array([
            [self.width - 325 + random_xx, 925],
            [self.width - 195 + random_xx, 920],  # Un ejemplo de punto intermedio
            [self.width - 150 + random_xx, 895],  # Otro punto
            [self.x, self.y]  # Final en una posición aleatoria
        ])    
        
    def attack_control_points_11(self, offset_x=0):
        width = self.formation.game.settings.WIDTH
        random_x = random.randint(350, 600)
        return np.array([
            
            [self.width - 190, 100],  # Un ejemplo de punto intermedio
            [self.width - 170, -10],
            [self.width - 265, 55],  # Otro punto
            [self.x, self.y]  # Final en una posición aleatoria
        ])   
        
        
    def attack_control_points_12(self, offset_x=0):
        random_x = random.randint(160, 170)
        return np.array([
            [265, 660],  # Comienza desde la posición actual
            [315, 760],  # Un ejemplo de punto intermedio
            [285, 850],  # Otro punto
            [random_x, 1000]  # Final en una posición aleatoria
        ])

    def attack_control_points_13(self, offset_x=0):
        random_x = random.randint(140, 150)
        return np.array([
            [random_x, -10],  # Comienza desde la posición actual
            [135, 40],  # Un ejemplo de punto intermedio
            [315, 50],  # Otro punto
            [self.x, self.y]  # Final en una posición aleatoria
        ])          


class Relative_curves:
    """ curvas de ataque de boss_green y alien red """ 
    def __init__(self, alien, formation, game):
        self.alien = alien
        self.formation = formation
        self.game = game
        self.attack_curves = []
        self.performing_capture = False
        self.capture_start_time = None

    def define_attack_curves_relative(self, offset_x=-50, offset_y=0):
        player_x = self.formation.game.player.rect.centerx  # Obtener la posición en X del jugador
        relative_player_x = player_x - self.alien.x

        base_curve_1 = np.array([
            [0, 0],  # Comienza desde la posición actual
            [-214, 270],  # Punto intermedio ajustado
            [-28, 456],  # Otro punto ajustado
            [100, 331]   # Final en una posición aleatoria
        ])

        base_curve_2 = np.array([
            [100, 331], 
            [180, 181],
            [-70, 100],
            [-92, 264]  # Final en una posición aleatoria
        ])

        base_curve_3 = np.array([
            [-92, 264],
            [-60, 438],  # Un ejemplo de punto intermedio
            [291, 570],  # Otro punto
            [relative_player_x, 1000]  # Final en una posición aleatoria
        ])

        base_curve_4 = np.array([
            [20, -230],
            [16, -190],  # Un ejemplo de punto intermedio
            [8, -105],  # Otro punto
            [0, 0]  # Final en una posición aleatoria
        ])

        # Aplicar desplazamientos relativos a los puntos de control
        adjusted_curve_1 = [point + np.array([offset_x, 0]) for point in base_curve_1]
        adjusted_curve_2 = [point + np.array([offset_x, 0]) for point in base_curve_2]
        adjusted_curve_3 = [point + np.array([offset_x, 0]) for point in base_curve_3]
        adjusted_curve_4 = [point + np.array([offset_x, 0]) for point in base_curve_4]

        # Trasladar la curva al punto inicial del alienígena
        starting_point = np.array([self.alien.x, self.alien.y])
        self.alien.attack_curves = [
            [starting_point + point for point in adjusted_curve_1],
            [starting_point + point for point in adjusted_curve_2],
            [starting_point + point for point in adjusted_curve_3],
            [starting_point + point for point in adjusted_curve_4]
            ]

    def define_attack_curves_relative_2(self, offset_x=0, offset_y=0):
        # Curva base en coordenadas relativas

        player_x = self.formation.game.player.rect.centerx  # Obtener la posición en X del jugador
        relative_player_x = player_x - self.alien.x
        base_curve_1 = np.array([
            [0, 0],  # Comienza desde la posición actual
            [214, 270],  # Punto intermedio ajustado
            [28, 456],  # Otro punto ajustado
            [-100, 331]   # Final en una posición aleatoria
            ])

        base_curve_2 = np.array([
            [-100, 331] , 
            [-180, 181],
            [70, 100],
            [92, 264]  # Final en una posición aleatoria
            ])

        base_curve_3 = np.array([
            [92, 264],
            [60, 438],  # Un ejemplo de punto intermedio
            [-291, 570],  # Otro punto
            [relative_player_x, 1000]  # Final en una posición aleatoria
            ])

        base_curve_4 = np.array([
            [-20, -230],
            [-16, -190],  # Un ejemplo de punto intermedio
            [-8, -105],  # Otro punto
            [0, 0]  # Final en una posición aleatoria
            ])

        # Aplicar desplazamientos relativos a los puntos de control
        adjusted_curve_1 = [point + np.array([offset_x, 0]) for point in base_curve_1]
        adjusted_curve_2 = [point + np.array([offset_x, 0]) for point in base_curve_2]
        adjusted_curve_3 = [point + np.array([offset_x, 0]) for point in base_curve_3]
        adjusted_curve_4 = [point + np.array([offset_x, 0]) for point in base_curve_4]

        # Trasladar la curva al punto inicial del alienígena
        starting_point = np.array([self.alien.x, self.alien.y])
        self.alien.attack_curves = [
            [starting_point + point for point in adjusted_curve_1],
            [starting_point + point for point in adjusted_curve_2],
            [starting_point + point for point in adjusted_curve_3],
            [starting_point + point for point in adjusted_curve_4]
            ]
