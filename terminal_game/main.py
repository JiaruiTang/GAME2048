from game_functions import Game2048

def main():
    # Initialize the 2048 game
    game = Game2048()
    game.print_board() 

    while True:
        try:
            # Prompt user for input
            move = input("Enter move (w/a/s/d): ").lower()

            # Allow quit
            if move == 'q':
                print('Quit the game.')
                break

            # Raise exception for invalid input
            if move not in ['w', 'a', 's', 'd']:
                raise ValueError("Invalid move. Please enter w, a, s, or d.")

            # Make the move and check if any tile was moved/merged
            changed = game.make_move(move)
            if changed:
                game.new_tile()  # Add a new tile if the board changed
                game.print_board()  # Print updated board

                # Check for win condition
                if game.check_win():
                    print("Win!")
                    break

                # Check for game over condition
                if game.check_game_over():
                    print("Game Over!")
                    break
            else:
                print("Move not possible in that direction.")

        except ValueError as e:
            # Handle invalid input by printing the error message
            print(e)

if __name__ == "__main__":
    main()


