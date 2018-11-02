for _ in range(int(input())):
    numbers = sorted([input() for _ in range(int(input()))])
    consistent = True
    for i in range(len(numbers) - 1):
        n = len(numbers[i])
        prefix = 0
        for j in range(n):
            if numbers[i][j] == numbers[i + 1][j]:
                prefix += 1
            else:
                break
        if prefix == n:
            consistent = False
            break
    print('YES' if consistent else 'NO')
