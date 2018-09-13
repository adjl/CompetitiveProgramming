#!/usr/bin/env python3

def main():
    for _ in range(int(input())):
        input() # Throw away
        distances = list(map(int, input().split()))
        print((max(distances) - min(distances)) * 2)


if __name__ == '__main__':
    main()
