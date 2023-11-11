from pieces.piece import Piece


class Pawn(Piece):
    def __init__(self, color: str, row: int, col: int, img_path: str):
        """
        Initializes the Pawn object

        Args:
            color (str): The color of the piece
            row (int): The row of the piece
            col (int): The column of the piece
            img_path (str): The path to the image of the piece

        Returns:
            None
        """
        super().__init__(color, row, col, img_path)

    def get_valid_moves(self, board: list) -> list:
        """
        Returns a list of valid moves for the pawn

        Args:
            board (list): 2D list of Piece objects representing the board

        Returns:
            list: A list of valid moves
        """
        moves = []
        direction = 1 if self.color == 'black' else -1  # Determines movement direction based on color
        start_row = 1 if self.color == 'black' else 6  # Starting row depending on color

        # Forward move
        if 0 <= self.row + direction < 8:  # Check if move is within board bounds
            if board[self.row + direction][self.col] is None:  # Check if square in front is empty
                moves.append((self.row + direction, self.col))

                # Double forward move from start position
                if self.row == start_row and board[self.row + 2 * direction][self.col] is None:
                    moves.append((self.row + 2 * direction, self.col))

        # Captures
        for dx in [-1, 1]:  # Check diagonals for capture
            if 0 <= self.col + dx < 8:  # Check if diagonal move is within board bounds
                if board[self.row + direction][self.col + dx] is not None:
                    if board[self.row + direction][self.col + dx].color != self.color:
                        moves.append((self.row + direction, self.col + dx))

        # TODO: Implement En Passant logic

        return moves
