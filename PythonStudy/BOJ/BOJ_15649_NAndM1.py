import sys


def solution(pick, ans, visited, min_val, max_val):
    if pick == 0:
        val = numbers[0]

        for i in range(len(ans)):
            if ans[i] == 0:
                val += numbers[i+1]
            elif ans[i] == 1:
                val -= numbers[i+1]
            elif ans[i] == 2:
                val *= numbers[i+1]
            else:
                if val < 0:
                    val *= -1
                    val //= numbers[i+1]
                    val *= -1
                else:
                    val //= numbers[i+1]
        min_val = min(val, min_val)
        max_val = max(val, max_val)
        return min_val, max_val

    for i in range(4):
        if visited[i] == 0:
            continue
        visited[i] -= 1
        ans.append(i)

        min_val, max_val = solution(pick-1, ans, visited, min_val, max_val)

        visited[i] += 1
        ans.pop()

    return min_val, max_val


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())

    numbers = list(map(int, sys.stdin.readline().split()))
    operators = list(map(int, sys.stdin.readline().split()))

    min_val, max_val = solution(N-1, [], operators, int(1e9), -int(1e9))
    print(max_val)
    print(min_val)
