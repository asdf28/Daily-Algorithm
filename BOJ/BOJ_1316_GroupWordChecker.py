N = int(input())
s = set()
cnt = 0

for i in range(N):
    li = input()
    s.clear()
    s.add(li[0])
    flg = False
    for j in range(1, len(li)):
        if li[j] != li[j-1]:
            if li[j] in s:
                flg = True
                break
            else:
                s.add(li[j])
    if flg is False:
        cnt += 1

print(cnt)
