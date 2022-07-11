import json
from channels.generic.websocket import WebsocketConsumer
from chess.constants import FILES_TO_COLUMNS, ROW_NAMES
from chess.engine import ChessEngine
from apps.game.models import Capture, Game, Move
from asgiref.sync import async_to_sync

from django.shortcuts import get_object_or_404

from chess.pieces import ChessPiece

class MovesConsumer(WebsocketConsumer):
    """
    Initializes a websocket connection to play the game

    Constructor
    ---
    Takes a `game: ChessBoard`

    Methods
    ---
    `receive()`: Takes a json input in the form of

    ```json
        {
            "message": {
                "start": [0, 2],
                "end": [0, 4]
            }
        }
    ```
    and shows a flow of the messages from the game engine
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.board = ChessEngine()
        self.game = Game()



    def connect(self):
        self.accept()        
        self.group_name = "chess"
        async_to_sync(self.channel_layer.group_add)(
                            self.group_name, 
                            self.channel_name
                        )
        
        # Load Game messages
        if len(self.board.messages) > 1:
            for message in self.board.messages:
                self.channel_layer.group_send(self.group_name, {
                    "type": "game_message",
                    "message": message
                })
                self.send(json.dumps({
                    "type": "game_message",
                    "message": message
                }))
        else:
            self.send(json.dumps({"type": "initial_messages", "message": self.board.messages}))
        self.channel_layer.group_send(self.group_name,  {"type": "connection_success", "message": "Connection Establiched!"})
        self.send(json.dumps({"type": "game_id", "message": f"{self.group_name}"}))
        

    
    def receive(self, text_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        # Get move coordinates
        from_pos = message["from"]
        to_pos = message["to"]

        start = [FILES_TO_COLUMNS[from_pos[0]], ROW_NAMES[from_pos[1]]]
        end = [FILES_TO_COLUMNS[to_pos[0]], ROW_NAMES[to_pos[1]]]

        # initialize board
        board = self.board
        player = self.board.white_to_play


        # Move the piece
        board.make_move(initial_pos=start, destination=end)

        # Log for debugging
        print(f"{from_pos} {to_pos} by {'White' if player else 'Black'}")

        async_to_sync(self.channel_layer.group_send)(
            self.group_name,
            {
                "type": "create_move",
                "message": f"{from_pos} {to_pos} by {'White' if player else 'Black'}",
                "game_id": str(self.game.game_id),
                "game_messages": [m for m in self.board.messages],
                "board": self.board.board,
            }
        )

    
    def create_move(self, event):
        move = event["message"]
        game_id = event["game_id"]
        messages = event["game_messages"]

        self.send(text_data=json.dumps({
            "type": "game",
            "message": move,
            "game_id": game_id,
            "messages": messages
        }))



    def disconnect(self, code):
        game_id = self.game.game_id
        _game = Game.objects.create(game_id=game_id)
        _game.save()
        

        game_moves = []
        game_captures = []
        
        # Take the game moves
        for move in self.board.moves_history:
            board = self.board.board
            color = ""
            
            # Add piece to moves
            piece = board.board[move[0][0]][move[0][1]]
            if self.get_isinstance_piece(piece):
                color = "White" if piece.color else "Black"
            color = ""
            game_moves.append(
                        Move(
                            from_pos=f"{[move[0][0], move[0][1]]}", 
                            to_pos=f"{[move[1][0], move[1][1]]}", 
                            color=color
                        )
                    )

        # Take the game captures
        for capture in self.board.captures:
            piece = board.board[capture[0][0]][capture[0][1]]
            if self.get_isinstance_piece(piece):
                color = "White" if piece.color else "Black"
            color = ""
            game_captures.append(
                Capture(
                    color = color
                )
            )



        # Bulk create moves and captures
        this_game = get_object_or_404(Game, game_id=game_id)
        this_game.moves.bulk_create(game_moves)
        this_game.captures.bulk_create(game_captures)
        this_game.save()
        
        

    def get_isinstance_piece(self, piece):
        if isinstance(piece, ChessPiece):
           return True
        return False