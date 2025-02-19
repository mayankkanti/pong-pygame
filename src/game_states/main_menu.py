import pygame
import sys
from utils import clock

def display_main_menu(screen, tilted_alpha):
    font_title = pygame.font.Font('assets/fonts/PressStart2P.ttf', int(74))
    font_subtitle = pygame.font.Font('assets/fonts/PressStart2P.ttf', 24)
    font_tilted = pygame.font.Font('assets/fonts/PressStart2P.ttf', 18)
    
    title_surface = font_title.render('PONG!', True, (255, 255, 255))
    title_rect = title_surface.get_rect(center=(400, 300))
    
    start_surface = font_subtitle.render('Press ENTER to Start', True, (255, 255, 255))
    start_rect = start_surface.get_rect(center=(400, 400))
    
    tilted_surface = font_tilted.render('First to 5!', True, (255, 255, 0))
    tilted_surface.set_alpha(tilted_alpha)
    tilted_surface = pygame.transform.rotate(tilted_surface, -30)
    tilted_rect = tilted_surface.get_rect(center=(550, 270))
    
    screen.fill((0, 0, 0))
    screen.blit(title_surface, title_rect)
    screen.blit(start_surface, start_rect)
    screen.blit(tilted_surface, tilted_rect)
    pygame.display.flip()

def handle_main_menu_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                return 'running'
    return 'main_menu'

def main_menu(screen):
    tilted_alpha = 255
    alpha_direction = -1
    while True:
        state = handle_main_menu_events()
        if state == 'running':
            break
        tilted_alpha += alpha_direction * 5
        if tilted_alpha >= 255 or tilted_alpha <= 0:
            alpha_direction *= -1

        display_main_menu(screen, tilted_alpha)
        clock.tick(60)
    print("Starting game...")
    return 'running'