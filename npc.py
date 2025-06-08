import pygame
from constants import TILE_SIZE, GREEN

class Ariadna:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def rect(self):
        return pygame.Rect(self.x * TILE_SIZE, self.y * TILE_SIZE, TILE_SIZE, TILE_SIZE)

    def interact(self, player, key):
        if not key.collected and player.has_sword:
            key.collected = True
            player.has_key = True

    def draw(self, surface):
        pygame.draw.rect(surface, GREEN, self.rect(), 2)
