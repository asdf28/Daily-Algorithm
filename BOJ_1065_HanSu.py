N = int(input())
cnt = 0
dif = 0

for num in range(1, N+1):
    if num < 100:
        cnt += 1
    else:
        tmp = num
        tmp_1 = tmp % 10
        tmp //= 10
        tmp_2 = tmp % 10
        dif = tmp_1 - tmp_2
        while True:
            tmp_1 = tmp % 10
            tmp //= 10
            tmp_2 = tmp % 10
            if dif != tmp_1 - tmp_2:
                break
            if tmp // 10 == 0:
                cnt += 1
                break
print(cnt)