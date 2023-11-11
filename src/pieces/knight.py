from pieces.piece import Piece


class Knight(Piece):
    def __init__(self, color: str, row: int, col: int, img_path: str):
        """
        Initializes the Knight object

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
        Returns a list of valid moves for the knight

        Args:
            board (list): 2D list of Piece objects representing the board

        Returns:
            list: A list of valid moves
        """
        # Implement the logic for bishop's valid moves
        moves = []
        move_offsets = [
            (-2, -1), (-2, 1),  # Upwards L-shapes
            (-1, -2), (-1, 2),  # Left and right L-shapes
            (1, -2), (1, 2),  # Left and right L-shapes
            (2, -1), (2, 1)  # Downwards L-shapes
        ]

        for offset in move_offsets:
            end_row = self.row + offset[0]
            end_col = self.col + offset[1]

            if 0 <= end_row < 8 and 0 <= end_col < 8:  # Check if move is within board bounds
                end_piece = board[end_row][end_col]
                if end_piece is None or end_piece.color != self.color:
                    moves.append((end_row, end_col))

        return moves
