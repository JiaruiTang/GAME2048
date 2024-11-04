import random

class Game2048:
    def __init__(self):
        """Initialize the game board and start with two tiles."""
        self.size = 4  # Board size is 4x4
        self.board = [[0] * self.size for i in range(self.size)]
        self.new_tile()
        self.new_tile()

    def new_tile(self):
        """Add a new '2' tile at a random empty position on the board."""
        empty_cells = [(i, j) for i in range(self.size) for j in range(self.size) if self.board[i][j] == 0]
        if empty_cells:
            i, j = random.choice(empty_cells)
            self.board[i][j] = 2

    def print_board(self):
        """Print the current state of the board."""
        for row in self.board:
            print("\t".join(str(val) if val != 0 else "." for val in row))
        print()

    def make_move(self, direction):
        """Process a move in the specified direction."""
        if direction == 'w':
            return self.move_up()
        elif direction == 's':
            return self.move_down()
        elif direction == 'a':
            return self.move_left()
        elif direction == 'd':
            return self.move_right()

    def move_up(self):
        """Move all tiles up and merge as needed."""
        changed = False
        for col in range(self.size):
            # Move values up vertically
            tiles = [self.board[row][col] for row in range(self.size) if self.board[row][col] != 0]
            # Merge necessary values
            merged_tiles = self.merge_tiles(tiles)
            for row in range(self.size):
                new_value = merged_tiles[row] if row < len(merged_tiles) else 0
                if self.board[row][col] != new_value:
                    self.board[row][col] = new_value
                    changed = True
        return changed

    def move_down(self):
        """Move all tiles down and merge as needed."""
        changed = False
        for col in range(self.size):
            tiles = [self.board[row][col] for row in range(self.size) if self.board[row][col] != 0]
            merged_tiles = self.merge_tiles(tiles)
            merged_tiles = [0] * (self.size - len(merged_tiles)) + merged_tiles
            for row in range(self.size):
                if self.board[row][col] != merged_tiles[row]:
                    self.board[row][col] = merged_tiles[row]
                    changed = True
        return changed

    def move_left(self):
        """Move all tiles to the left and merge as needed."""
        changed = False
        for row in range(self.size):
            tiles = [self.board[row][col] for col in range(self.size) if self.board[row][col] != 0]
            merged_tiles = self.merge_tiles(tiles)
            for col in range(self.size):
                new_value = merged_tiles[col] if col < len(merged_tiles) else 0
                if self.board[row][col] != new_value:
                    self.board[row][col] = new_value
                    changed = True
        return changed

    def move_right(self):
        """Move all tiles to the right and merge as needed."""
        changed = False
        for row in range(self.size):
            tiles = [self.board[row][col] for col in range(self.size) if self.board[row][col] != 0]
            merged_tiles = self.merge_tiles(tiles)
            merged_tiles = [0] * (self.size - len(merged_tiles)) + merged_tiles
            for col in range(self.size):
                if self.board[row][col] != merged_tiles[col]:
                    self.board[row][col] = merged_tiles[col]
                    changed = True
        return changed

    def merge_tiles(self, tiles):
        """Merge a list of tiles in one row or column."""
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

    def check_win(self):
        """Check if the player has won by reaching 2048."""
        return any(2048 in row for row in self.board)

    def check_game_over(self):
        """Check if there are no possible moves left (game over)."""
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 0:
                    return False
                if i < self.size - 1 and self.board[i][j] == self.board[i + 1][j]:
                    return False
                if j < self.size - 1 and self.board[i][j] == self.board[i][j + 1]:
                    return False
        return True

