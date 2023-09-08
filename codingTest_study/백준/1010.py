import sys

input = sys.stdin.readline

n = int(input())

for i in range(n):
    a, b = map(int, input().split())

    if a == b:
        print(1)
    else:
        j = max(a, b)
        l = min(a, b)
        g = min(j-l, l)

        k = 1
        count = 0

        while count < g:
            k *= j
            j -= 1
            count += 1
        while g > 0:
            k /= g
            g -= 1

        print(int(k))
