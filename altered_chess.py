import sys

f = open(sys.argv[1], "r")
commands = [line.split() for line in f.readlines()]
f.close()
num_move, let_move, num_index, letter_index = 0, 0, 0, 0
black_pieces = ['R1', 'N1', 'B1', 'QU', 'B2', 'N2', 'R2', 'P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8']
white_pieces = ['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'r1', 'n1', 'b1', 'qu', 'b2', 'n2', 'r2']
show_list = []
board = [[24 * "-"],
         ['R1', 'N1', 'B1', 'QU', 'KI', 'B2', 'N2', 'R2'],
         ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8'],
         ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
         ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
         ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
         ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
         ['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8'],
         ['r1', 'n1', 'b1', 'qu', 'ki', 'b2', 'n2', 'r2'],
         [24 * "-"]]
initial_board = [[24 * "-"],
                 ['R1', 'N1', 'B1', 'QU', 'KI', 'B2', 'N2', 'R2'],
                 ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8'],
                 ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
                 ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
                 ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
                 ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
                 ['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8'],
                 ['r1', 'n1', 'b1', 'qu', 'ki', 'b2', 'n2', 'r2'],
                 [24 * "-"]]
notation = [[24 * "-"],
            ['a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8'],
            ['a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7'],
            ['a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6'],
            ['a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5'],
            ['a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4'],
            ['a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3'],
            ['a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2'],
            ['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1'],
            [24 * "-"]]


def display(x):
    for j in x:
        print(' '.join(j))


def white_pawn(p):
    global num_move, let_move, num_index, letter_index
    index_counter = 0
    for i in board:
        if p in i:
            num_index, letter_index = (index_counter, i.index(p))
        index_counter += 1
    if num_move == (num_index - 1) and let_move == letter_index:
        if board[num_move][let_move] == '  ' or board[num_move][let_move] in black_pieces:
            board[num_move][let_move] = p
            board[num_index][letter_index] = '  '
            print('OK')
    else:
        print('FAILED')


def black_pawn(P):
    global num_move, let_move, num_index, letter_index
    index_counter = 0
    for i in board:
        if P in i:
            num_index, letter_index = (index_counter, i.index(P))
        index_counter += 1
    if num_move == (num_index + 1) and let_move == letter_index:
        if board[num_move][let_move] == '  ' or board[num_move][let_move] in white_pieces:
            board[num_move][let_move] = P
            board[num_index][letter_index] = '  '
            print('OK')
    else:
        print('FAILED')


def white_piece(x):
    global num_move, let_move, num_index, letter_index
    index_counter = 0
    global show_list
    for i in board:
        if x in i:
            num_index, letter_index = (index_counter, i.index(x))
        index_counter += 1
    showmoves(x)
    if notation[num_move][let_move] in show_list:
        if board[num_move][let_move] == '  ' or board[num_move][let_move] in black_pieces:
            board[num_move][let_move] = x
            board[num_index][letter_index] = '  '
            print('OK')
    else:
        print('FAILED')


def black_piece(X):
    global num_move, let_move, num_index, letter_index, show_list
    index_counter = 0
    for i in board:
        if X in i:
            num_index, letter_index = (index_counter, i.index(X))
        index_counter += 1
    showmoves(X)
    if notation[num_move][let_move] in show_list:
        if board[num_move][let_move] == '  ' or board[num_move][let_move] in white_pieces:
            board[num_move][let_move] = X
            board[num_index][letter_index] = '  '
            print('OK')
    else:
        print('FAILED')


def move(a, b):
    #  print(a[0],a[1],b[0], b[1])
    # indexing the position of move
    global num_move, let_move, num_index, letter_index, show_list
    if b[0] == 'a':
        let_move = 0
    elif b[0] == 'b':
        let_move = 1
    elif b[0] == 'c':
        let_move = 2
    elif b[0] == 'd':
        let_move = 3
    elif b[0] == 'e':
        let_move = 4
    elif b[0] == 'f':
        let_move = 5
    elif b[0] == 'g':
        let_move = 6
    elif b[0] == 'h':
        let_move = 7
    if b[1] == '1':
        num_move = 8
    elif b[1] == '2':
        num_move = 7
    elif b[1] == '3':
        num_move = 6
    elif b[1] == '4':
        num_move = 5
    elif b[1] == '5':
        num_move = 4
    elif b[1] == '6':
        num_move = 3
    elif b[1] == '7':
        num_move = 2
    elif b[1] == '8':
        num_move = 1
    if a[0] == 'p':
        white_pawn(a)
    elif a[0] == 'P':
        black_pawn(a)
    elif a in black_pieces or a == 'KI':
        black_piece(a)
    elif a in white_pieces or a == 'ki':
        white_piece(a)


def showmoves(x1):
    global num_move, let_move, num_index, letter_index
    index_counter = 0
    global show_list
    show_list = []
    for i in board:
        if x1 in i:
            num_index, letter_index = (index_counter, i.index(x1))
        index_counter += 1
    if x1[0] == 'p':
        if board[num_index - 1][letter_index] == '  ' or board[num_index - 1][letter_index] in black_pieces:
            show_list.append(notation[num_index - 1][letter_index])

    elif x1[0] == 'P':
        if board[num_index + 1][letter_index] == '  ' or board[num_index + 1][letter_index] in white_pieces:
            show_list.append(notation[num_index + 1][letter_index])

    elif x1[0] == 'r':  # white rook up movement
        tnum_index = num_index
        for j in range(7):
            tnum_index -= 1
            if tnum_index >= 1:
                if board[tnum_index][letter_index] == '  ' or board[tnum_index][letter_index] in black_pieces:
                    show_list.append(notation[tnum_index][letter_index])
                    if board[tnum_index][letter_index] in black_pieces:
                        break
                else:
                    break
        tnum_index = num_index
        for j in range(7):  # white rook down movement
            tnum_index += 1
            if tnum_index <= 8:
                if board[tnum_index][letter_index] == '  ' or board[tnum_index][letter_index] in black_pieces:
                    show_list.append(notation[tnum_index][letter_index])
                    if board[tnum_index][letter_index] in black_pieces:
                        break
                else:
                    break
        tletter_index = letter_index
        for j in range(7):  # white rook right movement
            tletter_index += 1
            if tletter_index <= 7:
                if board[num_index][tletter_index] == '  ' or board[num_index][tletter_index] in black_pieces:
                    show_list.append(notation[num_index][tletter_index])
                    if board[num_index][tletter_index] in black_pieces:
                        break
                else:
                    break
        tletter_index = letter_index
        for j in range(7):  # white rook left movement
            tletter_index -= 1
            if tletter_index >= 0:
                if board[num_index][tletter_index] == '  ' or board[num_index][tletter_index] in black_pieces:
                    show_list.append(notation[num_index][tletter_index])
                    if board[num_index][tletter_index] in black_pieces:
                        break
                else:
                    break

    elif x1[0] == 'R':
        tnum_index = num_index
        for j in range(7):  # black rook up movement
            tnum_index += 1
            if tnum_index <= 8:
                if board[tnum_index][letter_index] == '  ' or board[tnum_index][letter_index] in white_pieces:
                    show_list.append(notation[tnum_index][letter_index])
                    if board[tnum_index][letter_index] in white_pieces:
                        break
                else:
                    break
        tnum_index = num_index
        for j in range(7):  # black rook down movement
            tnum_index -= 1
            if tnum_index >= 1:
                if board[tnum_index][letter_index] == '  ' or board[tnum_index][letter_index] in white_pieces:
                    show_list.append(notation[tnum_index][letter_index])
                    if board[tnum_index][letter_index] in white_pieces:
                        break
                else:
                    break
        tletter_index = letter_index
        for j in range(7):  # black rook right movement
            tletter_index += 1
            if tletter_index <= 7:
                if board[num_index][tletter_index] == '  ' or board[num_index][tletter_index] in white_pieces:
                    show_list.append(notation[num_index][tletter_index])
                    if board[num_index][tletter_index] in white_pieces:
                        break
                else:
                    break
        tletter_index = letter_index
        for j in range(7):  # black rook left movement
            tletter_index -= 1
            if tletter_index >= 0:
                if board[num_index][tletter_index] == '  ' or board[num_index][tletter_index] in white_pieces:
                    show_list.append(notation[num_index][tletter_index])
                    if board[num_index][tletter_index] in white_pieces:
                        break
                else:
                    break

    elif x1[0] == 'n':  # this is for white knight
        if num_index - 2 >= 1 and letter_index + 1 <= 7:
            if board[num_index - 2][letter_index + 1] == '  ' or board[num_index - 2][letter_index + 1] in black_pieces:
                show_list.append(notation[num_index - 2][letter_index + 1])
        if num_index - 2 >= 1 and letter_index - 1 >= 0:
            if board[num_index - 2][letter_index - 1] == '  ' or board[num_index - 2][letter_index - 1] in black_pieces:
                show_list.append(notation[num_index - 2][letter_index - 1])
        if num_index + 2 <= 8 and letter_index + 1 <= 7:
            if board[num_index + 2][letter_index + 1] == '  ' or board[num_index + 2][letter_index + 1] in black_pieces:
                show_list.append(notation[num_index + 2][letter_index + 1])
        if num_index + 2 <= 8 and letter_index - 1 >= 0:
            if board[num_index + 2][letter_index - 1] == '  ' or board[num_index + 2][letter_index - 1] in black_pieces:
                show_list.append(notation[num_index + 2][letter_index - 1])
        if num_index - 1 >= 1 and letter_index + 1 <= 7:  # knight's diagonal movements
            if board[num_index - 1][letter_index + 1] == '  ':
                show_list.append(notation[num_index - 1][letter_index + 1])
        if num_index - 1 >= 1 and letter_index - 1 >= 0:
            if board[num_index - 1][letter_index - 1] == '  ':
                show_list.append(notation[num_index - 1][letter_index - 1])
        if num_index + 1 <= 8 and letter_index + 1 <= 7:
            if board[num_index + 1][letter_index + 1] == '  ':
                show_list.append(notation[num_index + 1][letter_index + 1])
        if num_index + 1 <= 8 and letter_index - 1 >= 0:
            if board[num_index + 1][letter_index - 1] == '  ':
                show_list.append(notation[num_index + 1][letter_index - 1])
        if num_index + 1 <= 8 and letter_index - 2 >= 0:
            if board[num_index + 1][letter_index - 2] == '  ' or board[num_index + 1][letter_index - 2] in black_pieces:
                show_list.append(notation[num_index + 1][letter_index - 2])
        if num_index + 1 <= 8 and letter_index + 2 <= 7:
            if board[num_index + 1][letter_index + 2] == '  ' or board[num_index + 1][letter_index + 2] in black_pieces:
                show_list.append(notation[num_index + 1][letter_index + 2])
        if num_index - 1 >= 1 and letter_index - 2 >= 0:
            if board[num_index - 1][letter_index - 2] == '  ' or board[num_index - 1][letter_index - 2] in black_pieces:
                show_list.append(notation[num_index - 1][letter_index - 2])
        if num_index - 1 >= 1 and letter_index + 2 <= 7:
            if board[num_index - 1][letter_index + 2] == '  ' or board[num_index - 1][letter_index - 2] in black_pieces:
                show_list.append(notation[num_index - 1][letter_index + 2])

    elif x1[0] == 'N':  # this is for black knight
        if num_index - 2 >= 1 and letter_index + 1 <= 7:
            if board[num_index - 2][letter_index + 1] == '  ' or board[num_index - 2][letter_index + 1] in white_pieces:
                show_list.append(notation[num_index - 2][letter_index + 1])
        if num_index - 2 >= 1 and letter_index - 1 >= 0:
            if board[num_index - 2][letter_index - 1] == '  ' or board[num_index - 2][letter_index - 1] in white_pieces:
                show_list.append(notation[num_index - 2][letter_index - 1])
        if num_index + 2 <= 8 and letter_index + 1 <= 7:
            if board[num_index + 2][letter_index + 1] == '  ' or board[num_index + 2][letter_index + 1] in white_pieces:
                show_list.append(notation[num_index + 2][letter_index + 1])
        if num_index + 2 <= 8 and letter_index - 1 >= 0:
            if board[num_index + 2][letter_index - 1] == '  ' or board[num_index + 2][letter_index - 1] in white_pieces:
                show_list.append(notation[num_index + 2][letter_index - 1])
        if num_index - 1 >= 1 and letter_index + 1 <= 7:  # knight's diagonal movements
            if board[num_index - 1][letter_index + 1] == '  ':
                show_list.append(notation[num_index - 1][letter_index + 1])
        if num_index - 1 >= 1 and letter_index - 1 >= 0:
            if board[num_index - 1][letter_index - 1] == '  ':
                show_list.append(notation[num_index - 1][letter_index - 1])
        if num_index + 1 <= 8 and letter_index + 1 <= 7:
            if board[num_index + 1][letter_index + 1] == '  ':
                show_list.append(notation[num_index + 1][letter_index + 1])
        if num_index + 1 <= 8 and letter_index - 1 >= 0:
            if board[num_index + 1][letter_index - 1] == '  ':
                show_list.append(notation[num_index + 1][letter_index - 1])
        if num_index + 1 <= 8 and letter_index - 2 >= 0:
            if board[num_index + 1][letter_index - 2] == '  ' or board[num_index + 1][letter_index - 2] in white_pieces:
                show_list.append(notation[num_index + 1][letter_index - 2])
        if num_index + 1 <= 8 and letter_index + 2 <= 7:
            if board[num_index + 1][letter_index + 2] == '  ' or board[num_index + 1][letter_index + 2] in white_pieces:
                show_list.append(notation[num_index + 1][letter_index + 2])
        if num_index - 1 >= 1 and letter_index - 2 >= 0:
            if board[num_index - 1][letter_index - 2] == '  ' or board[num_index - 1][letter_index - 2] in white_pieces:
                show_list.append(notation[num_index - 1][letter_index - 2])
        if num_index - 1 >= 1 and letter_index + 2 <= 7:
            if board[num_index - 1][letter_index + 2] == '  ' or board[num_index - 1][letter_index - 2] in white_pieces:
                show_list.append(notation[num_index - 1][letter_index + 2])
    elif x1[0] == 'b':
        tletter_index, tnum_index = letter_index, num_index
        for j in range(7):  # white bishop's upper left diagonal movement
            tletter_index -= 1
            tnum_index -= 1
            if tletter_index >= 0 and tnum_index >= 1:
                if board[tnum_index][tletter_index] == '  ' or board[tnum_index][tletter_index] in black_pieces:
                    show_list.append(notation[tnum_index][tletter_index])
                    if board[tnum_index][tletter_index] in black_pieces:
                        break
                else:
                    break
        tletter_index, tnum_index = letter_index, num_index
        for j in range(7):  # white bishop's upper right diagonal movement
            tletter_index += 1
            tnum_index -= 1
            if tletter_index <= 7 and tnum_index >= 1:
                if board[tnum_index][tletter_index] == '  ' or board[tnum_index][tletter_index] in black_pieces:
                    show_list.append(notation[tnum_index][tletter_index])
                    if board[tnum_index][tletter_index] in black_pieces:
                        break
                else:
                    break

    elif x1[0] == 'B':
        tletter_index, tnum_index = letter_index, num_index
        for j in range(7):  # black bishop's down left diagonal movement
            tletter_index -= 1
            tnum_index += 1
            if tletter_index >= 0 and tnum_index <= 8:
                if board[tnum_index][tletter_index] == '  ' or board[tnum_index][tletter_index] in white_pieces:
                    show_list.append(notation[tnum_index][tletter_index])
                    if board[tnum_index][tletter_index] in white_pieces:
                        break
                else:
                    break
        tletter_index, tnum_index = letter_index, num_index
        for j in range(7):  # black bishop's down right diagonal movement
            tletter_index += 1
            tnum_index += 1
            if tletter_index <= 7 and tnum_index <= 8:
                if board[tnum_index][tletter_index] == '  ' or board[tnum_index][tletter_index] in white_pieces:
                    show_list.append(notation[tnum_index][tletter_index])
                    if board[tnum_index][tletter_index] in white_pieces:
                        break
                else:
                    break

    elif x1 == 'QU':
        tletter_index, tnum_index = letter_index, num_index
        for j in range(7):  # bishop's up left diagonal movement pattern taken
            tletter_index -= 1
            tnum_index -= 1
            if tletter_index >= 0 and tnum_index >= 1:
                if board[tnum_index][tletter_index] == '  ' or board[tnum_index][tletter_index] in white_pieces:
                    show_list.append(notation[tnum_index][tletter_index])
                    if board[tnum_index][tletter_index] in white_pieces:
                        break
                else:
                    break
        tletter_index, tnum_index = letter_index, num_index
        for j in range(7):  # bishop's up right diagonal movement pattern taken
            tletter_index += 1
            tnum_index -= 1
            if tletter_index <= 7 and tnum_index >= 1:
                if board[tnum_index][tletter_index] == '  ' or board[tnum_index][tletter_index] in white_pieces:
                    show_list.append(notation[tnum_index][tletter_index])
                    if board[tnum_index][tletter_index] in white_pieces:
                        break
                else:
                    break
        tletter_index, tnum_index = letter_index, num_index
        for j in range(7):  # bishop's down left diagonal movement pattern taken
            tletter_index -= 1
            tnum_index += 1
            if tletter_index >= 0 and tnum_index <= 8:
                if board[tnum_index][tletter_index] == '  ' or board[tnum_index][tletter_index] in white_pieces:
                    show_list.append(notation[tnum_index][tletter_index])
                    if board[tnum_index][tletter_index] in white_pieces:
                        break
                else:
                    break
        tletter_index, tnum_index = letter_index, num_index
        for j in range(7):  # bishop's down right diagonal movement pattern taken
            tletter_index += 1
            tnum_index += 1
            if tletter_index <= 7 and tnum_index <= 8:
                if board[tnum_index][tletter_index] == '  ' or board[tnum_index][tletter_index] in white_pieces:
                    show_list.append(notation[tnum_index][tletter_index])
                    if board[tnum_index][tletter_index] in white_pieces:
                        break
                else:
                    break
        tnum_index = num_index
        for j in range(7):  # rook up movement pattern taken
            tnum_index += 1
            if tnum_index <= 8:
                if board[tnum_index][letter_index] == '  ' or board[tnum_index][letter_index] in white_pieces:
                    show_list.append(notation[tnum_index][letter_index])
                    if board[tnum_index][letter_index] in white_pieces:
                        break
                else:
                    break
        tnum_index = num_index
        for j in range(7):  # rook down movement pattern taken
            tnum_index -= 1
            if tnum_index >= 1:
                if board[tnum_index][letter_index] == '  ' or board[tnum_index][letter_index] in white_pieces:
                    show_list.append(notation[tnum_index][letter_index])
                    if board[tnum_index][letter_index] in white_pieces:
                        break
                else:
                    break
        tletter_index = letter_index
        for j in range(7):  # rook right movement pattern taken
            tletter_index += 1
            if tletter_index <= 7:
                if board[num_index][tletter_index] == '  ' or board[num_index][tletter_index] in white_pieces:
                    show_list.append(notation[num_index][tletter_index])
                    if board[num_index][tletter_index] in white_pieces:
                        break
                else:
                    break
        tletter_index = letter_index
        for j in range(7):  # rook left movement pattern taken
            tletter_index -= 1
            if tletter_index >= 0:
                if board[num_index][tletter_index] == '  ' or board[num_index][tletter_index] in white_pieces:
                    show_list.append(notation[num_index][tletter_index])
                    if board[num_index][tletter_index] in white_pieces:
                        break
                else:
                    break

    elif x1 == 'qu':
        tletter_index, tnum_index = letter_index, num_index
        for j in range(7):  # bishop's up left diagonal movement pattern taken
            tletter_index -= 1
            tnum_index -= 1
            if tletter_index >= 0 and tnum_index >= 1:
                if board[tnum_index][tletter_index] == '  ' or board[tnum_index][tletter_index] in black_pieces:
                    show_list.append(notation[tnum_index][tletter_index])
                    if board[tnum_index][tletter_index] in black_pieces:
                        break
                else:
                    break
        tletter_index, tnum_index = letter_index, num_index
        for j in range(7):  # bishop's up right diagonal movement pattern taken
            tletter_index += 1
            tnum_index -= 1
            if tletter_index <= 7 and tnum_index >= 1:
                if board[tnum_index][tletter_index] == '  ' or board[tnum_index][tletter_index] in black_pieces:
                    show_list.append(notation[tnum_index][tletter_index])
                    if board[tnum_index][tletter_index] in black_pieces:
                        break
                else:
                    break
        tletter_index, tnum_index = letter_index, num_index
        for j in range(7):  # bishop's down left diagonal movement pattern taken
            tletter_index -= 1
            tnum_index += 1
            if tletter_index >= 0 and tnum_index <= 8:
                if board[tnum_index][tletter_index] == '  ' or board[tnum_index][tletter_index] in black_pieces:
                    show_list.append(notation[tnum_index][tletter_index])
                    if board[tnum_index][tletter_index] in black_pieces:
                        break
                else:
                    break
        tletter_index, tnum_index = letter_index, num_index
        for j in range(7):  # bishop's down right diagonal movement pattern taken
            tletter_index += 1
            tnum_index += 1
            if tletter_index <= 7 and tnum_index <= 8:
                if board[tnum_index][tletter_index] == '  ' or board[tnum_index][tletter_index] in black_pieces:
                    show_list.append(notation[tnum_index][tletter_index])
                    if board[tnum_index][tletter_index] in black_pieces:
                        break
                else:
                    break
        tnum_index = num_index
        for j in range(7):  # rook up movement pattern taken
            tnum_index += 1
            if tnum_index <= 8:
                if board[tnum_index][letter_index] == '  ' or board[tnum_index][letter_index] in black_pieces:
                    show_list.append(notation[tnum_index][letter_index])
                    if board[tnum_index][letter_index] in black_pieces:
                        break
                else:
                    break
        tnum_index = num_index
        for j in range(7):  # rook down movement pattern taken
            tnum_index -= 1
            if tnum_index >= 1:
                if board[tnum_index][letter_index] == '  ' or board[tnum_index][letter_index] in black_pieces:
                    show_list.append(notation[tnum_index][letter_index])
                    if board[tnum_index][letter_index] in black_pieces:
                        break
                else:
                    break
        tletter_index = letter_index
        for j in range(7):  # rook right movement pattern taken
            tletter_index += 1
            if tletter_index <= 7:
                if board[num_index][tletter_index] == '  ' or board[num_index][tletter_index] in black_pieces:
                    show_list.append(notation[num_index][tletter_index])
                    if board[num_index][tletter_index] in black_pieces:
                        break
                else:
                    break
        tletter_index = letter_index
        for j in range(7):  # rook left movement pattern taken
            tletter_index -= 1
            if tletter_index >= 0:
                if board[num_index][tletter_index] == '  ' or board[num_index][tletter_index] in black_pieces:
                    show_list.append(notation[num_index][tletter_index])
                    if board[num_index][tletter_index] in black_pieces:
                        break
                else:
                    break

    elif x1 == 'ki':
        if num_index - 1 >= 1 and letter_index + 1 <= 7:
            if board[num_index - 1][letter_index + 1] == '  ' or board[num_index - 1][letter_index + 1] in black_pieces:
                show_list.append(notation[num_index - 1][letter_index + 1])
        if num_index - 1 >= 1 and letter_index - 1 >= 0:
            if board[num_index - 1][letter_index - 1] == '  ' or board[num_index - 1][letter_index - 1] in black_pieces:
                show_list.append(notation[num_index - 1][letter_index - 1])
        if num_index + 1 <= 8 and letter_index + 1 <= 7:
            if board[num_index + 1][letter_index + 1] == '  ' or board[num_index + 1][letter_index + 1] in black_pieces:
                show_list.append(notation[num_index + 1][letter_index + 1])
        if num_index + 1 <= 8 and letter_index - 1 >= 0:
            if board[num_index + 1][letter_index - 1] == '  ' or board[num_index + 1][letter_index - 1] in black_pieces:
                show_list.append(notation[num_index + 1][letter_index - 1])
        if num_index + 1 <= 8:
            if board[num_index + 1][letter_index] == '  ' or board[num_index + 1][letter_index] in black_pieces:
                show_list.append(notation[num_index + 1][letter_index])
        if num_index - 1 >= 1:
            if board[num_index - 1][letter_index] == '  ' or board[num_index - 1][letter_index] in black_pieces:
                show_list.append(notation[num_index - 1][letter_index])
        if letter_index + 1 <= 7:
            if board[num_index][letter_index + 1] == '  ' or board[num_index][letter_index + 1] in black_pieces:
                show_list.append(notation[num_index][letter_index + 1])
        if letter_index - 1 >= 0:
            if board[num_index][letter_index - 1] == '  ' or board[num_index][letter_index - 1] in black_pieces:
                show_list.append(notation[num_index][letter_index - 1])

    elif x1 == 'KI':
        if num_index - 1 >= 1 and letter_index + 1 <= 7:
            if board[num_index - 1][letter_index + 1] == '  ' or board[num_index - 1][letter_index + 1] in white_pieces:
                show_list.append(notation[num_index - 1][letter_index + 1])
        if num_index - 1 >= 1 and letter_index - 1 >= 0:
            if board[num_index - 1][letter_index - 1] == '  ' or board[num_index - 1][letter_index - 1] in white_pieces:
                show_list.append(notation[num_index - 1][letter_index - 1])
        if num_index + 1 <= 8 and letter_index + 1 <= 7:
            if board[num_index + 1][letter_index + 1] == '  ' or board[num_index + 1][letter_index + 1] in white_pieces:
                show_list.append(notation[num_index + 1][letter_index + 1])
        if num_index + 1 <= 8 and letter_index - 1 >= 0:
            if board[num_index + 1][letter_index - 1] == '  ' or board[num_index + 1][letter_index - 1] in white_pieces:
                show_list.append(notation[num_index + 1][letter_index - 1])
        if num_index + 1 <= 8:
            if board[num_index + 1][letter_index] == '  ' or board[num_index + 1][letter_index] in white_pieces:
                show_list.append(notation[num_index + 1][letter_index])
        if num_index - 1 >= 1:
            if board[num_index - 1][letter_index] == '  ' or board[num_index - 1][letter_index] in white_pieces:
                show_list.append(notation[num_index - 1][letter_index])
        if letter_index + 1 <= 7:
            if board[num_index][letter_index + 1] == '  ' or board[num_index][letter_index + 1] in white_pieces:
                show_list.append(notation[num_index][letter_index + 1])
        if letter_index - 1 >= 0:
            if board[num_index][letter_index - 1] == '  ' or board[num_index][letter_index - 1] in white_pieces:
                show_list.append(notation[num_index][letter_index - 1])


for i in commands:
    if i[0] == 'initialize':
        print(f"> {' '.join(i)}")
        print('OK')
        display(initial_board)
        board = initial_board
    elif i[0] == 'showmoves':
        print(f"> {' '.join(i)}")
        showmoves(i[1])
        if show_list == []:
            print('FAILED')
        else:
            print(' '.join(sorted(show_list)))
    elif i[0] == 'move':
        print(f"> {' '.join(i)}")
        move(i[1], i[2])
    elif i[0] == 'print':
        print(f"> {' '.join(i)}")
        display(board)
    elif i[0] == 'exit':
        print(f"> {' '.join(i)}")
        exit()
