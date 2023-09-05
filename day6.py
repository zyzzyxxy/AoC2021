import os
import math
import numpy as np


def get_fishes(fish, days):
    days = days - fish
    if(days<1):
        return 0
    #sum_new_fishes = int((days)/7)
    sum_new_fishes = math.ceil((days)/7)
    total_new_fishes=0
    if(sum_new_fishes>0):
        total_new_fishes = sum_new_fishes
        for i in range(sum_new_fishes):
            total_new_fishes += get_fishes(9, days)
            days = days - 7

    return total_new_fishes


def calc_fishes(fishes, days):
    counter = 0
    sum = 0
    for fish in fishes:
        sum += 1 + get_fishes(fish, days)
        print("fish done")

    print(sum)


def get_fish_matrix(days):
    matrix = np.ones(shape=(9,days+1))
    for day in range(days+1):
        for fish in range(9):
            if day ==0:
                matrix[fish][day] = 1
            else:
                if fish == 0:
                    value =  matrix[8][day-1] + matrix[6][day-1]
                    matrix[fish][day] = value
                else:
                    if (day - fish)<0:
                        matrix[fish][day] = 1
                    else:
                        if day==13 and fish == 6:
                            print()
                        matrix[fish][day] = matrix[0][day-fish]


    return matrix


def run():
    config_filename = os.getcwd() + "/day6"
    file = open(config_filename, 'r').read()
    arr = file.split(",")
    fishes = list(map(lambda x: (int(x)), arr))

    append_counter=0

    days = 256

    fish = 8

    fish_matrix = get_fish_matrix(days)
    print(fish_matrix[fish][days])

    sum_x = 0
    for fish in fishes:
        sum_x+=fish_matrix[fish][days]

    print("sum_x: ", sum_x)
    #calc_fishes(fishes, 256)
    #calc_fishes([fishes[0]], 80)
    #fishes = [fishes[0]]
    test_fish = 0
    #fishes[0] = test_fish
    #fishes = [fish]
    for i in range(days):
        for i in range (fishes.__len__()):
            if fishes[i] ==0:
                append_counter += 1
                fishes[i] = 6
            else:
                fishes[i] -=1
        for j in range(append_counter):
            pass
            fishes.append(8)
        append_counter = 0

    print(fishes.__len__())

#387413
if __name__ == '__main__':
    run()