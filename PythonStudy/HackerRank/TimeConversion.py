#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    result = list(s)
    # Write your code here
    if result[0] == '1' and result[1] == '2':
        if result[8] == 'A':
            result[0] = '0'
            result[1] = '0'

    elif result[8] == 'P':
        hour = str(int(s[0:2]) + 12)
        result[0] = hour[0]
        result[1] = hour[1]

    s = ''.join(result)
    return s[0:8]

if __name__ == '__main__':
    s = input()

    result = timeConversion(s)
    print(result)


