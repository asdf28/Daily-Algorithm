N = input()
ln = len(N)

arr = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in range(8):
    ln -= N.count(arr[i])

print(ln)
