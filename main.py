import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, TILE_SIZE, BLACK
from labyrinth import Labyrinth
from player import Player
from enemy import Minotaur
from item import Sword, Key
from npc import Ariadna
from hud import HUD

# ----------------------------
# Estados posibles del juego
# ----------------------------
MENU = "menu"        # Menú principal
RUNNING = "running"  # Juego en marcha
PAUSED = "paused"    # Juego pausado
WON = "won"          # El jugador ganó
GAME_OVER = "game_over"  # El jugador perdió


def initialize_game():
    """
    Crea e inicializa todos los objetos del juego:
    - Laberinto
    - Jugador
    - Espada
    - Llave
    - Minotauro
    - Ariadna
    - HUD
    - Posición de salida
    """
    maze = Labyrinth()  # Genera el laberinto
    player = Player(1, 1)  # Posición inicial del jugador
    sword_pos = maze.random_floor_position()  # Posición aleatoria para la espada
    sword = Sword(*sword_pos)  # Crea espada en esa posición
    key = Key(0, 0)  # Llave, pero se reposicionará con Ariadna
    minotaur = Minotaur(7, 7)  # Minotauro en posición fija
    ariadna = Ariadna(13, 7)  # Ariadna en posición fija
    key.x, key.y = ariadna.x, ariadna.y  # La llave se entrega con Ariadna
    hud = HUD(player)  # Interfaz de jugador
    exit_pos = (13, 13)  # Posición de salida del laberinto
    return maze, player, sword, key, minotaur, ariadna, hud, exit_pos


def draw_menu(screen, font):
    """Dibuja el menú principal"""
    screen.fill(BLACK)  # Fondo negro
    title = font.render("Laberinto de Borges", True, (255, 255, 255))  # Título
    start = font.render("ENTER - Iniciar", True, (255, 255, 255))  # Texto para comenzar
    quit_msg = font.render("Q - Salir", True, (255, 255, 255))  # Texto para salir
    # Centramos los textos en la pantalla
    screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 80))
    screen.blit(start, (SCREEN_WIDTH // 2 - start.get_width() // 2, 140))
    screen.blit(quit_msg, (SCREEN_WIDTH // 2 - quit_msg.get_width() // 2, 180))


def draw_pause_menu(screen, font):
    """Dibuja el menú de pausa"""
    screen.fill(BLACK)  # Fondo negro
    paused = font.render("Pausa", True, (255, 255, 255))
    cont = font.render("C - Continuar", True, (255, 255, 255))
    restart = font.render("R - Reiniciar", True, (255, 255, 255))
    quit_msg = font.render("Q - Salir", True, (255, 255, 255))
    # Centramos los textos en la pantalla
    screen.blit(paused, (SCREEN_WIDTH // 2 - paused.get_width() // 2, 80))
    screen.blit(cont, (SCREEN_WIDTH // 2 - cont.get_width() // 2, 140))
    screen.blit(restart, (SCREEN_WIDTH // 2 - restart.get_width() // 2, 180))
    screen.blit(quit_msg, (SCREEN_WIDTH // 2 - quit_msg.get_width() // 2, 220))


def main():
    pygame.init()  # Inicializa todos los módulos de Pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Crea la ventana principal
    pygame.display.set_caption("Laberinto de Borges")  # Título de la ventana
    clock = pygame.time.Clock()  # Objeto para controlar los FPS
    font = pygame.font.SysFont(None, 36)  # Fuente por defecto

    # Creamos las entidades del juego y el estado inicial
    maze, player, sword, key, minotaur, ariadna, hud, exit_pos = initialize_game()
    state = MENU  # Estado inicial en el menú
    running = True  # Bandera para mantener el juego en ejecución

    # Bucle principal del juego
    while running:
        for event in pygame.event.get():  # Procesa todos los eventos
            if event.type == pygame.QUIT:
                running = False  # Cierra el juego
            elif event.type == pygame.KEYDOWN:
                if state == MENU:
                    if event.key == pygame.K_RETURN:  # Comenzar el juego
                        state = RUNNING
                    elif event.key in (pygame.K_q, pygame.K_ESCAPE):  # Salir
                        running = False
                elif state == RUNNING:
                    if event.key in (pygame.K_ESCAPE, pygame.K_p):  # Pausar juego
                        state = PAUSED
                elif state == PAUSED:
                    if event.key == pygame.K_c:  # Continuar
                        state = RUNNING
                    elif event.key == pygame.K_r:  # Reiniciar
                        maze, player, sword, key, minotaur, ariadna, hud, exit_pos = initialize_game()
                        state = RUNNING
                    elif event.key in (pygame.K_q, pygame.K_ESCAPE):  # Salir
                        running = False
                elif state in (WON, GAME_OVER):  # Reinicio o salida tras final
                    if event.key == pygame.K_r:
                        maze, player, sword, key, minotaur, ariadna, hud, exit_pos = initialize_game()
                        state = RUNNING
                    elif event.key in (pygame.K_q, pygame.K_ESCAPE):
                        running = False

        # Si el juego está en marcha, actualizamos la lógica
        if state == RUNNING:
            player.handle_input(maze)  # Procesa entrada del jugador
            minotaur.update(player, maze)  # Actualiza comportamiento del enemigo

            # Verifica si el jugador recoge la espada
            if not sword.collected and player.rect().colliderect(sword.rect()):
                sword.collected = True
                player.has_sword = True

            # Interacción con Ariadna para recibir la llave
            if player.rect().colliderect(ariadna.rect()):
                ariadna.interact(player, key)

            # Si el jugador se encuentra con el minotauro
            if minotaur.alive and player.rect().colliderect(minotaur.rect()):
                if player.has_sword:
                    minotaur.alive = False  # El jugador mata al minotauro
                else:
                    state = GAME_OVER  # El jugador muere

            # Verifica si se cumplen las condiciones para ganar
            if (
                player.has_sword
                and player.has_key
                and not minotaur.alive
                and (player.x, player.y) == exit_pos
            ):
                state = WON

        # Dibujamos según el estado actual
        if state == MENU:
            draw_menu(screen, font)
        elif state == PAUSED:
            draw_pause_menu(screen, font)
        else:
            screen.fill(BLACK)  # Limpia pantalla
            maze.draw(screen)  # Dibuja laberinto
            sword.draw(screen)  # Dibuja espada
            if minotaur.alive:
                minotaur.draw(screen)  # Dibuja minotauro si está vivo
            ariadna.draw(screen)  # Dibuja a Ariadna
            player.draw(screen)  # Dibuja al jugador
            hud.draw(screen)  # Dibuja interfaz

            # Mensajes de fin de juego
            if state == WON:
                msg = font.render("\u00a1Ganaste!", True, (255, 255, 0))
                screen.blit(msg, (SCREEN_WIDTH // 2 - msg.get_width() // 2, SCREEN_HEIGHT // 2))
            elif state == GAME_OVER:
                msg = font.render("Has muerto", True, (255, 0, 0))
                screen.blit(msg, (SCREEN_WIDTH // 2 - msg.get_width() // 2, SCREEN_HEIGHT // 2))

        pygame.display.flip()  # Actualiza la pantalla
        clock.tick(10)  # Limita la velocidad de fotogramas

    pygame.quit()  # Finaliza Pygame


if __name__ == "__main__":
    main()  # Ejecuta el juego
