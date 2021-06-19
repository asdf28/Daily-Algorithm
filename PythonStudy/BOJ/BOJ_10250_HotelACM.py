import sys

T = int(sys.stdin.readline().rstrip())

for i in range(T):
    H, W, N = map(int, sys.stdin.readline().rstrip().split())
    RoomNum = N // H

    if RoomNum * H == N:
        RoomNum += H * 100

    else:
        RoomNum += (N - (RoomNum * H)) * 100 + 1

    print(RoomNum)
