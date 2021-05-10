word = input()
li = list()

for i in range(58):
    li.append(0)

for i in range(len(word)):
    if ord(word[i]) >= 97:
        li[ord(word[i]) - 97] += 1
    else:
        li[ord(word[i]) - 65] += 1

if li.count(max(li)) > 1:
    print("?")
else:
    print(chr(li.index(max(li))+65))