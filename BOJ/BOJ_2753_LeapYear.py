year = int(input())
ans = 0

if year % 4 == 0:
    if year % 100 != 0:
        ans = 1
    elif year % 400 == 0:
        ans = 1

print(ans)

