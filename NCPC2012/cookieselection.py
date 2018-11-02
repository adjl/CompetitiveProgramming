import sys

from bisect import bisect


try:
    cookies = []
    num_cookies = 0
    while True:
        line = input()
        if line.isdigit():
            cookie = int(line)
            if cookies:
                i = bisect(cookies, cookie)
                cookies[i:i] = [cookie]
            else:
                cookies.append(cookie)
            num_cookies += 1
        else:
            i = 0
            if num_cookies % 2 == 0:
                i = num_cookies // 2
            else:
                i = (num_cookies + 1) // 2 - 1
            print(cookies[i])
            del cookies[i]
            num_cookies -= 1
except EOFError:
    sys.exit()
