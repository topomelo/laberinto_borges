import pygame
from constants import TILE_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT, STAMINA_MAX, GREEN, ORANGE

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 2
        self.run_speed = 4
        self.stamina = STAMINA_MAX
        self.has_sword = False
        self.has_key = False
        self.alive = True

    def rect(self):
        return pygame.Rect(self.x * TILE_SIZE, self.y * TILE_SIZE, TILE_SIZE, TILE_SIZE)

    def handle_input(self, labyrinth):
        keys = pygame.key.get_pressed()
        dx = dy = 0
        running = keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]
        current_speed = self.run_speed if running and self.stamina > 0 else self.speed
        if running and current_speed == self.run_speed:
            self.stamina = max(0, self.stamina - 0.5)
        if keys[pygame.K_UP]:
            dy = -1
        elif keys[pygame.K_DOWN]:
            dy = 1
        if keys[pygame.K_LEFT]:
            dx = -1
        elif keys[pygame.K_RIGHT]:
            dx = 1

        if dx != 0 or dy != 0:
            # Recuperaci\u00f3n lenta mientras se camina
            if current_speed == self.speed:
                self.stamina = min(STAMINA_MAX, self.stamina + 0.2)
        else:
            # Recuperaci\u00f3n r\u00e1pida al estar quieto
            self.stamina = min(STAMINA_MAX, self.stamina + 0.5)

        new_x = self.x + dx
        new_y = self.y + dy
        if not labyrinth.is_wall(new_x, new_y):
            self.x = new_x
            self.y = new_y

    def draw(self, surface):
        pygame.draw.rect(surface, ORANGE, self.rect())
        # Borde verde si tiene la espada
        if self.has_sword:
            pygame.draw.rect(surface, GREEN, self.rect(), 2)
