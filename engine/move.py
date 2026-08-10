import operator

from engine.board import Board, Piece, PieceType, Color
from config import BOARD_SIZE

def move_to(board: Board, selected_square: tuple[int, int], dest_square: tuple[int, int]):
    print(f"Trying to move {selected_square} to {dest_square}")
    if board[dest_square[0]][dest_square[1]] is not None:
        print("Invalid destination")
        return

    if selected_square == (-1, -1):
        print("Invalid selectection")

    board[dest_square[0]][dest_square[1]] = board[selected_square[0]][selected_square[1]]
    board[selected_square[0]][selected_square[1]] = None

    return

def get_legal_moves(board: Board, selected_square: tuple[int, int]) -> list[tuple[int, int]]:
    piece = board.get_square(selected_square)
    legal_moves: list[tuple[int, int]] = []

    if piece is None:
        return None

    print(f"Currenty selected piece {piece.color.value} {piece.kind.value}")
    match piece.kind:
        case PieceType.PAWN:
            direction = 1 if piece.color == Color.BLACK else -1
            starting_rank = 1 if piece.color == Color.BLACK else 6
            current_rank = selected_square[0]
            col = selected_square[1]

            pawn_range = 2 if current_rank == starting_rank else 1

            for _ in range(pawn_range):
                current_rank += direction
                if board[current_rank][col] is not None:
                    break
                legal_moves.append((current_rank, col))

            return legal_moves

        case PieceType.ROOK:
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            legal_moves.extend(get_directional_legal_moves(board, directions, selected_square))

            return legal_moves

        case PieceType.BISHOP:
            directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
            legal_moves.extend(get_directional_legal_moves(board, directions, selected_square))

            return legal_moves

        case PieceType.QUEEN:
            directions = [(1, 1), (1, -1), (-1, 1), (-1, -1), (1, 0), (-1, 0), (0, 1), (0, -1)]
            legal_moves.extend(get_directional_legal_moves(board, directions, selected_square))

            return legal_moves

        case PieceType.KING:
            directions = [(1, 1), (1, -1), (-1, 1), (-1, -1), (1, 0), (-1, 0), (0, 1), (0, -1)]
            for direction in directions:
                current_square: tuple[int, int] = tuple(map(operator.add, selected_square, direction))
                if ((0 <= current_square[0] < BOARD_SIZE) and 
                    (0 <= current_square[1] < BOARD_SIZE) and
                    (board.get_square(current_square) is None)):
                    legal_moves.append(current_square)

            return legal_moves

        case PieceType.KNIGHT:
            directions = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
            for direction in directions:
                current_square: tuple[int, int] = tuple(map(operator.add, selected_square, direction))
                if ((0 <= current_square[0] < BOARD_SIZE) and 
                    (0 <= current_square[1] < BOARD_SIZE) and
                    (board.get_square(current_square) is None)):
                    legal_moves.append(current_square)

            return legal_moves

        case _:
            return legal_moves

def get_directional_legal_moves(board, directions, selected_square):
    legal_moves: list[tuple[int, int]] = []
    for direction in directions:
        current_square: tuple[int, int] = tuple(map(operator.add, selected_square, direction))

        while (0 <= current_square[0] < BOARD_SIZE) and (0 <= current_square[1] < BOARD_SIZE):
            if board.get_square(current_square) is not None:
                break
            legal_moves.append(current_square)
            current_square = tuple(map(operator.add, current_square, direction))

    return legal_moves

