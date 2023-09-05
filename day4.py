import os
import numpy as np

bingo_boards_global = []
boards = []

class Board:
    def __init__(self, id, board):
        self.id = id
        self.visited = False
        self.bingo = False
        self.bingo_nbr = 0
        self.bingo_prod = 0
        self.board = board

    def visit(self, nbr):
        for row in self.board:
            for i in range(row.__len__()):
                tuple = row[i]
                if nbr == tuple[0]:
                    row[i] = [nbr, True]
                    self.bingo_nbr = nbr
    def calc_prod(self):
        sum = 0
        for row in self.board:
            for tuple in row:
                if tuple[1] == False:
                    sum += int(tuple[0])
        self.bingo_prod = sum * int(self.bingo_nbr)
        print(self.bingo_prod)


def getBoards(lines):
    len = lines.__len__()
    counter = 0
    boards = []
    visited = False

    board = []
    row = []
    for line in lines:
        if counter == 99:
            print("99")
        row = []
        nbrs = line.split(" ")
        if nbrs.__len__()>1:
            for n in nbrs:
                if n.__len__()>0:
                    row.append([n, visited])
            board.append(row)
        else:
            b = Board(counter, board)
            boards.append(b)
            counter +=1
            board = []

    b = Board(counter, board)
    boards.append(b)

    return boards


def visit_nbr(n):
    global boards
    for board in boards:
        try:
            board.visit(n)
        except Exception:
            print(Exception)
            print(board)


def check_vertical(board):
    bingo = True
    for i in range(5):
        for row in board.board:
            if row[i][1]==False:
                bingo = False
        if bingo:
            return True
        bingo = True
    return False


def check_horisontal(board):
    bingo = True
    for row in board.board:
        for tuple in row:
            if tuple[1] == False:
                bingo = False
        if bingo:
            return True
        else:
            bingo = True
    return False


def remove_id(id):
    global boards
    boards = list(filter(lambda x: (x.id != id), boards))


def check_bingo():
    global boards
    global bingo_boards_global

    for board in boards:
        if check_vertical(board) or check_horisontal(board):
            board.bingo = True
            board.calc_prod()
            bingo_boards_global.append(board)
            remove_id(board.id)


def calc_prod(bingo_board, win_nbr):
    sum=0
    for row in bingo_board:
        for tuple in row:
            if tuple[1]==False:
                sum += int(tuple[0])
    prod = sum*int(win_nbr)
    print(prod)


def clean_bingo_boards():
    global boards
    for board in boards:
        if check_vertical(board) or check_horisontal(board):
            boards.remove(board)
    return boards


def board_in_list(board, bingo_boards):
    same = True
    for b in bingo_boards:
        for i in range(5):
            for j in range(5):
                if not board[0][i][j][0] == b[0][i][j][0]:
                    same = False
        if same:
            return same
        same = True
    return False

def run():
    global bingo_boards_global
    global boards
    config_filename = os.getcwd() + "/day4"
    file = open(config_filename, 'r').read()
    #bingo nbrs
    nbrs = file.split(" ")[0].split("\n")[0].split(",");
    #print(nbrs)

    lines = file.splitlines()[2:]
    #print(lines)

    boards = getBoards(lines)
    bingo_boards = []
    for n in nbrs:
        #boards = clean_bingo_boards(boards)
        visit_nbr(n)
        check_bingo()



    foo = bingo_boards_global
    foo2 = boards
    print(bingo_boards_global)



#6594
#wrong guess:
#5664
#Low
#4848
#5320

#High
#10080

if __name__ == '__main__':
    run()