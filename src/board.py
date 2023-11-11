import pygame

from logger import get_logger
from pieces.bishop import Bishop
from pieces.king import King
from pieces.knight import Knight
from pieces.pawn import Pawn
from pieces.piece import Piece
from pieces.queen import Queen
from pieces.rook import Rook

logger = get_logger(__name__)


class Board:
    def __init__(self):
        self._image_path = "assets/images"
        self.selected_piece = None
        # Board setup
        self.pieces = [
            [
                Rook("black", 0, 0, f"{self._image_path}/pieces/b_rook.png"),
                Knight("black", 0, 1, f"{self._image_path}/pieces/b_knight.png"),
                Bishop("black", 0, 2, f"{self._image_path}/pieces/b_bishop.png"),
                Queen("black", 0, 3, f"{self._image_path}/pieces/b_queen.png"),
                King("black", 0, 4, f"{self._image_path}/pieces/b_king.png"),
                Bishop("black", 0, 5, f"{self._image_path}/pieces/b_bishop.png"),
                Knight("black", 0, 6, f"{self._image_path}/pieces/b_knight.png"),
                Rook("black", 0, 7, f"{self._image_path}/pieces/b_rook.png"),
            ],
            [
                Pawn("black", 1, 0, f"{self._image_path}/pieces/b_pawn.png"),
                Pawn("black", 1, 1, f"{self._image_path}/pieces/b_pawn.png"),
                Pawn("black", 1, 2, f"{self._image_path}/pieces/b_pawn.png"),
                Pawn("black", 1, 3, f"{self._image_path}/pieces/b_pawn.png"),
                Pawn("black", 1, 4, f"{self._image_path}/pieces/b_pawn.png"),
                Pawn("black", 1, 5, f"{self._image_path}/pieces/b_pawn.png"),
                Pawn("black", 1, 6, f"{self._image_path}/pieces/b_pawn.png"),
                Pawn("black", 1, 7, f"{self._image_path}/pieces/b_pawn.png"),
            ],
            [None] * 8,
            [None] * 8,
            [None] * 8,
            [None] * 8,
            [
                Pawn("white", 6, 0, f"{self._image_path}/pieces/w_pawn.png"),
                Pawn("white", 6, 1, f"{self._image_path}/pieces/w_pawn.png"),
                Pawn("white", 6, 2, f"{self._image_path}/pieces/w_pawn.png"),
                Pawn("white", 6, 3, f"{self._image_path}/pieces/w_pawn.png"),
                Pawn("white", 6, 4, f"{self._image_path}/pieces/w_pawn.png"),
                Pawn("white", 6, 5, f"{self._image_path}/pieces/w_pawn.png"),
                Pawn("white", 6, 6, f"{self._image_path}/pieces/w_pawn.png"),
                Pawn("white", 6, 7, f"{self._image_path}/pieces/w_pawn.png"),
            ],
            [
                Rook("white", 7, 0, f"{self._image_path}/pieces/w_rook.png"),
                Knight("white", 7, 1, f"{self._image_path}/pieces/w_knight.png"),
                Bishop("white", 7, 2, f"{self._image_path}/pieces/w_bishop.png"),
                Queen("white", 7, 3, f"{self._image_path}/pieces/w_queen.png"),
                King("white", 7, 4, f"{self._image_path}/pieces/w_king.png"),
                Bishop("white", 7, 5, f"{self._image_path}/pieces/w_bishop.png"),
                Knight("white", 7, 6, f"{self._image_path}/pieces/w_knight.png"),
                Rook("white", 7, 7, f"{self._image_path}/pieces/w_rook.png"),
            ]

        ]

    @staticmethod
    def highlight_moves(win: pygame.Surface, moves: list):
        """
        Highlight the valid moves for the selected piece

        Args:
            win (pygame.Surface): The window to draw on
            moves (list): A list of valid moves

        Returns:
            None
        """
        for move in moves:
            row, col = move
            # highlight the valid moves by highlight the background of the square the piece can move to yellow
            pygame.draw.rect(win, (255, 255, 0), (col * 100, row * 100, 100, 100), 5)

    def highlight_selected(self, win: pygame.Surface):
        """
        Highlight the selected piece

        Args:
            win (pygame.Surface): The window to draw on

        Returns:
            None
        """
        if self.selected_piece:
            row, col = self.selected_piece.row, self.selected_piece.col
            # highlight the selected piece by darkening the outline of the square the piece is on
            pygame.draw.rect(win, (0, 0, 0), (col * 100, row * 100, 100, 100), 5)

    def draw(self, win: pygame.Surface):
        """
        Draw the board and the pieces

        Args:
            win (pygame.Surface): The window to draw on

        Returns:
            None
        """
        # Draw the chessboard
        win.fill(pygame.Color('white'))  # Set background color
        for row in range(8):
            for col in range(8):
                color = pygame.Color('white') if (row + col) % 2 == 0 else pygame.Color('gray')
                pygame.draw.rect(win, color, (row * 100, col * 100, 100, 100))

        # Draw the pieces
        for row in self.pieces:
            for piece in row:
                if piece:
                    piece.draw(win)

        if self.selected_piece:
            self.highlight_selected(win)
            self.highlight_moves(win, self.selected_piece.get_valid_moves(self.pieces))

    def get_piece(self, row: int, col: int) -> Piece | None:
        """
        Get the piece at the given row and col

        Args:
            row (int): The row of the piece
            col (int): The column of the piece

        Returns:
            Piece: The piece at the given row and col
        """
        logger.debug(f"Getting piece at {row}, {col}")
        # check if the row and col are within the board
        if 0 <= row < 8 and 0 <= col < 8:
            # check if there is a piece at the given row and col
            if self.pieces[row][col]:
                return self.pieces[row][col]
        return None

    def apply_move(self, move: tuple):
        """
        Apply the given move to the board

        Args:
            move (tuple): The move to apply

        Returns:
            None
        """
        logger.debug(f"Applying move {move}")
        start_row, start_col, end_row, end_col = move
        start_piece = self.get_piece(start_row, start_col)
        end_piece = self.get_piece(end_row, end_col)

        if start_piece and start_piece.color == "white":
            # check if the end piece is an opponent's piece
            if end_piece and end_piece.color == "black":
                # remove the opponent's piece
                self.pieces[end_row][end_col] = None
            # move the piece
            self.move_piece(start_piece, end_row, end_col)
        else:
            logger.warning("Invalid move")

    def move_piece(self, piece: Piece, row: int, col: int):
        """
        Move the given piece to the given row and col

        Args:
            piece (Piece): The piece to move
            row (int): The row to move the piece to
            col (int): The column to move the piece to

        Returns:
            None
        """
        logger.debug(f"Moving {piece} to {row}, {col}")
        self.pieces[piece.row][piece.col], self.pieces[row][col] = self.pieces[row][col], self.pieces[piece.row][
            piece.col]
        piece.move(row, col)

    def select_piece(self, row: int, col: int):
        """
        Select the piece at the given row and col

        Args:
            row (int): The row of the piece to select
            col (int): The column of the piece to select

        Returns:
            None
        """
        logger.debug(f"Selecting piece at {row}, {col}")
        self.selected_piece = self.get_piece(row, col)
