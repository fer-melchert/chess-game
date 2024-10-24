class ChessGame:
    def __init__(self):
        # Initialize the game and set up the board
        self.reset()

    def reset(self):
        # Set up the initial board configuration
        self.board = [
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        ]
        self.turn = 'white'  # White starts the game

    def print_board(self):
        # Print the current state of the board
        for row in self.board:
            print(' '.join(row))
        print()

    def move(self, start, end):
        # Convert chess notation to board indices
        start_row, start_col = 8 - int(start[1]), ord(start[0]) - ord('a')
        end_row, end_col = 8 - int(end[1]), ord(end[0]) - ord('a')
        piece = self.board[start_row][start_col]  # Get the piece at the start position

        # Check if it's the correct turn
        if self.turn == 'white' and piece.islower() or self.turn == 'black' and piece.isupper():
            print("It's not your turn!")
            return False

        # Move the piece and update the turn
        self.board[end_row][end_col] = self.board[start_row][start_col]
        self.board[start_row][start_col] = '.'
        self.turn = 'black' if self.turn == 'white' else 'white'  # Switch turns
        return True

    def is_valid_move(self, start, end):
        # Placeholder for move validation logic
        return True

def play_game():
    # Create a new game instance and print the initial board
    game = ChessGame()
    game.print_board()

    while True:
        # Prompt the current player for their move
        print(f"{game.turn.capitalize()}'s move")
        start = input("Enter the start position (e.g., e2): ")
        end = input("Enter the end position (e.g., e4): ")

        if start.lower() == 'reset':
            # Reset the game if the user types 'reset'
            game.reset()
            print("Game reset!")
            game.print_board()
            continue

        if game.is_valid_move(start, end):
            # Move the piece if the move is valid
            game.move(start, end)
        else:
            print("Invalid move, try again.")
        
        # Print the updated board after each move
        game.print_board()

if __name__ == "__main__":
    play_game()  # Start the game
