for _ in range(int(input())):
    input()  # Throw away
    x = [int(i) for i in input().split()]
    print((max(x) - min(x)) * 2)
