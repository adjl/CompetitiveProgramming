for _ in range(int(input())):
    r, e, c = [int(x) for x in input().split()]
    e -= c
    if e > r:
        print('advertise')
    elif e < r:
        print('do not advertise')
    else:
        print('does not matter')
