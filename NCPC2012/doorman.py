x, queue = int(input()), list(input())
party_goers, diff = 0, 0
while len(queue) >= 1 and abs(diff) <= x:
    if diff == x and queue[0] == 'M':
        if len(queue) > 1 and queue[1] == 'W':
            diff -= 1
            queue.pop(1)
        else:
            break
    elif diff == -x and queue[0] == 'W':
        if len(queue) > 1 and queue[1] == 'M':
            diff += 1
            queue.pop(1)
        else:
            break
    else:
        diff += 1 if queue[0] == 'M' else -1
        queue.pop(0)
    party_goers += 1
print(party_goers)
