import sys

N = int(sys.stdin.readline().rstrip())
arr = list(map(int,sys.stdin.readline().split()))

arr.sort()

target = 1
# 배열 순차 탐색
for e in arr:
    # 타겟보다 배열 값이 큰 경우
    if target < e:
        # 탐색을 종료한다
        break
    # 타겟에 원소를 더한다
    target += e

# 답은 이전값 + 1
print(target)
