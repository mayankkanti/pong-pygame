import pygame
import sys
from utils import clock, get_scores, reset_scores

def end_screen(screen):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    reset_scores()
                    return 'main_menu'
        
        screen.fill((0, 0, 0))
        score1, score2 = get_scores()
        font = pygame.font.Font('assets/fonts/PressStart2P.ttf', 34)
        
        if score1 == 5:
            text = font.render('Player 1 wins!', True, (255, 255, 255))
        else:
            text = font.render('Player 2 wins!', True, (255, 255, 255))
        
        text_rect = text.get_rect(center=(400, 300))
        screen.blit(text, text_rect)
        
        font_ins = pygame.font.Font('assets/fonts/PressStart2P.ttf', 18)
        instructions = font_ins.render('Press ESC to return to main menu', True, (255, 255, 255))
        instructions_rect = instructions.get_rect(center=(400, 400))
        screen.blit(instructions, instructions_rect)
        
        pygame.display.flip()
        clock.tick(60)