import sys

N = int(sys.stdin.readline().rstrip())
Score = list(map(int, sys.stdin.readline().rstrip().split()))

BestScore = max(Score)
NewAverage = 0
for i in range(N):
    NewAverage += (Score[i]/BestScore) * 100

print(NewAverage/N)
