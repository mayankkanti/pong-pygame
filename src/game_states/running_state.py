import pygame
import sys
from utils import get_scores, clock

def draw_score(screen,score, x, y):
    font_score = pygame.font.Font('assets/fonts/PressStart2P.ttf', 85)
    score_surface = pygame.Surface((200, 200), pygame.SRCALPHA)
    score_text = font_score.render(str(score), True, (255, 255, 255))
    score_text.set_alpha(128)
    score_rect = score_text.get_rect(center=(100, 100))
    score_surface.blit(score_text, score_rect)
    screen.blit(score_surface, (x, y))

def running_state(screen, players, ball_group):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return 'main_menu'
        screen.fill((0, 0, 0))
        players.update()
        ball_group.update()
        players.draw(screen)
        ball_group.draw(screen)
        score1, score2 = get_scores()
        draw_score(screen, score1, 100, 200)
        draw_score(screen, score2, 500, 200)
        
        if ball_group.sprite.reset_timer > 0:
            font = pygame.font.Font('assets/fonts/PressStart2P.ttf', 25)
            timer_surface = pygame.Surface((200, 100), pygame.SRCALPHA)
            timer_surface.fill((0, 0, 0, 128))
            timer_text = font.render(str(ball_group.sprite.reset_timer // 1000 + 1), True, (255, 255, 255))
            timer_rect = timer_text.get_rect(center=(100, 50))
            timer_surface.blit(timer_text, timer_rect)
            screen.blit(timer_surface, (300, 250))
        
        if score1 == 5 or score2 == 5:
            return 'end_screen'
        
        pygame.display.flip() 
        clock.tick(60)
