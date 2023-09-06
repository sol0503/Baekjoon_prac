n,k=map(int,input().split())
arr=[]
for i in range(n):
    a=int(input())
    arr.append(a)

arr.sort(reverse=True)
count=0
for i in arr:
    if k==0:
        break
    if i>k:
        continue
    else:
        c=k//i
        count+=c
        k-=i*c


print(count)