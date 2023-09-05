from pandas import DataFrame
MAX_VAL = 999999
import numpy

class Coord():
    def __init__(self, row, col):
        self.row = row
        self.col = col

class Node():
    def __init__(self, coord, value):
        self.coord = coord
        self.value = value

class edge():
    def __init__(self, frm, to, cost):
        self.frm = frm
        self.to = to
        self.cost = cost

class Graph():
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges

    def calc_shortest_path(self, start_node):
        pass


def get_nodes(lines):
    nodes = []
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            val = int(j)
            node = Node(Coord(i,j), val)
            nodes.append(node)
    return nodes


def get_arr(lines):
    arr = []
    for i in range(len(lines)):
        row = []
        for j in range(len(lines[0])):
            row.append(int(lines[i][j]))
        arr.append(row)
    return arr


def get_values_around(cost_dict, param, max_row, max_col):
    row, col = param
    values=[]
    min_val = 100000
    min_coord = []
    if row > 0 and cost_dict[(row-1,col)] < min_val:
        min_val = cost_dict[(row-1,col)]
        min_coord = [row-1, col]
    if row < max_row-1 and cost_dict[(row+1,col)] < min_val:
        min_val = cost_dict[(row + 1, col)]
        min_coord = [row+1, col]
    if col > 0 and cost_dict[(row,col-1)] < min_val:
        min_val = cost_dict[(row, col-1)]
        min_coord = [row, col-1]
    if col < max_col-1 and  cost_dict[(row,col+1)] < min_val:
        min_val = cost_dict[(row , col+1)]
        min_coord = [row, col+1]
    return min_val, min_coord




def get_cost_chart(arr, start_node):
    node_cost = {}
    rows = arr.__len__()
    cols =arr[0].__len__()
    path=[]
    for i in range(rows):
        for j in range(cols):
            node_cost[(i,j)] = MAX_VAL
    node_cost[start_node] = 0
    for times in range(10):
        for i in range(arr.__len__()):
            for j in range(arr[0].__len__()):
                if (i,j)!= start_node:
                    if (i,j)== (13,3):
                        print()
                    min_val, min_coord = get_values_around(node_cost, [i,j], rows, cols)
                    node_cost[(i,j)] = min_val + arr[i][j]
                    if (i,j)== (13,3):
                        print(node_cost[(i,j)])
        #print(node_cost[(49,49)])
    for i in range(arr.__len__()):
        for j in range(arr[0].__len__()):
            if (i, j) != start_node:
                min_val, min_coord = get_values_around(node_cost, [i, j], rows, cols)
                node_cost[(i, j)] = min_val + arr[i][j]
                path.append(min_coord)

    return node_cost, path

def incr(lst, i):
    return [x+i for x in lst]

def get_big_arr(arr):
    rows = arr.__len__()
    cols = arr[0].__len__()
    big_arr = []
    nArr = numpy.array(arr)
    for row in arr:
        bigRow = []
        for i in range(5):
            for val in row:
                new_val = val + i
                if new_val>9:
                    new_val -=9
                bigRow.append(new_val)

        big_arr.append(bigRow)

    temp_arr = big_arr.copy()
    for i in range(4):
        for row in temp_arr:
            big_arr.append(incr(row, i+1))

    for row in range(big_arr.__len__()):
        for col in range(big_arr[0].__len__()):
            if big_arr[row][col]>9:
                big_arr[row][col] = big_arr[row][col]-9

    print(big_arr)
    print(DataFrame(big_arr))

    return big_arr

def run():
    global MAX_VAL

    file = open("day15")
    lines =  file.read().splitlines()

    nodes = get_nodes(lines)
    arr = get_arr(lines)
    big_arr = get_big_arr(arr)
    node_cost, path = get_cost_chart(big_arr, (0,0))
    print(node_cost)

    f = open("output_15", "a")

    for row in range(big_arr.__len__()):
        for col in range(big_arr[0].__len__()):
            val = big_arr[row][col]
            f.write(str(val))
        f.write("\n")
    f.close()
    print(node_cost[(49,49)])
    #print(path)
    #for key in node_cost.keys():
    #    print(key, node_cost[key])


#494 too high
#491 too high


#2587 too low
run()