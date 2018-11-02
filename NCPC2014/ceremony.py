n = int(input())
h = sorted([int(i) for i in input().split()])
charges = 0
shortest, tallest = 0, n - 1
while n > 0:
    if h[tallest] >= n:
        tallest -= 1
        n -= 1
        charges += 1
    else:
        min_height = h[shortest]
        for i in range(shortest, tallest + 1):
            h[i] -= min_height
            if h[i] == 0:
                shortest += 1
                n -= 1
        charges += min_height
print(charges)
