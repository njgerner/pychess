from pieces.piece import Piece


class King(Piece):
    def __init__(self, color: str, row: int, col: int, img_path: str):
        """
        Initializes the King object

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
        Returns a list of valid moves for the king

        Args:
            board (list): 2D list of Piece objects representing the board

        Returns:
            list: A list of valid moves
        """
        # Implement the logic for bishop's valid moves
        moves = []
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]  # All 8 directions

        for d in directions:
            end_row = self.row + d[0]
            end_col = self.col + d[1]

            if 0 <= end_row < 8 and 0 <= end_col < 8:  # Check if within board
                end_piece = board[end_row][end_col]
                if end_piece is None or end_piece.color != self.color:
                    moves.append((end_row, end_col))

        # TODO: Add logic for castling

        return moves
