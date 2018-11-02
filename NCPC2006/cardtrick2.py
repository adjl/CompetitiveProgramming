from collections import deque


for _ in range(int(input())):
    n = int(input())
    d = deque([n])
    for i in range(n - 1, 0, -1):
        d.appendleft(i)
        d.rotate(i)
    print(*[i for i in d])
