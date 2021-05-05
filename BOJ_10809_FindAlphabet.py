S = input()

res = list()

for i in range(26):
    res.append(-1)

for i in range(len(S)):
    if res[ord(S[i])-97] == -1:
        res[ord(S[i]) - 97] = i


for i in range(26):
    print(res[i])