import math


def cost_to_move(nbr, position):
    moves = math.fabs(nbr - position)
    cost = moves*(moves+1)/2
    return cost

def cost_to_move_all(nbrs, position):
    sum = 0
    for n in nbrs:
        sum += cost_to_move(n, position)
    return sum


def run():
    values = open("day7").read().split(",")
    values = list(map(lambda x: int(x), values))
    mean = int(math.floor(sum(values)/values.__len__()))
    max_val = max(values)
    min_val = min(values)
    best_pos = 10000000000
    best_sum = 10000000000


    for i in range(max_val-min_val):
        summ = 0
        pos = min_val + i
        summ = cost_to_move_all(values, pos)
        if summ < best_sum:
            best_sum = summ
            best_pos = pos

    print(best_sum)
    print(best_pos)
    print( mean)
    values.sort()
    med = values[values.__len__()/2]




run()