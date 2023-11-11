import pygame


class Piece:
    def __init__(self, color, row, col, img_path):
        self.color = color
        self.row = row
        self.col = col
        self.img = self.load_img(img_path)

    @staticmethod
    def load_img(img_path):
        img = pygame.image.load(img_path).convert_alpha()
        return pygame.transform.scale(img, (100, 100))  # Scale the image to fit the board's cell

    def get_valid_moves(self, board):
        # This will be implemented in the specific piece subclasses
        pass

    def move(self, row, col):
        self.row = row
        self.col = col

    def draw(self, win):
        win.blit(self.img, (self.col * 100, self.row * 100))
