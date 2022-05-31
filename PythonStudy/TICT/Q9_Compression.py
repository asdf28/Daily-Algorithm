import sys


def solution(s):
    answer = []
    for unit in range(1, len(s)//2 + 1):
        compressed = []
        i = 0
        cnt = 1
        while True:
            if i + (2*unit) > len(s):
                if cnt != 1:
                    #compressed.append(cnt)
                    for k in map(int,str(cnt)):
                        compressed.append(k)
                for tmp in s[i:]:
                    compressed.append(tmp)
                break
            recurse = True
            for j in range(unit):
                if s[i + j] != s[i + j + unit]:
                    recurse = False
                    break
            if not recurse:
                if cnt != 1:
                    #compressed.append(cnt)
                    for k in map(int, str(cnt)):
                        compressed.append(k)
                for j in range(unit):
                    compressed.append(s[i+j])
                cnt = 1

            else:
                cnt += 1
            i += unit
        if len(answer) == 0 or len(answer) > len(compressed):
            answer = compressed

    print(answer)


arr = list(map(str, sys.stdin.readline().rstrip()))
solution(arr)