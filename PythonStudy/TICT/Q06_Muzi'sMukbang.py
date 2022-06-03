import heapq


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    q = []

    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i))

    ate = 0
    current = 0
    previous = 0
    leftOver = len(food_times)

    while ate + (q[0][0] - previous) * leftOver <= k:
        current, i = heapq.heappop(q)

        ate += (current - previous) * leftOver
        leftOver -= 1
        previous = current

    result = sorted(q, key=lambda x:x[1])
    return result[(k - ate) % leftOver][1] + 1
    # while True:
    #     isNotDone = False
    #     for i in range(len(food_times)):
    #         if food_times[i] == 0:
    #             continue
    #         if k == 0:
    #             return i + 1
    #
    #         food_times[i] -= 1
    #         k -= 1
    #
    #         isNotDone = True
    #
    #     if isNotDone == False:
    #         return -1



if __name__ == "__main__":
    food_times = [3,1,2]
    k = 5


    print(solution(food_times, k))