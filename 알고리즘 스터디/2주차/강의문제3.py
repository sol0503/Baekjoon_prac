import sys
n=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))
count=0
c=0
arr.sort()

for i in arr:
    c=i
    if arr[c-1]<=c:
        count+=1
        del(arr[:c])

print(count)  