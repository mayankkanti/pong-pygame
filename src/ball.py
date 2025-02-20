import pygame
from utils import clock, increment_score1, increment_score2

class Ball(pygame.sprite.Sprite):
    def __init__(self, players):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(center=(400, 300))
        self.velocity = [5, 5]
        self.reset_timer = 5000
        self.players = players
    def movement(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        if self.rect.top < 0 or self.rect.bottom > 600:
            self.velocity[1] = -self.velocity[1]
        if pygame.sprite.spritecollide(self, self.players, False):
            self.velocity[0] = -self.velocity[0]
    def score(self):
        global score1, score2
        if self.rect.left < 0:
            self.rect.center = (400, 300)
            self.velocity = [5, 5]
            increment_score2()
            self.reset_timer = 3000
        if self.rect.right > 800:
            self.rect.center = (400, 300)
            self.velocity = [-5, -5]
            increment_score1()
            self.reset_timer = 3000
    def update(self):
        if self.reset_timer > 0:
            self.reset_timer -= clock.get_time()
        else:
            self.movement()
        self.score()