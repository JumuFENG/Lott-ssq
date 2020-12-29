# Python 3
# -*- coding: utf-8 -*-

import random

def get_blue_number_weight(blueball):
    weight_arr = [-1] * 16
    for x in blueball:
        weight_arr[x-1] = blueball.index(x)
        arr_filled = True
        for i in range(0,len(weight_arr)):
            if weight_arr[i] == -1:
                arr_filled = False
                break
        if arr_filled:
            break
    for i in range(0, len(weight_arr)):
        if weight_arr[i] < 5:
            weight_arr[i] = weight_arr[i] + 1
        elif weight_arr[i] > 16:
            weight_arr[i] = 8
        else:
            weight_arr[i] = 16
    return [0] + weight_arr

def get_random_blue_number(blueball):
    weight_arr = get_blue_number_weight(blueball)
    print(weight_arr)
    data_list = []
    for x in range(0, len(weight_arr)):
        data_list += [x] * weight_arr[x]
    return random.choice(data_list)

if __name__ == '__main__':
    blueball = [16, 4, 10, 7, 11, 13, 12, 3, 15, 3, 12, 15, 5, 7, 10, 2, 3, 11, 5, 16, 4, 13, 5, 16, 10, 1, 9, 8, 8, 15, 7, 12, 2, 10, 15, 2, 8, 15, 3, 16, 6, 10, 12, 10, 6, 16, 7, 12, 9, 15, 1, 14, 4, 12, 6, 16, 12, 3, 4, 8, 15, 4, 10, 8, 7, 8, 1, 14, 5, 4, 8, 14, 7, 3, 14, 12, 2, 1, 15, 8, 15, 4, 2, 1, 8, 16, 7, 7, 3, 13, 4, 2, 15, 15, 6, 11, 3, 1, 13, 9, 3, 5, 8, 6, 6, 2, 8, 8, 2, 7, 14, 3, 13, 4, 7, 1, 7, 14, 9, 1, 9, 12, 16, 10, 9, 4, 3, 3, 11, 2, 14, 2, 7, 8, 12, 14, 16, 3, 9, 9, 14, 5, 11, 11, 6, 12, 3, 3, 7, 7, 4, 16, 7, 8, 10, 16, 3, 1, 6, 2, 2, 3, 7, 4, 1, 1, 5, 1, 15, 1, 1, 8, 10, 13, 2, 14, 1, 10, 12, 12, 5, 8, 8, 9, 9, 11, 1, 6, 2, 8, 11, 4, 11, 13, 4, 6, 4, 3, 3, 2, 10, 7, 16, 12, 15, 14, 3, 4, 8, 15, 4, 9, 1, 10, 11, 4, 10, 12, 16, 1, 12, 1, 6, 12, 16, 1, 10, 11, 8, 16, 9, 2, 15, 10, 14, 6, 14, 7, 13, 4, 16, 11, 8, 5, 10, 8, 16, 3, 15, 4, 16, 16, 10, 11, 13, 14, 4, 10, 13, 7, 4, 12, 6, 4, 9, 5, 4, 3, 1, 14, 7, 2, 15, 12, 15, 12, 7, 3, 1, 11, 15, 11, 3, 15, 5, 1, 1, 11, 16, 6, 13, 14, 11, 4, 14, 15, 9, 9, 14, 16, 12, 13, 6, 1, 12, 16, 2, 12, 5, 2, 2, 1, 10, 11, 1, 12, 9, 5, 15, 11, 14, 9, 4, 8, 2, 15, 2, 1, 10, 1, 1, 16, 5, 9, 2, 6, 13, 13, 12, 9, 5, 7, 16, 7, 7, 14, 14, 3, 16, 6, 3, 3, 9, 3, 3, 13, 12, 10, 13, 11, 9, 10, 8, 3, 10, 12, 1, 5, 10, 1, 5, 12, 11, 7, 10, 11, 7, 13, 1, 7, 16, 6, 14, 4, 7, 2, 2, 7, 3, 1, 6, 7, 12, 13, 16, 3, 9, 10, 4, 15, 15, 6, 6, 14, 7, 5, 16, 5, 4, 14, 2, 16, 3, 14, 5, 9, 7, 12, 16, 15, 7, 6, 12, 11, 3, 7, 13, 12, 11, 6, 11, 4, 16, 4, 5, 16, 5, 16, 8, 13, 12, 14, 10, 12, 9, 14, 6, 5, 8, 16, 2, 3, 12, 16, 4, 11, 11, 11, 2, 2, 8, 12, 16, 3, 3, 10, 15, 7, 16, 14, 16, 9, 2, 1, 13, 5, 11, 12, 14, 16, 1, 6, 2, 7, 14, 1, 11, 16, 2, 4, 1, 3, 6, 16, 6, 12, 9, 3, 9, 12, 6, 6, 7, 9, 2, 12, 10, 5, 8, 8, 16, 14, 13, 7, 2, 14, 2, 3, 12, 5, 15, 4, 3, 7, 15, 4, 10, 11, 4, 9, 11, 16, 6, 5, 8, 6, 7, 11, 7, 10, 7, 2, 10, 5, 6, 8, 4, 4, 4, 15, 5, 5, 15, 12, 13, 15, 11, 3, 2, 10, 9, 5, 8, 7, 13, 14, 15, 9, 10, 8, 9, 12, 2, 1, 13, 6, 7, 16, 7, 14, 13, 15, 8, 5, 7, 16, 3, 15, 6, 7, 7, 5, 7, 14, 12, 10, 6, 5, 13, 12, 15, 10, 3, 7, 14, 3, 12, 13, 15, 7, 2, 1, 14, 13, 16, 10, 3, 10, 16, 8, 9, 9, 4, 14, 2, 13, 9, 9, 14, 12, 4, 8, 5, 16, 1, 4, 16, 4, 11, 13, 1, 4, 6, 6, 1, 16, 12, 10, 9, 6, 7, 7, 8, 15, 12, 5, 16, 5, 4, 9, 7, 14, 2, 2, 10, 1, 7, 12, 13, 2, 1, 1, 11, 1, 4, 5, 14, 3, 7, 9, 8, 8, 15, 11, 11, 14, 11, 4, 1, 16, 12, 2, 10, 4, 16, 14, 3, 1, 12, 9, 4, 3, 16, 3, 16, 3, 11, 15, 15, 15, 3, 12, 15, 1, 5, 1, 12, 13, 7, 7, 5, 10, 10, 4, 5, 16, 7, 7, 1, 15, 12, 6, 4, 2, 6, 12, 14, 12, 1, 16, 13, 7, 3, 12, 11, 13, 9, 7, 5, 15, 13, 16, 4, 11, 2, 12, 9, 11, 12, 1, 7, 4, 15, 1, 3, 10, 4, 6, 6, 12, 10, 1, 7, 7, 12, 16, 8, 12, 12, 11, 3, 1, 12, 11, 12, 4, 13, 15, 8, 13, 12, 1, 14, 6, 5, 8, 9, 1, 4, 7, 4, 10, 8, 1, 11, 15, 1, 9, 11, 12, 5, 15, 5, 7, 13, 2, 11, 2, 16, 9, 4, 8, 4, 5, 8, 15, 15, 10, 14, 16, 12, 1, 12, 16, 4, 13, 14, 15, 4, 14, 2, 7, 10, 12, 9, 4, 5, 10, 9, 1, 7, 2, 15, 8, 6, 16, 12, 14, 3, 3, 3, 13, 5, 16, 11, 7, 7, 14, 7, 13, 14, 10, 1, 10, 8, 4, 4, 9, 12, 13, 4, 11, 1, 6, 15, 9, 14, 3, 8, 13, 15, 10, 15, 5, 6, 12, 8, 9, 1, 13, 10, 1, 11, 14, 16, 13, 10, 6, 11, 13, 9, 10, 1, 2, 13, 8, 14, 10, 2, 14, 12, 1, 6, 4, 5, 11, 9, 4, 9, 3, 4, 16, 3, 10, 7, 3, 2, 6, 2, 2, 16, 15, 4, 13, 4, 13, 7, 11, 14, 7, 15, 8, 8, 1, 5, 7, 14, 13, 9, 15, 6, 8, 8, 8, 12, 11, 10, 7, 2, 7, 10, 11, 6, 12, 2, 16, 14, 7, 11, 16, 6, 16, 6, 14, 16, 9, 8, 6, 13, 11, 8, 1, 4, 14, 2, 8, 13, 13, 6, 16, 15, 10, 15, 12, 9, 14, 2, 8, 7, 16, 7, 3, 6, 6, 12, 7, 14, 10, 14, 5, 1, 14, 16, 9, 10, 16, 12, 15, 7, 15, 10, 8, 9, 15, 13, 8, 2, 11, 16, 12, 14, 14, 4, 15, 12, 4, 1, 5, 10, 5, 9, 10, 11, 1, 8, 1, 15, 2, 11, 14, 4, 10, 8, 3, 10, 6, 12, 10, 1, 12, 9, 8, 14, 8, 14, 16, 16, 7, 2, 11, 7, 11, 9, 16, 16, 7, 8, 7, 9, 7, 13, 13, 8, 5, 11, 6, 9, 11, 7, 3, 1, 11, 3, 14, 7, 15, 10, 7, 14, 6, 10, 8, 13, 14, 5, 11, 16, 3, 9, 6, 13, 16, 13, 15, 3, 3, 14, 3, 11, 9, 9, 6, 6, 6, 6, 7, 2, 12, 12, 2, 12, 15, 9, 5, 5, 16, 6, 14, 14, 13, 2, 3, 14, 4, 12, 6, 12, 6, 16, 3, 5, 10, 6, 11, 14, 13, 2, 9, 1, 3, 3, 6, 12, 13, 12, 11, 8, 9, 5, 7, 11, 1, 6, 5, 9, 5, 15, 8, 9, 2, 9, 12, 2, 15, 1, 13, 12, 8, 9, 12, 6, 4, 10, 7, 1, 7, 13, 7, 9, 13, 3, 4, 6, 6, 9, 15, 15, 14, 7, 11, 16, 15, 2, 10, 12, 3, 1, 5, 8, 7, 1, 11, 9, 11, 11, 16, 13, 11, 9, 3, 14, 15, 6, 6, 13, 9, 3, 13, 9, 16, 4, 3, 2, 15, 2, 10, 16, 9, 6, 7, 2, 15, 13, 3, 16, 11, 11, 15, 9, 8, 5, 14, 4, 6, 6, 3, 12, 12, 12, 15, 11, 8, 5, 6, 8, 11, 6, 10, 16, 12, 14, 11, 12, 7, 14, 1, 1, 4, 4, 10, 1, 14, 4, 4, 9, 11, 2, 10, 11, 6, 9, 3, 3, 16, 2, 10, 8, 16, 9, 9, 5, 16, 4, 4, 3, 8, 3, 11, 12, 16, 6, 13, 2, 4, 3, 11, 16, 15, 10, 8, 15, 12, 13, 1, 5, 10, 11, 8, 4, 8, 6, 16, 9, 13, 6, 13, 13, 10, 13, 16, 14, 10, 10, 4, 3, 16, 2, 11, 6, 3, 7, 13, 7, 12, 10, 16, 7, 1, 15, 6, 12, 11, 16, 8, 16, 16, 3, 2, 7, 1, 10, 4, 5, 16, 9, 5, 15, 4, 12, 15, 10, 15, 14, 1, 9, 12, 11, 6, 5, 14, 5, 16, 15, 5, 5, 9, 4, 3, 16, 12, 4, 1, 9, 10, 15, 6, 4, 12, 9, 5, 9, 10, 13, 13, 1, 14, 12, 2, 12, 12, 10, 12, 12, 3, 2, 5, 3, 3, 1, 16, 6, 2, 10, 16, 8, 15, 8, 14, 15, 14, 15, 14, 8, 8, 9, 4, 15, 13, 13, 13, 12, 11, 5, 2, 8, 4, 15, 12, 10, 7, 1, 1, 12, 9, 14, 5, 5, 8, 5, 16, 1, 8, 13, 7, 16, 8, 13, 10, 13, 4, 15, 5, 5, 13, 5, 4, 5, 10, 13, 1, 14, 6, 9, 12, 3, 1, 8, 11, 14, 10, 6, 15, 9, 5, 6, 10, 10, 6, 1, 15, 6, 16, 16, 12, 1, 5, 9, 2, 10, 6, 15, 16, 9, 5, 1, 7, 15, 1, 10, 16, 10, 1, 15, 7, 16, 16, 11, 2, 9, 10, 6, 8, 6, 7, 1, 3, 14, 10, 6, 2, 16, 14, 1, 12, 10, 8, 8, 3, 12, 2, 5, 16, 2, 12, 9, 15, 14, 15, 2, 1, 1, 7, 11, 13, 1, 7, 12, 11, 3, 3, 12, 9, 10, 12, 5, 7, 8, 6, 14, 10, 3, 11, 2, 2, 15, 5, 1, 5, 4, 10, 12, 11, 12, 1, 6, 8, 10, 12, 9, 8, 4, 5, 3, 12, 13, 12, 11, 14, 11, 2, 4, 9, 6, 2, 11, 16, 6, 2, 12, 10, 7, 8, 6, 14, 14, 5, 14, 7, 4, 13, 13, 16, 10, 5, 14, 4, 4, 10, 16, 15, 11, 12, 10, 13, 9, 12, 2, 14, 1, 1, 16, 6, 1, 7, 5, 11, 7, 1, 4, 15, 12, 10, 14, 1, 9, 16, 5, 5, 13, 14, 3, 11, 16, 9, 15, 14, 1, 2, 5, 4, 15, 16, 9, 10, 14, 11, 9, 2, 14, 3, 15, 14, 1, 8, 4, 14, 4, 2, 6, 11, 3, 13, 4, 2, 3, 6, 13, 13, 16, 6, 5, 13, 14, 4, 6, 10, 2, 5, 5, 4, 2, 15, 16, 10, 3, 4, 11, 9, 11, 8, 11, 11, 4, 8, 7, 4, 6, 1, 16, 9, 1, 1, 7, 11, 8, 12, 3, 5, 3, 7, 5, 7, 6, 6, 1, 7, 13, 10, 6, 16, 11, 12, 8, 8, 9, 13, 4, 15, 8, 3, 5, 2, 9, 1, 15, 2, 2, 2, 15, 2, 13, 3, 2, 14, 4, 8, 16, 8, 6, 2, 2, 9, 2, 10, 2, 15, 6, 15, 15, 14, 7, 4, 9, 2, 15, 2, 11, 8, 8, 6, 15, 5, 13, 13, 9, 3, 2, 15, 6, 2, 7, 1, 7, 14, 6, 14, 9, 6, 6, 2, 10, 12, 4, 15, 2, 1, 4, 5, 4, 14, 7, 1, 13, 14, 3, 14, 7, 5, 10, 1, 11, 5, 6, 12, 15, 16, 9, 9, 4, 14, 9, 1, 9, 11, 3, 9, 8, 9, 9, 13, 10, 7, 13, 8, 5, 12, 15, 15, 6, 3, 16, 11, 8, 7, 4, 7, 4, 10, 11, 3, 4, 1, 10, 15, 4, 9, 14, 1, 4, 9, 1, 13, 6, 16, 16, 9, 4, 13, 13, 11, 12, 10, 13, 3, 14, 13, 2, 5, 15, 3, 5, 13, 2, 13, 3, 14, 10, 13, 3, 9, 16, 7, 11, 14, 15, 8, 12, 9, 3, 15, 8, 2, 5, 3, 7, 4, 9, 11, 16, 4, 8, 8, 11, 6, 16, 3, 14, 16, 15, 10, 5, 5, 4, 8, 5, 11, 9, 1, 16, 2, 9, 6, 1, 12, 15, 1, 13, 2, 5, 10, 11, 11, 3, 4, 2, 10, 8, 14, 4, 1, 11, 14, 6, 5, 12, 11, 8, 7, 2, 2, 9, 7, 2, 3, 6, 9, 16, 12, 10, 5, 15, 13, 4, 14, 1, 2, 2, 3, 3, 2, 16, 9, 12, 12, 1, 11, 8, 7, 16, 12, 9, 5, 5, 14, 7, 9, 12, 2, 5, 11, 7, 13, 2, 2, 12, 6, 14, 10, 8, 5, 8, 12, 10, 1, 5, 16, 10, 6, 16, 9, 16, 1, 4, 10, 11, 11, 10, 3, 6, 2, 10, 13, 14, 14, 11, 14, 5, 15, 9, 5, 4, 16, 5, 15, 10, 14, 11, 12, 10, 15, 1, 14, 13, 10, 15, 8, 12, 15, 1, 1, 5, 7, 6, 8, 16, 11, 5, 5, 8, 9, 5, 4, 12, 3, 1, 1, 2, 12, 5, 1, 9, 6, 13, 6, 3, 6, 9, 2, 5, 9, 9, 15, 16, 2, 11, 15, 13, 13, 9, 7, 10, 1, 11, 6, 11, 16, 3, 5, 16, 12, 14, 16, 13, 5, 14, 7, 11, 1, 1, 5, 6, 8, 12, 10, 9, 4, 9, 8, 12, 9, 14, 11, 4, 12, 8, 1, 2, 8, 10, 13, 5, 13, 11, 8, 1, 11, 14, 11, 14, 8, 8, 11, 4, 2, 3, 16, 7, 3, 12, 3, 8, 4, 5, 3, 11, 4, 3, 3, 10, 14, 9, 13, 13, 6, 9, 14, 14, 8, 4, 15, 3, 5, 6, 8, 13, 9, 6, 7, 5, 2, 16, 3, 7, 11, 10, 11, 8, 6, 16, 7, 14, 11, 7, 12, 9, 3, 1, 3, 5, 2, 7, 13, 10, 2, 15, 9, 8, 5, 15, 7, 10, 13, 12, 13, 11, 1, 11, 15, 3, 16, 3, 15, 12, 9, 3, 11, 7, 9, 12, 14, 2, 16, 3, 10, 2, 6, 3, 16, 9, 9, 4, 6, 11, 13, 3, 9, 7, 12, 12, 3, 9, 1, 15, 4, 5, 3, 14, 10, 13, 3, 12, 7, 8, 12, 12, 3, 13, 12, 3, 16, 5, 11, 16, 13, 14, 9, 1, 11, 10, 4, 12, 13, 16, 5, 16, 8, 4, 7, 1, 13, 7, 10, 13, 9, 9, 14, 9, 1, 2, 13, 12, 2, 15, 5, 10, 9, 5, 15, 3, 13, 9, 16, 16, 15, 14, 9, 7, 3, 7, 5, 14, 10, 15, 7, 7, 13, 12, 4, 16, 5, 8, 6, 3, 15, 15, 5, 6, 5, 15, 1, 14, 11, 15, 16, 15, 3, 16, 14, 14, 15, 10, 10, 6, 15, 7, 3, 1, 1, 7, 6, 2, 11, 14, 12, 7, 12, 12, 5, 2, 1, 15, 15, 2, 3, 14, 15, 1, 8, 5, 2, 1, 12, 14, 14, 14, 1, 1, 14, 6, 15, 6, 16, 3, 5, 7, 7, 7, 13, 16, 14, 6, 6, 5, 15, 4, 3, 8, 4, 7, 13, 9, 15, 10, 12, 4, 2, 7, 11, 2, 9, 11, 2, 9, 9, 6, 14, 13, 5, 10, 2, 14, 11, 3, 7, 5, 1, 16, 14, 1, 13, 11, 5, 5, 12, 11, 15, 4, 6, 3, 6, 10, 4, 4, 6, 9, 5, 13, 12, 13, 8, 3, 15, 11, 13, 9, 6, 7, 9, 8, 11, 7, 16, 12, 13, 13, 14, 3, 1, 14, 7, 10, 4, 11, 6, 2, 11, 1, 13, 11, 11, 8, 11, 11, 10, 14, 11, 1, 11, 14, 2, 11, 4, 2, 16, 7, 16, 12, 13, 11, 1, 13, 15, 9, 16, 11, 3, 15, 13, 7, 11, 16, 3, 16, 7, 15, 8, 14, 10, 13, 1, 7, 10, 7, 15, 16, 12, 14, 2, 8, 1, 4, 9, 13, 6, 6, 13, 2, 12, 12, 15, 13, 9, 8, 7, 6, 16, 3, 16, 12, 11]
    b = get_random_blue_number(blueball)
    print(b)
