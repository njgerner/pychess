# PyChess: A Python Chess Game

## Description
PyChess is a fully interactive chess game built in Python, using the Pygame library. It features a complete implementation of chess rules including special moves like castling, en passant, and pawn promotion. The game supports two-player mode, with an intuitive interface and turn-by-turn gameplay.

## Features
- Full chess gameplay with all standard rules
- Turn-by-turn play for two players
- Special chess moves: castling, pawn promotion, and en passant
- Check, checkmate, and stalemate detection
- Graphical user interface using Pygame

## Installation

### Prerequisites
- Python 3.10 or higher
- Pygame

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/njgerner/pychess
   ```
2. Navigate to the cloned directory:
   ```bash
   cd pychess
   ```
   
3. Install via poetry:
   ```bash
   poetry install
   ```

### Running the Game
Execute the main script to start the game:
```bash
python src/game.py
```

## How to Play
- Start the game using the command above.
- Click to select a piece and click again on a valid square to move it.
- The game follows standard chess rules for movement, captures, and special moves.
- The current player's turn is displayed on the screen.

## Contributions
Contributions to PyChess are welcome. Please ensure that your code adheres to the project's coding standards and include tests for new features.

## License
MIT
