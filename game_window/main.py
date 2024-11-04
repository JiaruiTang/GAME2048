# !pip install pygame
import pygame
import game_functions as gf

# Constants for the game display
WINDOW_SIZE = 600
GRID_SIZE = 4
TILE_SIZE = WINDOW_SIZE // GRID_SIZE
BACKGROUND_COLOR = (187, 173, 160)
TILE_COLORS = {
    0: (205, 193, 180),
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46),
}
# TILE_COLORS = {
#     0: (220, 220, 220),
#     2: (255, 182, 193),
#     4: (255, 160, 122),
#     8: (255, 105, 180),
#     16: (255, 99, 71),
#     32: (255, 69, 0),
#     64: (255, 20, 147),
#     128: (219, 112, 147),
#     256: (199, 21, 133),
#     512: (138, 43, 226),
#     1024: (148, 0, 211),
#     2048: (75, 0, 130),
# }
# TILE_COLORS = {
#     0: (230, 230, 230),
#     2: (204, 255, 204),
#     4: (153, 255, 153),
#     8: (102, 255, 178),
#     16: (51, 255, 204),
#     32: (0, 204, 204),
#     64: (0, 153, 153),
#     128: (0, 102, 204),
#     256: (0, 51, 204),
#     512: (51, 51, 204),
#     1024: (51, 0, 153),
#     2048: (0, 51, 102),
# }

# Initialize pygame
pygame.init()
gameWindow = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))  # Square window
pygame.display.set_caption("2048 Game")
font = pygame.font.Font(None, 40)

def draw_board(board):
    """Draw the game board with tiles and colors based on the values."""
    gameWindow.fill(BACKGROUND_COLOR)
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            value = board[i][j]
            color = TILE_COLORS.get(value, TILE_COLORS[2048])
            pygame.draw.rect(gameWindow, color, (j * TILE_SIZE, i * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            if value != 0:
                text_surface = font.render(str(value), True, (119, 110, 101))
                text_rect = text_surface.get_rect(center=(j * TILE_SIZE + TILE_SIZE // 2, i * TILE_SIZE + TILE_SIZE // 2))
                gameWindow.blit(text_surface, text_rect)
    pygame.display.flip()

def main():
    board = gf.initialize_board()
    gf.add_new_tile(board)
    gf.add_new_tile(board)

    draw_board(board)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d]:
                    # Map the keys w, s, a, d to corresponding moves
                    move = {
                        pygame.K_w: 'w',  # Up
                        pygame.K_s: 's',  # Down
                        pygame.K_a: 'a',  # Left
                        pygame.K_d: 'd'   # Right
                    }[event.key]
                    changed = gf.make_move(board, move)
                    if changed:
                        gf.add_new_tile(board)
                    draw_board(board)
                    if gf.check_win(board):
                        print("Congratulations! You've reached 2048!")
                        running = False
                    if gf.check_game_over(board):
                        print("Game Over! No more moves possible.")
                        running = False

    pygame.quit()

if __name__ == "__main__":
    main()
