import pygame
from constants import TILE_SIZE, GREEN

class Ariadna:
    def __init__(self, x, y):
        self.x = x  # Posición horizontal en tiles
        self.y = y  # Posición vertical en tiles

    def rect(self):
        # Devuelve un rectángulo para representar visualmente a Ariadna
        return pygame.Rect(self.x * TILE_SIZE, self.y * TILE_SIZE, TILE_SIZE, TILE_SIZE)

    def interact(self, player, key):
        # Si el jugador tiene la espada y la llave no ha sido recogida
        if not key.collected and player.has_sword:
            key.collected = True  # Marca la llave como recogida
            player.has_key = True  # El jugador ahora tiene la llave

    def draw(self, surface):
        # Dibuja a Ariadna como un rectángulo verde con borde
        pygame.draw.rect(surface, GREEN, self.rect(), 2)
