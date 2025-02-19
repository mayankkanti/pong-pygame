import pygame


clock = pygame.time.Clock()


# Huh i just realizeed that when import variable, python import a copy of the variable, not the variable itself


_score1 = 0
_score2 = 0

def get_scores():
    return _score1, _score2

def increment_score1():
    global _score1
    _score1 += 1
    
def increment_score2():
    global _score2
    _score2 += 1
    
def reset_scores():
    global _score1, _score2
    _score1 = 0
    _score2 = 0