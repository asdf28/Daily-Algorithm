def solution(N, stages):
    last = max(max(stages),N)
    yet = [0] * (last + 1)
    reach = [0] * (last + 2)
    failure = []
    answer = []

    for e in stages:
        yet[e] += 1

    for i in range(last, 0, -1):
        reach[i] = yet[i] + reach[i+1]

    for i in range(1, N+1):
        if reach[i] == 0:
            failure.append((i,0))
        else:
            failure.append((i, yet[i]/reach[i]))

    failure.sort(key=lambda x: (-x[1], x[0]))

    for e in failure:
        stage, rate = e
        answer.append(stage)

    print(answer)

stages = [1]

solution(2, stages)