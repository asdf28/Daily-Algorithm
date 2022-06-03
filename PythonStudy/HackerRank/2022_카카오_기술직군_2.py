from bisect import bisect_right


def solution(teamK, teamB):
    result = []
    # Write your code here
    teamK.sort()

    for score in teamB:
        result.append(bisect_right(teamK, score))

    return result


if __name__ == '__main__':
    teamK = [1,4,2,4]
    teamB = [3,5]

    solution(teamK, teamB)