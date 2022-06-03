#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'solution' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER X
#  2. INTEGER_ARRAY arr
#  3. INTEGER_ARRAY indexes
#


def solution(X, arr, indexes):
    result = []
    X_index = []
    X_index.append(0)

    # Write your code here
    for i in range(len(arr)):
        if arr[i] == X:
            X_index.append(i+1)

    for num in indexes:
        if num > len(X_index):
            result.append(-1)
            continue
        result.append(X_index[num])
    print(result)




if __name__ == '__main__':
    X = 8
    arr = [0,0,0,8,8,0,0,0,8,0]
    indexes = [100,2]

    solution(8,arr,indexes)
