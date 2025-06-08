import pygame
from constants import TILE_SIZE, BLUE, YELLOW

class Item:
    def __init__(self, x, y, name, color):
        self.x = x
        self.y = y
        self.name = name
        self.color = color
        self.collected = False

    def rect(self):
        return pygame.Rect(self.x * TILE_SIZE, self.y * TILE_SIZE, TILE_SIZE, TILE_SIZE)

    def draw(self, surface):
        if not self.collected:
            pygame.draw.rect(surface, self.color, self.rect())

class Sword(Item):
    def __init__(self, x, y):
        super().__init__(x, y, "sword", BLUE)

class Key(Item):
    def __init__(self, x, y):
        super().__init__(x, y, "key", YELLOW)
