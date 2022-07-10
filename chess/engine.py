import uuid
from chess.constants import *  # noqa
from chess.pieces import Bishop, King, Knight, Pawn, Queen, Rook




class ChessBoard:
    """
        This places the pieces on the board matrix.
        We'll use a 2-D List to do draw the pieces on the board


        ### THE STRUCTURE OF THE BOARD
        `board: List[List[Piece]]`: The board object
        `initialize()`: To load the board and place `Piece`s on it
        `move`: A move, takes two arguments, `from_pos` and `to_pos`, each an `Iterable`
        
        ``` py
              [1]       [2]      [3]     [4]      [5]      [6]      [7]      [8]

        [H]  ['wR',    'wN',    'wB',    'wQ',    'wK',    'wB',    'wN',    'wR']

        [G]  ['wP',    'wP',    'wP',    'wP',    'wP',    'wP',    'wP',    'wP']

        [F]  ['__',    '__',    '__',    '__',    '__',    '__',    '__',    '__']

        [E]  ['__',    '__',    '__',    '__',    '__',    '__',    '__',    '__']

        [D]  ['__',    '__',    '__',    '__',    '__',    '__',    '__',    '__']

        [C]  ['__',    '__',    '__',    '__',    '__',    '__',    '__',    '__']

        [B]  ['bP',    'bP',    'bP',    'bP',    'bP',    'bP',    'bP',    'bP']

        [A]  ['bR',    'bN',    'bB',    'bQ',    'bK',    'bB',    'bN',    'bR']
        ```

        
    """

    def __init__(self) -> None:
        self.board = [
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
        ]


        # White Pieces
        self.board[7][0] = Rook(True)
        self.board[7][1] = Knight(True)
        self.board[7][2] = Bishop(True)
        self.board[7][3] = Queen(True)
        self.board[7][4] = King(True)
        self.board[7][5] = Bishop(True)
        self.board[7][6] = Knight(True)
        self.board[7][7] = Rook(True)

        # Add white pawns on the next row
        for pos in range(8):
            self.board[6][pos] = Pawn(True)


        # Black Pieces
        self.board[0][0] = Rook(False)
        self.board[0][1] = Knight(False)
        self.board[0][2] = Bishop(False)
        self.board[0][3] = Queen(False)
        self.board[0][4] = King(False)
        self.board[0][5] = Bishop(False)
        self.board[0][6] = Knight(False)
        self.board[0][7] = Rook(False)

        # Place the black pawns
        for pos in range(8):
            self.board[1][pos] = Pawn(False)
        

    def __str__(self):
        """
        Prints the current state of the board.
        """

        buffer = ""
        for i in range(33):
            buffer += "*"
        print(buffer)
        for i in range(len(self.board)):
            tmp_str = "|"
            for j in self.board[i]:
                
                if j == None or j.name == 'GP':
                    tmp_str += "   |"
                elif len(j.name) == 2:
                    tmp_str += (" " + str(j) + "|")
                else:
                    tmp_str += (f" {WHITE if j.color else BLACK}" + str(j) + " |")
            print(tmp_str)
        buffer = ""
        for i in range(33):
            buffer += "*"
        print(buffer)
        return buffer


class ChessEngine:
    """
    This is where the Game Play is handled.

    Takes a `ChessBoard`: The board, `white_to_play`: To switch players


    Methods
    -----

    `move(initial_pos, destination)`: Moves a piece from initial_pos to the destination based on `is_valid_move()` of the piece.
    `promote(position)`: Promotes a pawn once it's reached opponent's side

    """


    def __init__(self) -> None:
        self.white_to_play = True
        self.board = ChessBoard()
        self.moves_history = []
        self.captures = []


    def make_move(self, initial_pos, destination):
        if self.board.board[initial_pos[0]][initial_pos[1]] == None:
            print(NO_PIECE_MOVED)
            return


        # In case you accidentally pick an opponent's piece
        selected_piece = self.board.board[initial_pos[0]][initial_pos[1]]
        if self.white_to_play != selected_piece.color:
            print(PIECE_RESTRAINED)
            return


        # Check if a piece is blocking the path
        target_piece = self.board.board[destination[0]][destination[1]]
        is_target = target_piece != None

        if is_target and (self.board[initial_pos[0]][initial_pos[1]].color == target_piece.color):
            print(PATH_BLOCKED)
            return


        # Capture the piece
        if target_piece != None:
            self.captures.append(target_piece)

        # Move the piece selected to the destination
        self.board.board[destination[0]][destination[1]] = selected_piece

        # log the move
        self.moves_history.append([[initial_pos[0], initial_pos[1]], [destination[0], destination[1]]])

        self.board.board[initial_pos[0]][initial_pos[1]] = None
        print(f"{WHITE if selected_piece.color else BLACK}{selected_piece} moved.")


        # Switch players
        self.white_to_play = not self.white_to_play
