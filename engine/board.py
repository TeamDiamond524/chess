from enum import Enum
from dataclasses import dataclass
from config import BOARD_SIZE

class Color(Enum):
    WHITE = "w"
    BLACK = "b"

class PieceType(Enum):
    KING = "king"
    QUEEN = "queen"
    ROOK = "rook"
    BISHOP = "bishop"
    KNIGHT = "knight"
    PAWN = "pawn"

class Board:
    def __init__(self):
        self.squares = [[None for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

    def set_up(self):
        self.squares = [
            [ Piece(Color.BLACK, PieceType.ROOK), Piece(Color.BLACK, PieceType.KNIGHT), Piece(Color.BLACK, PieceType.BISHOP), Piece(Color.BLACK, PieceType.QUEEN), Piece(Color.BLACK, PieceType.KING), Piece(Color.BLACK, PieceType.BISHOP),  Piece(Color.BLACK, PieceType.KNIGHT), Piece(Color.BLACK, PieceType.ROOK) ],
            [ Piece(Color.BLACK, PieceType.PAWN) ] * 8,
            [ None ] * 8,
            [ None ] * 8,
            [ None ] * 8,
            [ None ] * 8,
            [ Piece(Color.WHITE, PieceType.PAWN) ] * 8,
            [ Piece(Color.WHITE, PieceType.ROOK), Piece(Color.WHITE, PieceType.KNIGHT), Piece(Color.WHITE, PieceType.BISHOP), Piece(Color.WHITE, PieceType.QUEEN), Piece(Color.WHITE, PieceType.KING), Piece(Color.WHITE, PieceType.BISHOP),  Piece(Color.WHITE, PieceType.KNIGHT), Piece(Color.WHITE, PieceType.ROOK) ],
        ]

    def __getitem__(self, index: int):
        return self.squares[index]

@dataclass
class Piece:
    color: "Color"
    kind: "PieceType"
