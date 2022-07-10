from django.db import models
import uuid


class BaseGameModel(models.Model):
    """
    Model definition for BaseGameModel
    ---

    Contains an `id: uuid`
    ---


    This is just in case more fields will be required later for all our game models

    """

    id = models.CharField(
        primary_key=True, default=uuid.uuid4, editable=False, max_length=300
    )

    class Meta:
        abstract = True


class Move(BaseGameModel):
    """
    Will record a move's initial and final location.
    ---

    `color: str`: The color of the moved piece

    `from_pos: str`: Initial position eg. "[4, 3]"
    
    `to_pos: str`: Destination position eg. "[3, 3]"
    """

    from_pos = models.CharField(max_length=10)
    to_pos = models.CharField(max_length=10)
    color = models.CharField(max_length=10)


class Capture(BaseGameModel):
    """
    Will keep track of captured pieces of any game.
    ---

    `color: str`: The color of the captured piece
    """

    captured_piece = models.CharField(max_length=10)
    color = models.CharField(max_length=10)


class Game(models.Model):
    """
    Model definition for Game.
    ---

    Fields:
    ---
    A game has two players, moves and captures

    `moves: [Move]`: A list containing all the moves
    
    `captures: [Capture]`: A list of all captures within the board
    
    `game_id: uuid`: A unique UUID Field for each game

    `winner: str`: The color of the winner (White/Black)

    Properties
    ---
    `@moves_count: int`: Get total moves within the game
    
    `@captures_count: int`: Get total captures within the game



    ---

    `players`: These are already handled within the `chess.engine`


    """

    game_id = models.CharField(
        primary_key=True, default=uuid.uuid4, editable=True, max_length=200
    )
    moves = models.ManyToManyField(Move)
    captures = models.ManyToManyField(Capture)

    winner = models.CharField(blank=True, null=True, max_length=10)

    @property
    def moves_count(self):
        return self.moves.all.count()

    @property
    def captures_count(self):
        return self.captures.all.count()
