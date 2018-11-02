e, f, c = [int(i) for i in input().split()]
empty_bottles = e + f
bottles_drank = 0
while empty_bottles >= c:
    bottles_drank += empty_bottles // c
    empty_bottles = (empty_bottles // c) + (empty_bottles % c)
print(bottles_drank)
