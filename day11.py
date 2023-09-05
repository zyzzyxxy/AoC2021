from pandas import *

octopuses = dict()
flashes = 0
flashes2 = 0
step = 0



class Coord:
    def __init__(self, row,col):
        self.row = row
        self.col = col


class Octopus:
    def __init__(self, coord, counter):
        self.coord = coord
        self.counter = counter

    flash = False
    did_flash = False
    def should_flash(self):
        val = self.counter > 9 and not self.did_flash
        return val


    def increment(self):
        self.counter +=1

    def reset(self):
        self.flash = False
        self.counter = 0


def increment(coord):
    global octopuses
    c = octopuses[coord].coord
    octopuses[get_key(c.row, c.col)].increment()


def get_coords_around_coord(coord):
    coord_list = []
    row = coord.row
    col = coord.col
    rows = [row]
    cols = [col]
    if row >0:
        rows.append(row-1)
    if row <9:
        rows.append(row+1)
    if col > 0:
        cols.append(col - 1)
    if col < 9:
        cols.append(col + 1)
    for r in rows:
        for c in cols:
            if r == row and c == col:
                pass
            else:
                new_coord = Coord(r, c)
                coord_list.append(new_coord)
    return coord_list

def do_flashes():
    global octopuses
    increment_list = []
    for key in octopuses:
        if octopuses[key].should_flash():
            coord =  octopuses[key].coord
            increment_list.extend(get_coords_around_coord(coord))
            octopuses[key].did_flash = True

    while len(increment_list) > 0:
        coord = increment_list.pop(0)
        key = get_key(coord.row, coord.col)
        o = octopuses[key]
        increment(key)
        if octopuses[key].should_flash():
            increment_list.extend(get_coords_around_coord(coord))
            octopuses[key].did_flash = True



def increment_all():
    global octopuses
    for key in octopuses:
        increment(key)


def reset_octos():
    global octopuses
    global flashes
    global step
    flashes_this_turn = 0
    for key in octopuses:
        if octopuses[key].did_flash:
            flashes_this_turn +=1
            octopuses[key].did_flash = False
            octopuses[key].counter = 0
            flashes +=1
    if flashes_this_turn == 100:
        print("all flash at:", step)


def run_steps(steps):
    global step
    s = step
    for i in range(steps):
        step += 1

        increment_all()
        do_flashes()
        reset_octos()


def get_key(row, col):
    return str(row) + ":"+str(col)


def flash_val2(row, col, arr):
    arr[row][col] = 0
    for i in range(3):
        for j in range(3):
            r = row - 1 + i
            c = col - 1 + j
            if r >= 0 and r <= 9 and c>=0 and c<=9 and not (c == col and r == row):
                if arr[r][c] != 0:
                    arr[r][c] +=1
    return arr


def flash2(arr):
    global flashes2
    row = col = 10
    flashes = 0
    for r in range(row):
        for c in range(col):
            val = arr[r][c]
            if val > 9 :
                arr = flash_val2(r, c, arr)
                flashes += 1
                flashes2 += 1
    if flashes > 0:
        arr = flash2(arr)
    return arr


def run_steps2(steps, arr):

    row = col = 10
    for i in range(steps):
        #increment
        for r in range(row):
            for c in range(col):
                arr[r][c] += 1
        arr = flash2(arr)
    return arr

def run():
    global octopuses
    global flashes
    file = open("day11")
    lines = file.read().splitlines()

    arr = []
    for row in range(len(lines)):
        arr.append([])
        for col in range(len(lines[0])):
            arr[row].append(int(lines[row][col]))
            cord = get_key(row, col)
            octopuses[cord] = Octopus(Coord(row,col), int(lines[row][col]))

    run_steps(1000)
    arr =run_steps2(290, arr)
    print( DataFrame(arr) )
    print(octopuses)
    print(flashes)
    print(flashes2)


run()