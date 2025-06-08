import pygame
from constants import SCREEN_WIDTH, HUD_HEIGHT, STAMINA_MAX, WHITE, RED, GREEN, BLACK

class HUD:
    def __init__(self, player):
        self.player = player
        self.bar_rect = pygame.Rect(10, SCREEN_WIDTH + 10, 200, 20)

    def draw(self, surface):
        # Fondo del HUD
        hud_area = pygame.Rect(0, SCREEN_WIDTH, SCREEN_WIDTH, HUD_HEIGHT)
        pygame.draw.rect(surface, BLACK, hud_area)

        # Barra de estamina
        pygame.draw.rect(surface, WHITE, self.bar_rect, 2)
        ratio = self.player.stamina / STAMINA_MAX
        inner_width = int(self.bar_rect.width * ratio)
        inner_rect = pygame.Rect(self.bar_rect.x + 1, self.bar_rect.y + 1, inner_width - 2, self.bar_rect.height - 2)
        pygame.draw.rect(surface, GREEN if ratio > 0.3 else RED, inner_rect)

        # Inventario
        font = pygame.font.SysFont(None, 24)
        text = []
        if self.player.has_sword:
            text.append("Espada")
        if self.player.has_key:
            text.append("Llave")
        inv_text = ", ".join(text) if text else "Vac\u00edo"
        label = font.render(f"Inventario: {inv_text}", True, WHITE)
        surface.blit(label, (220, SCREEN_WIDTH + 10))
