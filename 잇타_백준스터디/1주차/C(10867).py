import sys
num=int(sys.stdin.readline())

arr=map(int,(sys.stdin.readline().split()))
arr=list(set(arr))
arr.sort()

for i in arr:
    print(i,end=' ')
