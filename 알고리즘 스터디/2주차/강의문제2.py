import sys
num=int(sys.stdin.readline())
count=0
a=num
b=num
arr=[]

while a>=10:
    a=a//10
    b=b%10
    arr.append(b)
    b=a

arr.reverse()


count+=a
for i in arr:
    if i==0 or i==1:
        count+=i
    else:
        count*=i

print(count)

