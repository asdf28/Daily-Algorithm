import sys
from inspect import stack

if __name__ == "__main__":
    myEnqueue = []
    myDequeue = []

    n = int(sys.stdin.readline().rstrip())

    for x in range(n):
        query = list(map(int,sys.stdin.readline().split()))

        if query[0] == 1:
            myEnqueue.append(query[1])
            # print(myEnqueue, myDequeue)
        elif query[0] == 2:
            if len(myDequeue) == 0:
                while myEnqueue:
                    myDequeue.append(myEnqueue.pop())
            myDequeue.pop()

        elif query[0] == 3:
            if len(myDequeue) == 0:
                while myEnqueue:
                    myDequeue.append(myEnqueue.pop())
            front = myDequeue.pop()
            print(front)
            myDequeue.append(front)



