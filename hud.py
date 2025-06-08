import pygame
from constants import SCREEN_WIDTH, HUD_HEIGHT, STAMINA_MAX, WHITE, RED, GREEN, BLACK

class HUD:
    def __init__(self, player):
        self.player = player  # Referencia al jugador para acceder a su estamina y objetos
        self.bar_rect = pygame.Rect(10, SCREEN_WIDTH + 10, 200, 20)  # Rectángulo para la barra de estamina

    def draw(self, surface):
        # Dibuja el fondo del HUD como un rectángulo negro debajo del laberinto
        hud_area = pygame.Rect(0, SCREEN_WIDTH, SCREEN_WIDTH, HUD_HEIGHT)
        pygame.draw.rect(surface, BLACK, hud_area)

        # Dibuja el contorno de la barra de estamina en blanco
        pygame.draw.rect(surface, WHITE, self.bar_rect, 2)

        # Calcula el ancho interno de la barra según la estamina actual
        ratio = self.player.stamina / STAMINA_MAX
        inner_width = int(self.bar_rect.width * ratio)
        inner_rect = pygame.Rect(self.bar_rect.x + 1, self.bar_rect.y + 1, inner_width - 2, self.bar_rect.height - 2)

        # El color de la barra es verde si tiene más del 30% de estamina, rojo si menos
        pygame.draw.rect(surface, GREEN if ratio > 0.3 else RED, inner_rect)

        # Dibuja el texto del inventario
        font = pygame.font.SysFont(None, 24)
        text = []  # Lista de objetos que tiene el jugador

        if self.player.has_sword:
            text.append("Espada")
        if self.player.has_key:
            text.append("Llave")

        # Si no tiene nada, muestra "Vacío"
        inv_text = ", ".join(text) if text else "Vacío"
        label = font.render(f"Inventario: {inv_text}", True, WHITE)

        # Muestra el texto en la pantalla, a la derecha de la barra de estamina
        surface.blit(label, (220, SCREEN_WIDTH + 10))
