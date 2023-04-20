import sys
a=int(sys.stdin.readline())
arr=[]
for i in range(a):
    b,c=map(str,input().split())
    b=int(b)
    arr.append((b,c))

arr=sorted(arr,key=lambda x:x[0])

for i in range(a):
    print(arr[i][0],arr[i][1])