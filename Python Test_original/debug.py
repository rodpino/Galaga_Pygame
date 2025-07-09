import pygame
pygame.init ()

font = pygame.font.Font("Python Test_original/emulogic.ttf", 10)

def debug (info, y = 10, x = 30):
    screen = pygame.display.get_surface ()
    debug_surf = font.render(str(info), True, "white")
    debug_rect = debug_surf.get_rect (topleft = (x, y))
    #pygame.draw.rect(screen, "black", debug_rect)
    screen.blit (debug_surf, debug_rect)