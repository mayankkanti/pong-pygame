import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, up_key, down_key):
        super().__init__()
        self.image = pygame.Surface((10, 120))
        self.image.fill((255, 255, 0))
        self.up_key = up_key
        self.down_key = down_key
        self.rect = self.image.get_rect(topleft=(x, y))
    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[self.up_key]:
            self.rect.y -= 10
        if keys[self.down_key]:
            self.rect.y += 10
    def bounding_box(self):
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > 600:
            self.rect.bottom = 600
    def update(self):
        self.player_input()
        self.bounding_box()        
