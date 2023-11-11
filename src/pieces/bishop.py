from pieces.piece import Piece


class Bishop(Piece):
    def __init__(self, color: str, row: int, col: int, img_path: str):
        """
        Initializes the Bishop object

        Args:
            color (str): The color of the piece
            row (int): The row of the piece
            col (int): The column of the piece
            img_path (str): The path to the image of the piece

        Returns:
            None
        """
        super().__init__(color, row, col, img_path)

    def get_valid_moves(self, board: list):
        """
        Returns a list of valid moves for the bishop

        Args:
            board (list): 2D list of Piece objects representing the board

        Returns:
            list: A list of valid moves
        """
        moves = []
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]  # Diagonal directions

        for d in directions:
            for i in range(1, 8):  # Max board size is 8x8
                end_row = self.row + d[0] * i
                end_col = self.col + d[1] * i

                if 0 <= end_row < 8 and 0 <= end_col < 8:  # Check if within board
                    end_piece = board[end_row][end_col]
                    if end_piece is None:  # Empty square
                        moves.append((end_row, end_col))
                    elif end_piece.color != self.color:  # Capture opponent's piece
                        moves.append((end_row, end_col))
                        break
                    else:  # Blocked by same color piece
                        break
                else:  # Off board
                    break

        return moves
