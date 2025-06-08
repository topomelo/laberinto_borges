import random
import pygame
from constants import TILE_SIZE, MAZE_WIDTH, MAZE_HEIGHT, SCREEN_WIDTH, SCREEN_HEIGHT, GRAY, BLACK

# Mapa del laberinto: X son paredes, . son caminos
LAYOUT = [
    "XXXXXXXXXXXXXXX",
    "X.............X",
    "X.XXXXX.XXXXX.X",
    "X.X...X.X...X.X",
    "X.X.X.X.X.X.X.X",
    "X...X.....X...X",
    "XXXXX.XXX.XXX.X",
    "X.....X.......X",
    "X.XXX.X.XXXXX.X",
    "X...X...X.....X",
    "XXX.XXXXX.X.X.X",
    "X.....X...X.X.X",
    "X.XXXXX.X.X.X.X",
    "X.......X.....X",
    "XXXXXXXXXXXXXXX",
]

class Labyrinth:
    def __init__(self):
        self.tiles = [list(row) for row in LAYOUT]

    def draw(self, surface):
        for y, row in enumerate(self.tiles):
            for x, char in enumerate(row):
                rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                if char == 'X':
                    pygame.draw.rect(surface, GRAY, rect)
                else:
                    pygame.draw.rect(surface, BLACK, rect)

    def is_wall(self, x, y):
        if x < 0 or x >= MAZE_WIDTH or y < 0 or y >= MAZE_HEIGHT:
            return True
        return self.tiles[y][x] == 'X'

    def random_floor_position(self):
        while True:
            x = random.randint(1, MAZE_WIDTH - 2)
            y = random.randint(1, MAZE_HEIGHT - 2)
            if not self.is_wall(x, y):
                return x, y
