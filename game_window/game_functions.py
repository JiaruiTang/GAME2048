import random

def initialize_board():
    """Initializes an empty 4x4 board."""
    return [[0 for _ in range(4)] for _ in range(4)]

def add_new_tile(board):
    """Adds a new '2' tile at a random empty position on the board."""
    empty_cells = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        board[i][j] = 2

def make_move(board, direction):
    """Performs the move in the specified direction and merges tiles."""
    if direction == 'w':
        return move_up(board)
    elif direction == 's':
        return move_down(board)
    elif direction == 'a':
        return move_left(board)
    elif direction == 'd':
        return move_right(board)

def move_up(board):
    """Moves tiles up and merges them if needed."""
    changed = False
    for col in range(4):
        tiles = [board[row][col] for row in range(4) if board[row][col] != 0]
        merged_tiles = merge_tiles(tiles)
        for row in range(4):
            new_value = merged_tiles[row] if row < len(merged_tiles) else 0
            if board[row][col] != new_value:
                board[row][col] = new_value
                changed = True
    return changed

def move_down(board):
    """Moves tiles down and merges them if needed."""
    changed = False
    for col in range(4):
        tiles = [board[row][col] for row in range(4) if board[row][col] != 0]
        merged_tiles = merge_tiles(tiles)
        merged_tiles = [0] * (4 - len(merged_tiles)) + merged_tiles
        for row in range(4):
            if board[row][col] != merged_tiles[row]:
                board[row][col] = merged_tiles[row]
                changed = True
    return changed

def move_left(board):
    """Moves tiles left and merges them if needed."""
    changed = False
    for row in range(4):
        tiles = [board[row][col] for col in range(4) if board[row][col] != 0]
        merged_tiles = merge_tiles(tiles)
        for col in range(4):
            new_value = merged_tiles[col] if col < len(merged_tiles) else 0
            if board[row][col] != new_value:
                board[row][col] = new_value
                changed = True
    return changed

def move_right(board):
    """Moves tiles right and merges them if needed."""
    changed = False
    for row in range(4):
        tiles = [board[row][col] for col in range(4) if board[row][col] != 0]
        merged_tiles = merge_tiles(tiles)
        merged_tiles = [0] * (4 - len(merged_tiles)) + merged_tiles
        for col in range(4):
            if board[row][col] != merged_tiles[col]:
                board[row][col] = merged_tiles[col]
                changed = True
    return changed

def merge_tiles(tiles):
    """Merges tiles in a row or column."""
    merged = []
    skip = False
    for i in range(len(tiles)):
        if skip:
            skip = False
            continue
        if i + 1 < len(tiles) and tiles[i] == tiles[i + 1]:
            merged.append(tiles[i] * 2)
            skip = True
        else:
            merged.append(tiles[i])
    return merged

def check_win(board):
    """Checks if the player has won by reaching 2048."""
    return any(2048 in row for row in board)

def check_game_over(board):
    """Checks if there are no possible moves left (game over)."""
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                return False
            if i < 3 and board[i][j] == board[i + 1][j]:
                return False
            if j < 3 and board[i][j] == board[i][j + 1]:
                return False
    return True


