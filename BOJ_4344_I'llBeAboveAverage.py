C = int(input())
cnt = 0
for i in range(C):
    arr = list(map(int, input().split()))
    NumberOfStudent = arr.pop(0)
    avg = sum(arr) / NumberOfStudent
    for j in range(NumberOfStudent):
        if arr[j] > avg:
            cnt += 1

    print("%.3f" % (cnt / NumberOfStudent * 100) + "%")

    arr.clear()
    avg = 0
    cnt = 0
