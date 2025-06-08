import pygame
from constants import TILE_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT, STAMINA_MAX, GREEN, ORANGE

class Player:
    def __init__(self, x, y):
        self.x = x  # Posición horizontal en tiles
        self.y = y  # Posición vertical en tiles
        self.speed = 2  # Velocidad de movimiento normal
        self.run_speed = 4  # Velocidad al correr
        self.stamina = STAMINA_MAX  # Energía del jugador
        self.has_sword = False  # True si tiene la espada
        self.has_key = False  # True si tiene la llave
        self.alive = True  # Estado de vida del jugador

    def rect(self):
        # Devuelve el rectángulo para dibujar y detectar colisiones
        return pygame.Rect(self.x * TILE_SIZE, self.y * TILE_SIZE, TILE_SIZE, TILE_SIZE)

    def handle_input(self, labyrinth):
        keys = pygame.key.get_pressed()  # Obtiene teclas presionadas
        dx = dy = 0  # Movimiento en X e Y

        # Determina si el jugador está corriendo (shift) y si tiene estamina suficiente
        running = keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]
        current_speed = self.run_speed if running and self.stamina > 0 else self.speed

        # Reduce estamina al correr
        if running and current_speed == self.run_speed:
            self.stamina = max(0, self.stamina - 0.5)

        # Movimiento vertical
        if keys[pygame.K_UP]:
            dy = -1
        elif keys[pygame.K_DOWN]:
            dy = 1

        # Movimiento horizontal
        if keys[pygame.K_LEFT]:
            dx = -1
        elif keys[pygame.K_RIGHT]:
            dx = 1

        # Recuperación de estamina
        if dx != 0 or dy != 0:
            if current_speed == self.speed:
                self.stamina = min(STAMINA_MAX, self.stamina + 0.2)  # Recupera más lento al caminar
        else:
            self.stamina = min(STAMINA_MAX, self.stamina + 0.5)  # Recupera más rápido si está quieto

        # Calcula nueva posición
        new_x = self.x + dx
        new_y = self.y + dy

        # Mueve al jugador si el nuevo tile no es una pared
        if not labyrinth.is_wall(new_x, new_y):
            self.x = new_x
            self.y = new_y

    def draw(self, surface):
        # Dibuja al jugador como un rectángulo naranja
        pygame.draw.rect(surface, ORANGE, self.rect())
        # Si tiene la espada, dibuja un borde verde
        if self.has_sword:
            pygame.draw.rect(surface, GREEN, self.rect(), 2)
