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