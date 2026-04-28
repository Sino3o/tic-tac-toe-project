"""Display the 3x3 board."""
def print_board(board):
    print()
    print("   0   1   2")
    for i in range(3):
        print(i, " " + " | ".join(board[i]))
        if i < 2:
            print("  ---+---+---")
    print()


"""Check if the current player has won already"""
def check_winner(board, player):
    for row in board: 
        if row[0] == player and row[1] == player and row[2] == player:
            return True
        
    for col in range(3):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
    
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    
    return False

"""Check if the game is a draw"""
def is_draw(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True

"""check if the move is valid"""
def get_move(board, player):
    while True:
        try:
            row  = int(input(f"Player{player}, enter row(0-2): "))
            col  = int(input(f"Player{player}, enter column(0-2): "))

            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Invalid move. Row and column must be between 0 and 2.")
            elif board[row][col] != " ":
                print("That spot is already taken. Please choose another spot.")
            else:
                return row, col
        except ValueError:
            print("Invalid input. Please enter numbers only.")

"""switch player"""
def switch_player(player):
    return "O" if player =="X" else "X"
    
"the main game"
def play_game():
    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]

    current_player = "X"
    game_over = False
    print("welcome to Tic Tac Toe!")
    print("Players take turns entering row and column numbers from 0 to 2.")

    while not game_over:
        print_board(board)
        row, col = get_move(board, current_player)
        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            game_over = True
        elif is_draw(board):
            print_board(board)
            print("This game is a draw!")
            game_over = True
        else:
            current_player = switch_player(current_player)

if __name__ == "__main__":
    play_game()