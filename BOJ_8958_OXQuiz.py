N = int(input())
cnt = 0
tmp = 0
for i in range(N):
    arr = list(map(str, input()))
    for j in range(len(arr)):
        if arr[j] == 'O':
            tmp += 1
            cnt += tmp
        elif arr[j] == 'X':
            tmp = 0
    print(cnt)
    cnt = 0
    tmp = 0
