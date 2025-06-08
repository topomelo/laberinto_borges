import random
import pygame
from constants import TILE_SIZE, RED

class Minotaur:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.alive = True
        self.direction = random.choice([(1,0),(-1,0),(0,1),(0,-1)])
        self.detect_radius = 5

    def rect(self):
        return pygame.Rect(self.x * TILE_SIZE, self.y * TILE_SIZE, TILE_SIZE, TILE_SIZE)

    def line_of_sight(self, player, labyrinth):
        if abs(player.x - self.x) + abs(player.y - self.y) > self.detect_radius:
            return False
        if player.x == self.x:
            step = 1 if player.y > self.y else -1
            for y in range(self.y + step, player.y, step):
                if labyrinth.is_wall(self.x, y):
                    return False
            return True
        elif player.y == self.y:
            step = 1 if player.x > self.x else -1
            for x in range(self.x + step, player.x, step):
                if labyrinth.is_wall(x, self.y):
                    return False
            return True
        return False

    def update(self, player, labyrinth):
        if not self.alive:
            return
        if self.line_of_sight(player, labyrinth):
            dx = (player.x - self.x)
            dy = (player.y - self.y)
            if abs(dx) > abs(dy):
                step_x = 1 if dx > 0 else -1
                if not labyrinth.is_wall(self.x + step_x, self.y):
                    self.x += step_x
                elif dy != 0 and not labyrinth.is_wall(self.x, self.y + (1 if dy>0 else -1)):
                    self.y += 1 if dy > 0 else -1
            else:
                step_y = 1 if dy > 0 else -1
                if not labyrinth.is_wall(self.x, self.y + step_y):
                    self.y += step_y
                elif dx != 0 and not labyrinth.is_wall(self.x + (1 if dx>0 else -1), self.y):
                    self.x += 1 if dx > 0 else -1
        else:
            dx, dy = self.direction
            if labyrinth.is_wall(self.x + dx, self.y + dy):
                self.direction = random.choice([(1,0),(-1,0),(0,1),(0,-1)])
            else:
                self.x += dx
                self.y += dy

    def draw(self, surface):
        if self.alive:
            pygame.draw.rect(surface, RED, self.rect())
