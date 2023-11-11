import pygame

from board import Board


class EventHandler:
    def __init__(self, board: Board):
        self.board = board

    def handle_events(self, event_list):
        for event in event_list:
            if event.type == pygame.QUIT:
                return "QUIT"
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.handle_mouse_button_down(event)

    def handle_mouse_button_down(self, event):
        pos = pygame.mouse.get_pos()
        row, col = self.get_row_col_from_mouse(pos)
        if self.board.selected_piece:
            # Attempt to move the piece
            self.board.move_piece(self.board.selected_piece, row, col)
            self.board.selected_piece = None
        else:
            self.board.selected_piece = self.board.get_piece(row, col)

    @staticmethod
    def get_row_col_from_mouse(pos):
        x, y = pos
        row = y // 100  # Assuming each square is 100x100 pixels
        col = x // 100
        return row, col
