import operator

from engine.board import Board, Piece, PieceType, Color
from config import BOARD_SIZE

def move_to(board: Board, selected_square: tuple[int, int], dest_square: tuple[int, int]) -> bool:
    print(f"Trying to move {selected_square} to {dest_square}")

    if selected_square == (-1, -1):
        print("Invalid selectection")
        return False

    legal_moves = get_legal_moves(board, selected_square)
    if dest_square not in legal_moves:
        print("illigal move")
        return False

    board[dest_square[0]][dest_square[1]] = board[selected_square[0]][selected_square[1]]
    board[selected_square[0]][selected_square[1]] = None

    return True

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

            #Pawn capture logic
            diagonals: list[tuple[int, int]] = [(direction, direction), (direction, -direction)]
            for diagonal in diagonals:
                capture_square: tuple[int, int] = tuple(map(operator.add, selected_square, diagonal))
                print(f"Capture_square: {capture_square}; Checking diagonal {diagonal}")
                if board.get_square(diagonal) is not None:
                    if is_legal_capture(board, selected_square, capture_square):
                        legal_moves.append(capture_square)

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
            legal_moves.extend(get_legal_moves_for_squares(board, directions, selected_square))

            return legal_moves

        case PieceType.KNIGHT:
            directions = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
            legal_moves.extend(get_legal_moves_for_squares(board, directions, selected_square))

            return legal_moves

        case _:
            return legal_moves

def get_directional_legal_moves(board, directions, selected_square):
    legal_moves: list[tuple[int, int]] = []
    for direction in directions:
        current_square: tuple[int, int] = tuple(map(operator.add, selected_square, direction))

        while (0 <= current_square[0] < BOARD_SIZE) and (0 <= current_square[1] < BOARD_SIZE):
            if board.get_square(current_square) is not None:
                if is_legal_capture(board, selected_square, current_square):
                    legal_moves.append(current_square)
                break
            legal_moves.append(current_square)
            current_square = tuple(map(operator.add, current_square, direction))

    return legal_moves

def get_legal_moves_for_squares(board, squares, selected_square):
    legal_moves: list[tuple[int, int]] = []
    for square_direction in squares:
        current_square: tuple[int, int] = tuple(map(operator.add, selected_square, square_direction))
        if (0 <= current_square[0] < BOARD_SIZE) and (0 <= current_square[1] < BOARD_SIZE):
            if board.get_square(current_square) is not None: 
                if is_legal_capture(board, selected_square, current_square):
                    legal_moves.append(current_square)
            else:
                legal_moves.append(current_square)

    return legal_moves


def is_legal_capture(board, selected_square, capture_square) -> bool:
    selected_color = board.get_square(selected_square).color
    opponent_piece = board.get_square(capture_square)

    if opponent_piece is None:
        return False

    if opponent_piece.kind == PieceType.KING:
        return False

    return selected_color != opponent_piece.color

