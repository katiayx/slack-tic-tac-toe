# Display ttt board

def display_ttt_board(board):
    """create empty ttt board"""

    for i in range(3):
        for j in range(3):
            if j != 2:
                print "  |",
        print
        if i != 2:
            print "----------"
        else:
            print


board = []
for i in range(9):
    board.append(i + 1)


def get_user_move():
    """ask for a move by user, 
    check whether move is valid"""


