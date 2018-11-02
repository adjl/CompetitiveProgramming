for _ in range(int(input())):
    n = input()
    if n == 'P=NP':
        print('skipped')
        continue
    print(sum([int(k) for k in n.split('+')]))
