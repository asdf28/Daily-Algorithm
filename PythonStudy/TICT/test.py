n = 3

arr = [1,2,3]

for e in arr[:]:
    print(e)
    if e == 2:
        arr.pop(1)
print(arr)
