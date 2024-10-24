class ChessGame:\
    def __init__(self):\
        self.reset()\
\
    def reset(self):\
        self.board = [\
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],\
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],\
            ['.', '.', '.', '.', '.', '.', '.', '.'],\
            ['.', '.', '.', '.', '.', '.', '.', '.'],\
            ['.', '.', '.', '.', '.', '.', '.', '.'],\
            ['.', '.', '.', '.', '.', '.', '.', '.'],\
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],\
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']\
        ]\
        self.turn = 'white'\
\
    def print_board(self):\
        for row in self.board:\
            print(' '.join(row))\
        print()\
\
    def move(self, start, end):\
        start_row, start_col = 8 - int(start[1]), ord(start[0]) - ord('a')\
        end_row, end_col = 8 - int(end[1]), ord(end[0]) - ord('a')\
        piece = self.board[start_row][start_col]\
\
        if self.turn == 'white' and piece.islower() or self.turn == 'black' and piece.isupper():\
            print("It's not your turn!")\
            return False\
\
        self.board[end_row][end_col] = self.board[start_row][start_col]\
        self.board[start_row][start_col] = '.'\
        self.turn = 'black' if self.turn == 'white' else 'white'\
        return True\
\
    def is_valid_move(self, start, end):\
        return True\
\
def play_game():\
    game = ChessGame()\
    game.print_board()\
\
    while True:\
        print(f"\{game.turn.capitalize()\}'s move")\
        start = input("Enter the start position (e.g., e2): ")\
        end = input("Enter the end position (e.g., e4): ")\
\
        if start.lower() == 'reset':\
            game.reset()\
            print("Game reset!")\
            game.print_board()\
            continue\
\
        if game.is_valid_move(start, end):\
            game.move(start, end)\
        else:\
            print("Invalid move, try again.")\
        \
        game.print_board()\
\
if __name__ == "__main__":\
    play_game()}
