def minesweeper_first_move(board, x, y):
    """board: 8x8 array: board[x][y] is 'B' if a bomb, or None else.    (x,y) is where the user clicked.
    Returns: modify board[x][y] to 'B': bomb, #: if it's adjacent to that many bombs, ' ': not adjacent to any bombs, or '?' if unknown: 

    >>> board = [['B', None, 'B'], [None, None, None], [None, 'B', None]]
    >>> minesweeper_first_move(board, 1, 1)
    >>>
    >>> board
    >>> [['?', '?', '?'], ['?', 3, '?'], ['?', '?', '?']]
    """
    bomb_counter = 0
    x_length = len(board)
    y_length = len(board[0])

    for i in xrange(x-1, x+2):
        for j in xrange(y-1, y+2):
            if i >= 0 and i < x_length and j >= 0 and j < y_length:
                if board[i][j] == 'B':
                    bomb_counter += 1

    if board[x][y] == 'B':
        for i in xrange(x_length):
            for j in xrange(y_length):
                if not (i == x and j == y):
                    board[i][j] = '?'
    else:
        for i in xrange(x_length):
            for j in xrange(y_length):
                if not (i == x and j == y):
                    board[i][j] = '?'
                elif bomb_counter != 0:
                    board[i][j] = bomb_counter
                else:
                    board[i][j] = " "

if __name__ == "__main__":
    # import doctest
    # doctest.testmod()
    board = [['B', None, 'B'], [None, None, None], [None, 'B', None]]
    minesweeper_first_move(board, 1, 1)
    print board
