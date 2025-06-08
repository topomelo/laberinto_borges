import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, TILE_SIZE, BLACK
from labyrinth import Labyrinth
from player import Player
from enemy import Minotaur
from item import Sword, Key
from npc import Ariadna
from hud import HUD


# Estados del juego
MENU = "menu"
RUNNING = "running"
PAUSED = "paused"
WON = "won"
GAME_OVER = "game_over"


def initialize_game():
    """Crea todas las entidades y devuelve los objetos principales."""
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
    return maze, player, sword, key, minotaur, ariadna, hud, exit_pos


def draw_menu(screen, font):
    screen.fill(BLACK)
    title = font.render("Laberinto de Borges", True, (255, 255, 255))
    start = font.render("ENTER - Iniciar", True, (255, 255, 255))
    quit_msg = font.render("Q - Salir", True, (255, 255, 255))
    screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 80))
    screen.blit(start, (SCREEN_WIDTH // 2 - start.get_width() // 2, 140))
    screen.blit(quit_msg, (SCREEN_WIDTH // 2 - quit_msg.get_width() // 2, 180))


def draw_pause_menu(screen, font):
    screen.fill(BLACK)
    paused = font.render("Pausa", True, (255, 255, 255))
    cont = font.render("C - Continuar", True, (255, 255, 255))
    restart = font.render("R - Reiniciar", True, (255, 255, 255))
    quit_msg = font.render("Q - Salir", True, (255, 255, 255))
    screen.blit(paused, (SCREEN_WIDTH // 2 - paused.get_width() // 2, 80))
    screen.blit(cont, (SCREEN_WIDTH // 2 - cont.get_width() // 2, 140))
    screen.blit(restart, (SCREEN_WIDTH // 2 - restart.get_width() // 2, 180))
    screen.blit(quit_msg, (SCREEN_WIDTH // 2 - quit_msg.get_width() // 2, 220))



def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Laberinto de Borges")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 36)

    maze, player, sword, key, minotaur, ariadna, hud, exit_pos = initialize_game()
    state = MENU
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if state == MENU:
                    if event.key == pygame.K_RETURN:
                        state = RUNNING
                    elif event.key in (pygame.K_q, pygame.K_ESCAPE):
                        running = False
                elif state == RUNNING:
                    if event.key in (pygame.K_ESCAPE, pygame.K_p):
                        state = PAUSED
                elif state == PAUSED:
                    if event.key == pygame.K_c:
                        state = RUNNING
                    elif event.key == pygame.K_r:
                        maze, player, sword, key, minotaur, ariadna, hud, exit_pos = initialize_game()
                        state = RUNNING
                    elif event.key in (pygame.K_q, pygame.K_ESCAPE):
                        running = False
                elif state in (WON, GAME_OVER):
                    if event.key == pygame.K_r:
                        maze, player, sword, key, minotaur, ariadna, hud, exit_pos = initialize_game()
                        state = RUNNING
                    elif event.key in (pygame.K_q, pygame.K_ESCAPE):
                        running = False

        if state == RUNNING:
            player.handle_input(maze)
            minotaur.update(player, maze)

            if not sword.collected and player.rect().colliderect(sword.rect()):
                sword.collected = True
                player.has_sword = True

            if player.rect().colliderect(ariadna.rect()):
                ariadna.interact(player, key)

            if minotaur.alive and player.rect().colliderect(minotaur.rect()):
                if player.has_sword:
                    minotaur.alive = False
                else:
                    state = GAME_OVER

            if (
                player.has_sword
                and player.has_key
                and not minotaur.alive
                and (player.x, player.y) == exit_pos
            ):
                state = WON

        if state == MENU:
            draw_menu(screen, font)
        elif state == PAUSED:
            draw_pause_menu(screen, font)
        else:
            screen.fill(BLACK)
            maze.draw(screen)
            sword.draw(screen)
            if minotaur.alive:
                minotaur.draw(screen)
            ariadna.draw(screen)
            player.draw(screen)
            hud.draw(screen)

            if state == WON:
                msg = font.render("\u00a1Ganaste!", True, (255, 255, 0))
                screen.blit(msg, (SCREEN_WIDTH // 2 - msg.get_width() // 2, SCREEN_HEIGHT // 2))
            elif state == GAME_OVER:
                msg = font.render("Has muerto", True, (255, 0, 0))
                screen.blit(msg, (SCREEN_WIDTH // 2 - msg.get_width() // 2, SCREEN_HEIGHT // 2))

        pygame.display.flip()
        clock.tick(10)

    pygame.quit()


if __name__ == "__main__":
    main()