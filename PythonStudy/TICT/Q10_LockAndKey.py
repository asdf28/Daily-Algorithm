import copy


def solution(key, lock):
    answer = True

    N = len(lock)
    M = len(key)

    max_x_lock = 0
    max_y_lock = 0
    min_x_lock = int(1e9)
    min_y_lock = int(1e9)
    for i in range(N):
        for j in range(N):
            if lock[i][j] == 0:
                max_x_lock = max(max_x_lock, i)
                max_y_lock = max(max_y_lock, j)
                min_x_lock = min(min_x_lock, i)
                min_y_lock = min(min_y_lock, j)
    # print(min_x_lock,max_x_lock,min_y_lock,max_y_lock)

    for rotate in range(4):
        # print("rotate")
        # print(key)
        for x in range(-N,N):
            if x > min_x_lock or x + M - 1 < max_x_lock:
                # print("x",x,min_x_lock,max_y_lock)
                continue
            for y in range(-N,N):
                if y > min_y_lock or y + M - 1 < max_y_lock:
                    # print("y",y,min_y_lock,max_y_lock)
                    continue
                answer = True
                # print(x,y)
                for i in range(M):
                    for j in range(M):
                        if x + i >= N or y + j >= N or x + i < 0 or y + j < 0:
                            # print(i, j, x, y, key[i][j])
                            # print("continue")
                            continue
                        # print(i, j, x+i, y+j, lock[x+i][y+j], key[i][j])
                        if lock[x+i][y+j] == key[i][j]:
                            answer = False
                            # print(answer)
                            break
                    if answer == False:
                        break
                if answer == True:
                    # print(True)
                    return True
        tmp = copy.deepcopy(key)
        for i in range(M):
            for j in range(M):
                key[j][M - i - 1] = tmp[i][j]
    return False
    # 열쇠 홈과 자물쇠 홈인 경우
        # 자물쇠가 다 안열렸을 것임. 안됨
    # 열쇠 돌기와 자물쇠 홈인 경우
        # 열려야함
    # 열쇠 홈과 자물쇠 돌기인 경우
        # 상관 없는듯
    # 열쇠 돌기와 자물쇠 돌기인 경우
        # 안됨

    return answer

key = [[0, 1, 0], [0, 1, 0], [0, 0, 1]]
lock = [[1, 1, 1,1], [0, 1, 1,1], [1, 1, 1,1],[1, 1, 1,1]]
# key = [[0,0,0], [0,1,0], [1,0,0]]
# lock = [[1,1,1], [1,1,0], [1,0,1]]
#
print(solution(key, lock))
# print(solution([[0, 0], [0, 0]], [[1, 0, 0], [1, 0, 0], [1, 1, 1]]))