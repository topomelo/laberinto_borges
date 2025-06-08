import pygame
from constants import TILE_SIZE, BLUE, YELLOW

class Item:
    def __init__(self, x, y, name, color):
        self.x = x  # Posición horizontal en tiles
        self.y = y  # Posición vertical en tiles
        self.name = name  # Nombre del objeto ("sword" o "key")
        self.color = color  # Color para dibujarlo
        self.collected = False  # Estado: si fue recogido o no

    def rect(self):
        # Devuelve un rectángulo para detectar colisiones y dibujar
        return pygame.Rect(self.x * TILE_SIZE, self.y * TILE_SIZE, TILE_SIZE, TILE_SIZE)

    def draw(self, surface):
        # Dibuja el objeto si aún no fue recogido
        if not self.collected:
            pygame.draw.rect(surface, self.color, self.rect())

# Espada azul, da capacidad de matar al minotauro
class Sword(Item):
    def __init__(self, x, y):
        super().__init__(x, y, "sword", BLUE)

# Llave amarilla, permite salir del laberinto
class Key(Item):
    def __init__(self, x, y):
        super().__init__(x, y, "key", YELLOW)
