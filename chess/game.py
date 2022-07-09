from chess.constants import *
import uuid


class Piece:
    """
    This holds a piece and tracks it's position on the board
    """

    def __init__(self, color, row, column, piece_type, initial_pos) -> None:
        self.color = color
        self.row = row
        self.column = column
        self.type = piece_type
        self.initial_pos = initial_pos
        self.current_position = [self.row, self.column]

    def __str__(self) -> str:
        return f"{self.color}{self.type}"

class Move:
    """
    A move made by each of the chess pieces on the board
    """

    def __init__(self, start_position, end_position, board):
        # Starting position on the board
        self.start_row = start_position[1]
        self.start_col = start_position[0]

        # Destination on the board
        self.end_row = end_position[1]
        self.end_col = end_position[0]

        # Keep track of the original position of the moved piece
        self.moved_piece = board[self.start_row][self.start_col]

        # Keep track of the destination of the piece
        self.captured_piece = board[self.end_row][self.end_col]

        # Track every move
        self.move_index = (
            f"{self.start_row}{self.start_col}{self.end_row}{self.end_col}"
        )

        print(self.move_index)

    # def __str__(self) -> str:
    #     return f"{self.captured_piece} {self.moved_piece}"

    # Prevent same row/column combination
    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Move):
            return self.move_index == __o.move_index
        return False

    def get_notation(self):
        """
        Will return a formatted position of the piece on the board
        Eg: Move from e1 >> d4 will return e1d4
        """

        return self.get_chess_rank_file_notation(
            row=self.start_row, column=self.start_col
        ) + self.get_chess_rank_file_notation(row=self.end_row, column=self.end_col)

    def get_chess_rank_file_notation(self, row, column):
        """
        Returns a nicely formatted string of the position on the board
        eg: e3
        """
        return COLUMNS_TO_FILES[column] + ROWS_TO_RANKS[row]


