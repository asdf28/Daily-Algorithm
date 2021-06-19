a = set()

for i in range(1,10000):
    tmp = i
    ans = i
    while True:
        ans += tmp % 10
        tmp //= 10
        if tmp == 0:
            break

    if ans <= 10000:
        a.add(ans)

li = list(a)
for i in range(1,10000):
    if len(li) != 0 and i != li[0]:
        print(i)
    elif len(li) != 0:
        li.pop(0)
    else:
        break
