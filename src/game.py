import os

import pygame

from board import Board
from events import EventHandler
from state import GameState

# Initialize Pygame
pygame.init()

# Game Window Constants
WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // 100  # Assuming each square is 100x100 pixels
    col = x // 100
    return row, col


def main():
    clock = pygame.time.Clock()
    board = Board()
    game_state = GameState(board)
    event_handler = EventHandler(board, game_state)

    run = True
    while run:
        clock.tick(60)
        events = pygame.event.get()
        action = event_handler.handle_events(events)  # Handle events through EventHandler

        if action == "QUIT":
            run = False

        board.draw(WIN)
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