class GameBoard:
    """
    BOARD OVERVIEW

    `'__'` represents an empty slot

    ```py
         [A]       [B]        [C]     [D]      [E]      [F]      [G]      [H]

    [8]  ['bR',    'bN',    'bB',    'bQ',    'bK',    'bB',    'bN',    'bR']

    [7]  ['bP',    'bP',    'bP',    'bP',    'bP',    'bP',    'bP',    'bP']

    [6]  ['__',    '__',    '__',    '__',    '__',    '__',    '__',    '__']

    [5]  ['__',    '__',    '__',    '__',    '__',    '__',    '__',    '__']

    [4]  ['__',    '__',    '__',    '__',    '__',    '__',    '__',    '__']

    [3]  ['__',    '__',    '__',    '__',    '__',    '__',    '__',    '__']

    [2]  ['wP',    'wP',    'wP',    'wP',    'wP',    'wP',    'wP',    'wP']

    [1]  ['wR',    'wN',    'wB',    'wQ',    'wK',    'wB',    'wN',    'wR']
    ```

    """

    def __init__(self):
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
        self.white_to_move = True
        self.moves_history = []
        self.captured_pieces = []
        self.initialize()

    # Place the pieces
    def initialize(self):
        self.board = [
            [
                Piece(
                    color=WHITE, row=0, column=0, initial_pos=[0, 0], piece_type=ROOK
                ),
                Piece(
                    color=WHITE, row=0, column=1, initial_pos=[0, 1], piece_type=KNIGHT
                ),
                Piece(
                    color=WHITE, row=0, column=2, initial_pos=[0, 2], piece_type=BISHOP
                ),
                Piece(
                    color=WHITE, row=0, column=3, initial_pos=[0, 3], piece_type=QUEEN
                ),
                Piece(
                    color=WHITE, row=0, column=4, initial_pos=[0, 4], piece_type=KING
                ),
                Piece(
                    color=WHITE, row=0, column=5, initial_pos=[0, 5], piece_type=BISHOP
                ),
                Piece(
                    color=WHITE, row=0, column=6, initial_pos=[0, 6], piece_type=KNIGHT
                ),
                Piece(
                    color=WHITE, row=0, column=7, initial_pos=[0, 7], piece_type=ROOK
                ),
            ],
            [
                Piece(
                    color=WHITE, row=1, column=0, initial_pos=[1, 0], piece_type=PAWN
                ),
                Piece(
                    color=WHITE, row=1, column=1, initial_pos=[1, 1], piece_type=PAWN
                ),
                Piece(
                    color=WHITE, row=1, column=2, initial_pos=[1, 2], piece_type=PAWN
                ),
                Piece(
                    color=WHITE, row=1, column=3, initial_pos=[1, 3], piece_type=PAWN
                ),
                Piece(
                    color=WHITE, row=1, column=4, initial_pos=[1, 4], piece_type=PAWN
                ),
                Piece(
                    color=WHITE, row=1, column=5, initial_pos=[1, 5], piece_type=PAWN
                ),
                Piece(
                    color=WHITE, row=1, column=6, initial_pos=[1, 6], piece_type=PAWN
                ),
                Piece(
                    color=WHITE, row=1, column=7, initial_pos=[1, 7], piece_type=PAWN
                ),
            ],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [
                Piece(
                    color=BLACK, row=6, column=0, initial_pos=[6, 0], piece_type=PAWN
                ),
                Piece(
                    color=BLACK, row=6, column=1, initial_pos=[6, 1], piece_type=PAWN
                ),
                Piece(
                    color=BLACK, row=6, column=2, initial_pos=[6, 2], piece_type=PAWN
                ),
                Piece(
                    color=BLACK, row=6, column=3, initial_pos=[6, 3], piece_type=PAWN
                ),
                Piece(
                    color=BLACK, row=6, column=4, initial_pos=[6, 4], piece_type=PAWN
                ),
                Piece(
                    color=BLACK, row=6, column=5, initial_pos=[6, 5], piece_type=PAWN
                ),
                Piece(
                    color=BLACK, row=6, column=6, initial_pos=[6, 6], piece_type=PAWN
                ),
                Piece(
                    color=BLACK, row=6, column=7, initial_pos=[6, 7], piece_type=PAWN
                ),
            ],
            [
                Piece(
                    color=BLACK, row=7, column=0, initial_pos=[7, 0], piece_type=ROOK
                ),
                Piece(
                    color=BLACK, row=7, column=1, initial_pos=[7, 1], piece_type=KNIGHT
                ),
                Piece(
                    color=BLACK, row=7, column=2, initial_pos=[7, 2], piece_type=BISHOP
                ),
                Piece(
                    color=BLACK, row=7, column=3, initial_pos=[7, 3], piece_type=QUEEN
                ),
                Piece(
                    color=BLACK, row=7, column=4, initial_pos=[7, 4], piece_type=KING
                ),
                Piece(
                    color=BLACK, row=7, column=5, initial_pos=[7, 5], piece_type=BISHOP
                ),
                Piece(
                    color=BLACK, row=7, column=6, initial_pos=[7, 6], piece_type=KNIGHT
                ),
                Piece(
                    color=BLACK, row=7, column=7, initial_pos=[7, 7], piece_type=ROOK
                ),
            ],
        ]

    def get_board(self):
        return self.board

    # Move a piece
    def make_move(self, move):

        if self.board[move.start_row][move.start_col] == None:
            return ILLEGAL_MOVE

        else:

            if move in self.get_legal_moves():
                self.board[move.start_row][move.start_col] = None
                self.board[move.end_row][move.end_col] = move.moved_piece

                # Capture a piece
                if self.board[move.end_row][move.end_col] != None:
                    self.captured_pieces.append(self.board[move.end_row][move.end_col])
                    self.board[move.end_row][move.end_col] = move.moved_piece

                # Save move to the moves_history and swap players
                self.moves_history.append(move)
                self.white_to_move = not self.white_to_move
                return move.get_notation()
            else:
                return (
                    ILLEGAL_MOVE
                    + f"{[move.start_row, move.start_col]} {[move.end_row, move.end_col]}"
                )

    # Undo a move
    def undo_move(self):
        # Only undo a move if moves previous moves exist
        if len(self.moves_history) != 0:
            # make move to be the previous move
            move = self.moves_history.pop()
            print(move)
            self.board[move.start_row][move.start_col] = move.moved_piece
            self.board[move.end_row][move.end_col] = move.captured_piece

    def get_legal_moves(self):
        self.legal_moves = []

        for row in range(len(self.board)):
            for column in range(
                len(self.board[row])
            ):  # Loop through each column within a row
                turn = self.board[row][column].__str__()[
                    0
                ]  # returns an value like 'wR'

                # Check who's turn it is to play
                if (turn == "w" and self.white_to_move) or (
                    turn == "b" and not self.white_to_move
                ):
                    piece = self.board[row][
                        column
                    ].type  # Get the piece type eg 'R' for ROOK

                    # Create legal moves for all pieces
                    if piece == PAWN:
                        self.get_pawn_moves(row, column, self.legal_moves)

                    if piece == ROOK:
                        self.get_rook_moves(row, column, self.legal_moves)

                    if piece == KNIGHT:
                        self.get_knight_moves(row, column, self.legal_moves)

                    if piece == BISHOP:
                        self.get_bishop_moves(row, column, self.legal_moves)

                    if (
                        piece == QUEEN
                    ):  # Easiest to implement, just combine bishop and rook moves
                        self.get_queen_moves(row, column, self.legal_moves)

                    if piece == KING:
                        self.get_king_moves(row, column, self.legal_moves)

        return self.legal_moves

    def get_rook_moves(self, row, column, legal_moves):
        pass

    def get_knight_moves(self, row, column, legal_moves):
        pass

    def get_bishop_moves(self, row, column, legal_moves):
        pass

    def get_queen_moves(self, row, column, legal_moves):
        pass

    def get_king_moves(self, row, column, legal_moves):
        pass

    # Legal moves by the pieces
    def get_pawn_moves(self, row, column, legal_moves):

        # If it's white's turn
        if (
            self.board[row][column].__str__()[0] == WHITE
        ):  # white pawns start at 2nd row [n][1]
            # print(isinstance(self.board[row - 3][column], Piece))
            if not isinstance(self.board[row + 1][column], Piece):
                move = Move(
                    start_position=(row, column),
                    end_position=(row + 1, column),
                    board=self.board,
                )
                legal_moves.append(move)

            if row == 1 and (
                self.board[row + 2][column] == None
            ):  # First pawn move (Optional 2 step jump)
                move = Move(
                    start_position=(row, column),
                    end_position=(row + 2, column),
                    board=self.board,
                )
                legal_moves.append(move)

            # Ability to capture enemy
            if column - 1 >= 0:  # Left
                if self.board[row + 1][column - 1].__str__()[0] == BLACK:
                    legal_moves.append(
                        Move((row + 1, column - 1), (row + 2, column), self.board)
                    )

            if column + 1 <= 7:  # Right
                if self.board[row + 1][column - 1].__str__()[0] == BLACK:
                    legal_moves.append(
                        Move((row + 1, column - 1), (row + 1, column - 1), self.board)
                    )

        else:
            if not isinstance(self.board[row - 1][column], Piece):
                move = Move(
                    start_position=(row, column),
                    end_position=(row - 1, column),
                    board=self.board,
                )
                legal_moves.append(move)

            if row == 1 and (
                self.board[row - 2][column] == None
            ):  # First pawn move (Optional 2 step jump)
                move = Move(
                    start_position=(row, column),
                    end_position=(row - 2, column),
                    board=self.board,
                )
                legal_moves.append(move)



