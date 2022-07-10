"""
  Create names of pieces
"""
PAWN = "P"
KNIGHT = "N"
ROOK = "R"
BISHOP = "B"
QUEEN = "Q"
KING = "K"

BLANK = "_"  # for an empty square

"""
  Create enums for color to avoid typos, and to make more legible
"""
WHITE = "w"
BLACK = "b"


# Ranks
ONE = "1"
TWO = "2"
THREE = "3"
FOUR = "4"
FIVE = "5"
SIX = "6"
SEVEN = "7"
EIGHT = "8"

# Files
A = "a"
B = "b"
C = "c"
D = "d"
E = "e"
F = "f"
G = "g"
H = "h"


# Get the rows, and reverse dictionary of the same
RANKS_TO_ROWS = {ONE: 7, TWO: 6, THREE: 5, FOUR: 4, FIVE: 3, SIX: 2, SEVEN: 1, EIGHT: 0}
ROWS_TO_RANKS = {value: key for key, value in RANKS_TO_ROWS.items()}


# Get the columns and reverse dictionary of the same
FILES_TO_COLUMNS = {A: 0, B: 1, C: 2, D: 3, E: 4, F: 5, G: 6, H: 7}
COLUMNS_TO_FILES = {value: key for key, value in FILES_TO_COLUMNS.items()}

ROW_NAMES = {ONE: 0, TWO: 1, THREE: 2, FOUR: 3, FIVE: 4, SIX: 5, SEVEN: 6, EIGHT: 7}

# Messages
ILLEGAL_MOVE = "Illegal Move!"
BLOCKED_MOVE = "Move is blocked!"
NO_PIECE_MOVED = "No piece Moved!"
PIECE_RESTRAINED = "Opponent's piece!"
PATH_BLOCKED = "There is a piece blocking the path"
