import numpy


def check_low(map_arr, i, j):
    low = True
    rows = map_arr.__len__()
    cols = map_arr[0].__len__()
    if i != 0:
        if map_arr[i][j] >= map_arr[i-1][j]:
            return False
    if j != 0:
        if map_arr[i][j] >= map_arr[i][j-1]:
            return False
    if i < rows -1:
        if map_arr[i][j] >= map_arr[i+1][j]:
            return False
    if j < rows -1:
        if map_arr[i][j] >= map_arr[i][j+1]:
            return False
    return True

def get_low_points(map_arr):
    result_arr = []
    for i in range(map_arr.__len__()):
        for j in range(map_arr[0].__len__()):
            if check_low(map_arr, i, j):
                result_arr.append([i,j])
    return result_arr


def coord_in_basin(coord, basin):
    for c in basin:
        if c[0] == coord[0] and c[1] == coord[1]:
            return True
    return False


def get_basin(map_arr, coord):
    basin = []
    row = coord[0]
    col = coord[1]
    rows = map_arr.__len__()
    cols = map_arr[0].__len__()
    if map_arr[row][col] == 9:
        return []

    if not coord_in_basin(coord, basin):
        basin.append(coord)

    if row > 0 and map_arr[row-1][col] > map_arr[row][col]:
        basin.extend(get_basin(map_arr, [row-1, col]))
    if col > 0 and map_arr[row][col-1] > map_arr[row][col]:
        basin.extend(get_basin(map_arr,[row, col-1]))
    if row < rows - 1 and map_arr[row+1][col] > map_arr[row][col]:
        basin.extend(get_basin(map_arr,[row+1, col]))
    if col < cols -1 and map_arr[row][col+1] > map_arr[row][col]:
        basin.extend(get_basin(map_arr,[row, col+1]))

    return basin


def clean_duplicates(basin):
    result = []
    for coord in basin:
        if not coord in result:
            result.append(coord)
    return result

def get_basins(map_arr, coordinates):
    basins = []
    for coord in coordinates:
        basin = get_basin(map_arr, coord)
        basin = clean_duplicates(basin)
        print(basin.__len__())
        print(basin)
        basins.append(len(basin))
    return basins


def run():
    file = open("day9")
    lines = file.read().splitlines()
    print(lines[0].__len__())
    map_arr = numpy.zeros((100, 100))
    for i in range(100):
        for j in range(100):
            map_arr[i][j] = int(lines[i][j])

    arr = get_low_points(map_arr)
    #incremented_list = [x + 1 for x in arr]
    basins = numpy.array(get_basins(map_arr, arr))
    print(arr)
    print(basins.sort())
    print(basins)
    print(basins[-1] * basins[-2] * basins[-3])
    print(590*637*807)
    #303294810 too high




run()