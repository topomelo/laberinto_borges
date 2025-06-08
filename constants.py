TILE_SIZE = 32  # Tamaño de cada baldosa (tile) en píxeles
MAZE_WIDTH = 15  # Ancho del laberinto en cantidad de tiles
MAZE_HEIGHT = 15  # Alto del laberinto en cantidad de tiles
HUD_HEIGHT = 40  # Altura del HUD (barra superior) en píxeles

# Tamaño de la pantalla calculado en base al laberinto y HUD
SCREEN_WIDTH = MAZE_WIDTH * TILE_SIZE
SCREEN_HEIGHT = MAZE_HEIGHT * TILE_SIZE + HUD_HEIGHT

# Colores definidos en formato RGB para facilitar uso visual
BLACK = (0, 0, 0)        # Negro: fondo principal
WHITE = (255, 255, 255)  # Blanco: textos y elementos neutros
GRAY = (100, 100, 100)   # Gris: bordes o detalles
GREEN = (0, 255, 0)      # Verde: usado para elementos positivos
RED = (255, 0, 0)        # Rojo: peligro o muerte
BLUE = (0, 0, 255)       # Azul: decorativo o informativo
YELLOW = (255, 255, 0)   # Amarillo: destacable
ORANGE = (255, 165, 0)   # Naranja: ítems especiales o advertencias

STAMINA_MAX = 100  # Valor máximo de estamina del jugador
