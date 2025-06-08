import random
import pygame
from constants import TILE_SIZE, RED

class Minotaur:
    def __init__(self, x, y):
        self.x = x  # Posición horizontal en tiles
        self.y = y  # Posición vertical en tiles
        self.alive = True  # Estado de vida del minotauro
        self.direction = random.choice([(1,0),(-1,0),(0,1),(0,-1)])  # Dirección de movimiento aleatoria
        self.detect_radius = 5  # Radio de detección en tiles

    def rect(self):
        # Devuelve el rectángulo que representa al minotauro en pantalla
        return pygame.Rect(self.x * TILE_SIZE, self.y * TILE_SIZE, TILE_SIZE, TILE_SIZE)

    def line_of_sight(self, player, labyrinth):
        # Verifica si el jugador está dentro del radio de visión y no hay paredes entre ambos
        if abs(player.x - self.x) + abs(player.y - self.y) > self.detect_radius:
            return False  # Está fuera del radio de detección

        if player.x == self.x:
            # Mismo eje vertical
            step = 1 if player.y > self.y else -1
            for y in range(self.y + step, player.y, step):
                if labyrinth.is_wall(self.x, y):  # Hay una pared en el camino
                    return False
            return True

        elif player.y == self.y:
            # Mismo eje horizontal
            step = 1 if player.x > self.x else -1
            for x in range(self.x + step, player.x, step):
                if labyrinth.is_wall(x, self.y):  # Hay una pared en el camino
                    return False
            return True

        return False  # No está alineado ni vertical ni horizontalmente

    def update(self, player, labyrinth):
        # Lógica de movimiento del minotauro por cada frame
        if not self.alive:
            return  # No hace nada si está muerto

        if self.line_of_sight(player, labyrinth):
            # Persigue al jugador si lo ve
            dx = (player.x - self.x)
            dy = (player.y - self.y)

            if abs(dx) > abs(dy):
                # Prefiere moverse horizontalmente si la distancia horizontal es mayor
                step_x = 1 if dx > 0 else -1
                if not labyrinth.is_wall(self.x + step_x, self.y):
                    self.x += step_x
                elif dy != 0 and not labyrinth.is_wall(self.x, self.y + (1 if dy > 0 else -1)):
                    self.y += 1 if dy > 0 else -1
            else:
                # Prefiere moverse verticalmente si la distancia vertical es mayor
                step_y = 1 if dy > 0 else -1
                if not labyrinth.is_wall(self.x, self.y + step_y):
                    self.y += step_y
                elif dx != 0 and not labyrinth.is_wall(self.x + (1 if dx > 0 else -1), self.y):
                    self.x += 1 if dx > 0 else -1
        else:
            # Movimiento aleatorio si no ve al jugador
            dx, dy = self.direction
            if labyrinth.is_wall(self.x + dx, self.y + dy):
                # Cambia de dirección si choca contra una pared
                self.direction = random.choice([(1,0),(-1,0),(0,1),(0,-1)])
            else:
                # Continúa en la dirección actual
                self.x += dx
                self.y += dy

    def draw(self, surface):
        # Dibuja al minotauro en la pantalla si está vivo
        if self.alive:
            pygame.draw.rect(surface, RED, self.rect())
