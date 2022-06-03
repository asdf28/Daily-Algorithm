#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solution' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY infectedHouses
#
from collections import deque

def factorial(n):
    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, (n + 1)):
        dp[i] = dp[i-1] * i % (int(1e9) + 7)

    return dp


def bfs(n, infectedHouses):
    dx = [1, -1]
    visited = [False] * (n + 1)
    days = [0] * (n + 1)

    q = deque()

    for house in infectedHouses:
        q.append((0, house))
        visited[house] = True

    while q:
        day, house = q.popleft()
        days[day] += 1

        for d in dx:
            next_house = house + d
            if next_house <= 0 or next_house > n:
                continue
            if visited[next_house] == True:
                continue
            q.append((day + 1, next_house))
            visited[next_house] = True

    return days


def solution(n, infectedHouses):
    # Write your code here
    days = bfs(n, infectedHouses)

    dp = factorial(n)

    result = 1

    for infected in days[1:]:
        if infected == 0:
            break
        result *= dp[infected]

    return result % (int(1e9) + 7)




if __name__ == '__main__':
    n = 6
    infectedHouses = [3, 5]

    print(solution(n, infectedHouses))