class Board:

    """
    BOARD OVERVIEW

    `'__'` represents an empty slot \n

    ```py
         [A]       [B]        [C]     [D]      [E]      [F]      [G]      [H]

    [8]  ['bR',    'bN',    'bB',    'bQ',    'bK',    'bB',    'bN',    'bR']

    [7]  ['bP',    'bP',    'bP',    'bP',    'bP',    'bP',    'bP',    'bP']

    [6]  ['__',    '__',    '__',    '__',    '__',    '__',    '__',    '__']

    [5]  ['__',    '__',    '__',    '__',    '__',    '__',    '__',    '__']

    [4]  ['__',    '__',    '__',    '__',    '__',    '__',    '__',    '__']

    [3]  ['__',    '__',    '__',    '__',    '__',    '__',    '__',    '__']

    [2]  ['wP',    'wP',    'wP',    'wP',    'wP',    'wP',    'wP',    'wP']

    [1]  ['wR',    'wN',    'wB',    'wQ',    'wK',    'wB',    'wN',    'wR']


    p
    [
        [Piece(color=BLACK, row=0, column=0, type=ROOK)],
        [Piece(color=BLACK, row=1, column=0, type=PAWN)],
    ]

    
    ```
    The board is literaly the board, a 2D array for each column on the board;
    with the top-left being the black rook and so forth.

    Here, we'll need to track two more things:
    a. white's move: to know which player should play next
    b. moves history: To log the game's moves. This will permit operations like undo,
        and creating leaderboards.
    """

    def __init__(self):
        self.board = [
            # Use enums for the rows and cols names
            [B_ROOK, B_KNIGHT, B_BISHOP, B_QUEEN, B_KING, B_BISHOP, B_KNIGHT, B_ROOK],
            [B_PAWN, B_PAWN, B_PAWN, B_PAWN, B_PAWN, B_PAWN, B_PAWN, B_PAWN],
            [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
            [
                W_PAWN,
                W_PAWN,
                W_PAWN,
                W_PAWN,
                W_PAWN,
                W_PAWN,
                W_PAWN,
                W_PAWN,
            ],
            [W_ROOK, W_KNIGHT, W_BISHOP, W_QUEEN, W_KING, W_BISHOP, W_KNIGHT, W_ROOK],
        ]

        self.white_to_move = True
        self.moves_history = []
        self.captured_pieces = []

        print(f"{'White plays' if self.white_to_move == True else 'Black Plays'}")

    def __str__(self):
        return self.board

    # Move a piece
    def make_move(self, move):

        if self.board[move.start_row][move.start_col] == EMPTY:
            return ILLEGAL_MOVE

        else:
           

            if move in self.get_legal_moves():
                self.board[move.start_row][move.start_col] = EMPTY
                self.board[move.end_row][move.end_col] = move.moved_piece

                # Capture a piece
                if self.board[move.end_row][move.end_col] != EMPTY:
                    self.captured_pieces.append(self.board[move.end_row][move.end_col])
                    # self.board[move.end_row][move.end_col] = move.moved_piece

                # Save move to the moves_history and swap players
                self.moves_history.append(move)
                self.white_to_move = not self.white_to_move
                return move.get_notation()
            else:
                return ILLEGAL_MOVE + "Cannot move pawn like that!"

    # Undo a move
    def undo_move(self):
        # Only undo a move if moves previous moves exist
        if len(self.moves_history) != 0:
            # make move to be the previous move
            move = self.moves_history.pop()
            print(move)
            self.board[move.start_row][move.start_col] = move.moved_piece
            self.board[move.end_row][move.end_col] = move.captured_piece

    def get_legal_moves(self):
        self.legal_moves = []

        for row in range(len(self.board)):
            for column in range(
                len(self.board[row])
            ):  # Loop through each column within a row
                turn = self.board[row][column][0]  # returns an value like 'wR'

                # Check who's turn it is to play
                if (turn == "w" and self.white_to_move) or (
                    turn == "b" and not self.white_to_move
                ):
                    piece = self.board[row][column][
                        1
                    ]  # Get the piece type eg 'R' for ROOK

                    # Create legal moves for all pieces
                    if piece == PAWN:
                        print("Pawn")
                        self.get_pawn_moves(row, column, self.legal_moves)

                    if piece == ROOK:
                        self.get_rook_moves(row, column, self.legal_moves)

                    if piece == KNIGHT:
                        self.get_knight_moves(row, column, self.legal_moves)

                    if piece == BISHOP:
                        self.get_bishop_moves(row, column, self.legal_moves)

                    if (
                        piece == QUEEN
                    ):  # Easiest to implement, just combine bishop and rook moves
                        self.get_queen_moves(row, column, self.legal_moves)

                    if piece == KING:
                        self.get_king_moves(row, column, self.legal_moves)

        return self.legal_moves

    # Legal moves by the pieces
    def get_pawn_moves(self, row, column, legal_moves):
        # If it's white's turn
        if self.white_to_move:  # white pawns start at 2nd row [n][1]
            if self.board[row + 1][column] == EMPTY:
                self.move = Move(start_position=(row, column),end_position=(row + 1, column),board=self.board,)
                legal_moves.append(self.move)
                if row == 1 and (self.board[row + 2][column] == EMPTY):  # First pawn move (Optional 2 step jump)
                    move = Move(start_position=(row, column),end_position=(row + 2, column),board=self.board,)
                    legal_moves.append(move)
                

        return legal_moves
    

    def get_rook_moves(self, row, column, legal_moves):
        pass

    def get_knight_moves(self, row, column, legal_moves):
        pass

    def get_bishop_moves(self, row, column, legal_moves):
        pass

    def get_queen_moves(self, row, column, legal_moves):
        pass

    def get_king_moves(self, row, column, legal_moves):
        pass


class Move:
    """
    A move made by each of the chess pieces on the board
    """

    def __init__(self, start_position, end_position, board):
        # Starting position on the board
        self.start_row = start_position[1]
        self.start_col = start_position[0]

        # Destination on the board
        self.end_row = end_position[1]
        self.end_col = end_position[0]

        # Keep track of the original position of the moved piece
        self.moved_piece = board[self.start_row][self.start_col]

        # Keep track of the destination of the piece
        self.captured_piece = board[self.end_row][self.end_col]

        # Track every move
        self.move_index = str(uuid.uuid4())

        print(self.move_index)

    # def __str__(self) -> str:
    #     return f"{self.captured_piece} {self.moved_piece}"

    # Prevent same row/column combination
    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Move):
            return self.move_index == __o.move_index
        return False

    def get_notation(self):
        """
        Will return a formatted position of the piece on the board
        Eg: Move from e1 >> d4 will return e1d4
        """

        return self.get_chess_rank_file_notation(
            row=self.start_row, column=self.start_col
        ) + self.get_chess_rank_file_notation(row=self.end_row, column=self.end_col)

    def get_chess_rank_file_notation(self, row, column):
        """
        Returns a nicely formatted string of the position on the board
        eg: e3
        """
        return COLUMNS_TO_FILES[column] + ROWS_TO_RANKS[row]

