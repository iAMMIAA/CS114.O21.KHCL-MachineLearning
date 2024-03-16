def check_winner(board)
    for row in board
        if len(set(row)) == 1
            return True

    for col in zip(board)
        if len(set(col)) == 1
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]
        return True

    return False

def main()
    board = [list(map(int, input().split())) for _ in range(3)]
    n = int(input())
    numbers = [int(input()) for _ in range(n)]

    for i in range(3)
        for j in range(3)
            if board[i][j] in numbers
                board[i][j] = 0

    if check_winner(board)
        print('Yes')
    else
        print('No')

if __name__ == __main__
    main()