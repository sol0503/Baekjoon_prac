import sys
a=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))
arr_max=max(arr)
arr_min=min(arr)
print(arr_max*arr_min)