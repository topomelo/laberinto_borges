import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, TILE_SIZE, BLACK
from labyrinth import Labyrinth
from player import Player
from enemy import Minotaur
from item import Sword, Key
from npc import Ariadna
from hud import HUD


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Laberinto de Borges")
    clock = pygame.time.Clock()

    maze = Labyrinth()
    player = Player(1, 1)
    sword_pos = maze.random_floor_position()
    sword = Sword(*sword_pos)
    key = Key(0, 0)  # se coloca con Ariadna
    minotaur = Minotaur(7, 7)
    ariadna = Ariadna(13, 7)
    key.x, key.y = ariadna.x, ariadna.y
    hud = HUD(player)
    exit_pos = (13, 13)

    font = pygame.font.SysFont(None, 36)
    running = True
    won = False
    game_over = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if not won and not game_over:
            player.handle_input(maze)
            minotaur.update(player, maze)

            # Colisiones con objetos
            if not sword.collected and player.rect().colliderect(sword.rect()):
                sword.collected = True
                player.has_sword = True

            if player.rect().colliderect(ariadna.rect()):
                ariadna.interact(player, key)

            if minotaur.alive and player.rect().colliderect(minotaur.rect()):
                if player.has_sword:
                    minotaur.alive = False
                else:
                    game_over = True

            # Verificar victoria
            if (player.has_sword and player.has_key and not minotaur.alive and
                    (player.x, player.y) == exit_pos):
                won = True

        screen.fill(BLACK)
        maze.draw(screen)
        sword.draw(screen)
        if not minotaur.alive:
            pass
        else:
            minotaur.draw(screen)
        ariadna.draw(screen)
        player.draw(screen)
        hud.draw(screen)

        if won:
            msg = font.render("\u00a1Ganaste!", True, (255, 255, 0))
            screen.blit(msg, (SCREEN_WIDTH // 2 - msg.get_width() // 2, SCREEN_HEIGHT // 2))
        elif game_over:
            msg = font.render("Has muerto", True, (255, 0, 0))
            screen.blit(msg, (SCREEN_WIDTH // 2 - msg.get_width() // 2, SCREEN_HEIGHT // 2))

        pygame.display.flip()
        clock.tick(10)

    pygame.quit()


if __name__ == "__main__":
    main()
