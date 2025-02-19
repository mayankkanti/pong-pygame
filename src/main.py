import pygame
import sys
from player import Player
from ball import Ball
# from obstacle import Obstacles
from game_states.main_menu import main_menu
# from game_states.pause_menu import pause_menu
from game_states.running_state import running_state
from game_states.end_screen import end_screen
from utils import clock 

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('PONG!')

# objects
player1 = Player(10, 10, pygame.K_w, pygame.K_s)
player2 = Player(780, 10, pygame.K_UP, pygame.K_DOWN)
players = pygame.sprite.Group(player1, player2)

ball = Ball(players)
ball_group = pygame.sprite.GroupSingle(ball)


# Game states
current_state = 'main_menu'

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # Game States
    if current_state == 'main_menu':
        current_state = main_menu(screen)
    if current_state == 'running':
        current_state = running_state(screen, players, ball_group)
    if current_state == 'end_screen':
        current_state = end_screen(screen)
    # update display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()