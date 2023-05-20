n = input()
arr_n = set(map(int, input().split()))
m = input()
arr_m = list(map(int, input().split()))

for i in arr_m:
    if i in arr_n:
        print(1)
    else:
        print(0)
