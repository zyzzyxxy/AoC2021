import os
import numpy as np

board = []
lines = []

def remove_item(new_vals, item):
    res = []
    for i in new_vals:
        if i!= item:
            res.append(i)
    return res

class Point:
    def __init__(self,x,y):
        self.y = x
        self.x = y

class Line:
    def __init__(self, start_point, end_point):
        self.start_point = start_point
        self.end_point = end_point

    def is_vertical_or_horisintal(self):
        return self.start_point.x == self.end_point.x or self.start_point.y == self.end_point.y


def put_vert_hori_line_on_board(line):
    global board

    start_x = min(line.start_point.x,line.end_point.x)
    end_x = max(line.start_point.x,line.end_point.x)
    start_y = min(line.start_point.y,line.end_point.y)
    end_y = max(line.start_point.y,line.end_point.y)

    x_limit = end_x-start_x
    y_limit = end_y-start_y

    #x row
    #y col
    start = board[start_x][start_y]
    end = board[end_x][end_y]
    if y_limit > 0:
        for i in range(y_limit+1):
            board[start_x][start_y + i] += 1
    if x_limit > 0:
        for i in range(x_limit+1):
            board[start_x+i][start_y] += 1

    start2 = board[start_x][start_y]
    end2 = board[end_x][end_y]

def put_diagonal_line_on_board(line):
    global board

    start_x = line.start_point.x
    end_x = line.end_point.x
    start_y = line.start_point.y
    end_y = line.end_point.y

    x_limit = end_x-start_x
    y_limit = end_y-start_y
    start = board[start_x][start_y]
    end = board[end_x][end_y]
    rounds = 0
    for i in range(np.abs(y_limit) + 1):
        if start_x < end_x:
            if start_y < end_y:
                board[start_x + i][start_y + i] += 1
            else:
                board[start_x + i][start_y - i] += 1
        else:
            if start_y < end_y:
                board[start_x - i][start_y + i] += 1
            else:
                board[start_x - i][start_y - i] += 1


    start2 = board[start_x][start_y]
    end2 = board[end_x][end_y]

    b = board
    #print("as")

def put_lines_in_board():
    global board
    global lines
    b = board
    for line in lines:
        if line.is_vertical_or_horisintal():
            put_vert_hori_line_on_board(line)
        else:
            put_diagonal_line_on_board(line)


def count_high_vals_board():
    global board
    sum = 0
    vals = []
    for row in board:
        for val in row:
            if val >= 2:
                sum += 1
                vals.append(val)

    print(vals)
    print(vals.__len__())
    print(sum)


def print_board():
    global board
    for i in range(20):
        print(board[i+40][20:40])


def run():
    global board
    global lines
    board = np.zeros((1000,1000))
    config_filename = os.getcwd() + "/day5"
    file = open(config_filename, 'r').read()
    arr = file.splitlines();
    for line in arr:
        vals = line.split(" -> ")
        x1 = int(vals[0].split(",")[0])
        y1 = int(vals[0].split(",")[1])
        x2 = int(vals[1].split(",")[0])
        y2 = int(vals[1].split(",")[1])
        sp = Point(x1,y1)
        ep = Point(x2,y2)
        line = Line(sp, ep)
        lines.append(line)

    l = lines
    print(lines[0])

    put_lines_in_board()
    count_high_vals_board()
    #print_board()

#14811 too high
#7619 too high
#7278 too low

#7318 right


#---section 2
#21243 too high
#21214 too high
#12979 wrong
#7333 too low

#19939 right
if __name__ == '__main__':
    run()