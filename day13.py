import numpy as np
from pandas import DataFrame

def split_matrix_horizontal(matrix, value):
    upper = []
    lower = []
    for i in range (matrix.shape[0]):
        if i < value:
            upper.append(matrix[i])
        elif i > value:
            lower.append(matrix[i])
    return upper, lower


def split_matrix_vertical(matrix, value):
    left = []
    right = []
    for row in matrix:
        left.append(row[:value])
        right.append(row[value+1:])
    return left, right


def add_horizontals(upper, lower):
    if upper.__len__() == lower.__len__():
        return upper + lower
    else:
        diff = abs(upper.__len__() - lower.__len__())
        print("diff","hori", diff, type(upper), type(lower))
        if upper.__len__() > lower.__len__():
            result = upper[diff:] + lower
        else:
            result = lower[diff:] + upper
        return result


def add_vertical(left, right):
    left = np.array(left)
    right = np.array(right)
    if left.shape[1]== right.shape[1]:
        return left + right
    else:
        diff = abs(left.shape[1] - right.shape[1])
        print("diff","vert", diff)
        if left.__len__() > right.__len__():
            for i in range(left.__len__()):
                result = left[i][diff:] + right[i]
        else:
            for i in range(left.__len__()):
                result = right[i][diff:] + left[i]
        return result


def fold_matrix(matrix, axis, value):
    if axis == "y":
        upper, lower = split_matrix_horizontal(matrix, value)
        lower = np.flip(lower, axis=0)
        result = add_horizontals(upper, lower)
        return result
    if axis == "x":
        left, right = split_matrix_vertical(matrix, value)
        right = np.flip(right, axis=1)
        result = add_vertical(left,right)
        return result


def calc_values_in_arr(matrix):
    rows = matrix.__len__()
    cols = matrix[0].__len__()
    sum = 0
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] != 0:
                sum +=1
    return sum


def matrix_to_readable(matrix):
    rows = matrix.__len__()
    cols = matrix[0].__len__()
    result = []
    for row in range(rows):
        res_row = []
        for col in range(cols):
            if matrix[row][col] != 0:
                res_row.append("#")
            else:
                res_row.append(".")
        result.append(res_row)
    return result


def run():
    file = open("day13")
    lines = file.read().splitlines()



    #dots = lines[:-3]
    dots = lines[:-13]
    print (dots)
    X = []
    Y = []
    for dot in dots:
        x, y = dot.strip().split(",")
        X.append(int(x))
        Y.append(int(y))

    height = max(Y)+2
    width = max(X)+1

    matrix = np.zeros((height, width))
    for i in range(X.__len__()):
        matrix[Y[i]][X[i]] = 1

    instructions = lines[-12:]
    #instructions = lines[-2:]
    print(instructions)
    I = []
    for i in instructions:
        axis, value = i.split("=")
        axis = axis[-1]
        value = int(value)
        I.append([axis, value])
    print(I)

    for instruction in instructions:
        instruction = instruction.split("=")
        matrix = fold_matrix(matrix, instruction[0][-1], int(instruction[1]))

    test_m = np.matrix([[1,2,3,4,], [5,6,7,8]])
    add_m = np.matrix([[1,1,1],[0,0,0]])
    #test_res = add_vertical(test_m, add_m)
    #print("test", test_res)
#    test_m[1:] += add_m
    print(test_m)
    print(np.flip(test_m, axis=0))
    values = calc_values_in_arr(matrix)
    str_matrix = matrix_to_readable(matrix)
    print(values)
    print(DataFrame(matrix))
    print(DataFrame(str_matrix))
    print(str_matrix)

    output_file = open("output_13", "a")
    for i in range(str_matrix[0].__len__() //5):
        for row in str_matrix:
            print(row[i*5:i*5+5])
        print()
    output_file.close()

run()