"""Display the 3x3 board."""
def print_board(board):
    print()
    print("   0   1   2")
    for i in range(3):
        print(i, " " + " | ".join(board[i]))
        if i < 2:
            print("  ---+---+---")
    print()
