import os
import numpy as np
from bitarray import bitarray
import struct


def remove_item(new_vals, item):
    res = []
    for i in new_vals:
        if i!= item:
            res.append(i)
    return res


def run():
    config_filename = os.getcwd() + "/day3"
    file = open(config_filename, 'r').read()
    arr = file.splitlines();
    gamma = 0
    epsilon = 0
    counter_arr = np.zeros(12)
    counter_arr2 = np.ones(12)
    ox = arr
    co02 = arr
    counter = 0

    while ox.__len__()>1 and counter <12:
        zeros=0
        ones=0
        for item in ox:
            if int(item[counter]) == 0:
                zeros +=1
            if int(item[counter]) == 1:
                ones += 1

        #check common
        common_val = 1
        if(zeros>ones):
            common_val=0

        ox = list(filter(lambda s: int(s[counter]) == common_val, ox))
        counter +=1

    print(ox)
    counter = 0
    while co02.__len__()>1 and counter <12:
        zeros=0
        ones=0
        for item in co02:
            if int(item[counter]) == 0:
                zeros +=1
            if int(item[counter]) == 1:
                ones += 1

        #check common
        un_common_val = 0
        if(zeros>ones):
            un_common_val=1

        new_vals = co02

        if counter == 11:
            print()
            pass
        for item in co02:
            item_val = int(item[counter])
            if item_val != un_common_val and new_vals.__len__()>1:
                new_vals=remove_item(new_vals,item)
        co02 = new_vals


        counter +=1

    print(co02)
    print(int('010010001001',2), int('111000100101',2))
    print(int('010010001001',2) * int('111000100101',2))


#419*3676
#419*3677
#guessed:
#1536986
#1540663

#010010001001
#111000100101
if __name__ == '__main__':
    run()