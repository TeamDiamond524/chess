from enum import Enum

class Turn(Enum):
    WHITE = "w"
    BLACK = "b"

TURN_COUNTER: "Turn" = Turn.WHITE

def change_turn():
    global TURN_COUNTER
    if TURN_COUNTER == Turn.WHITE:
        TURN_COUNTER = Turn.BLACK
    else: TURN_COUNTER = Turn.WHITE
    return

def get_whose_turn():
    return TURN_COUNTER
