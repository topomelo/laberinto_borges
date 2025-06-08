# Laberinto de Borges

Este proyecto es un peque\u00f1o videojuego en Python inspirado en las vistas superiores cl\u00e1sicas de los juegos arcade. El objetivo es ayudar a Teseo a resolver el laberinto, rescatar a Ariadna y escapar.

## Requisitos
- Python 3.8 o superior
- [Pygame](https://www.pygame.org/)

Instala las dependencias con:

```bash
pip install pygame
```

## Ejecuci\u00f3n
Desde la ra\u00edz del proyecto ejecuta:

```bash
python main.py
```

## Estructura del c\u00f3digo
- `main.py`: bucle principal del juego.
- `labyrinth.py`: definici\u00f3n del laberinto.
- `player.py`: l\u00f3gica de Teseo y gesti\u00f3n de la estamina.
- `enemy.py`: IA b\u00e1sica del Minotauro.
- `npc.py`: gesti\u00f3n de Ariadna.
- `item.py`: manejo de la espada y la llave.
- `hud.py`: muestra la estamina y el inventario en pantalla.

## Controles
- Flechas: movimiento en las cuatro direcciones.
- Shift: correr (consume estamina).
- ENTER: iniciar partida desde el men\u00fa principal.
- Esc o P: abrir el men\u00fa de pausa durante la partida.
  - C: continuar.
  - R: reiniciar la partida.
  - Q: salir del juego.

## Objetivo del juego
1. Encuentra la espada de Teseo.
2. Derrota al Minotauro.
3. Localiza a Ariadna para que te entregue la llave.
4. Llega a la salida con la espada, la llave y el Minotauro derrotado.

\u00a1Buena suerte!
