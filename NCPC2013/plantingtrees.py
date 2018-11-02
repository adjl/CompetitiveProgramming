input()  # Throw away
seedlings = sorted([int(i) for i in input().split()], reverse=True)
print(max([i + s for i, s in enumerate(seedlings)]) + 2)
