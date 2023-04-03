import sys
num=int(sys.stdin.readline())

a=int(num/5) #5가 최대한 많이 들어갈수있는 수
b=int(num/3) #3이 최대한 많이 들어갈수있는 수
c=int(num%3) #3으로 나눠지는지 판단
d=num  #num받아놓기

count=0
arr=[]
for i in range(1,a+1):
    arr.append(i)
if num%5==0:
    print(a)
else:
    for i in reversed (arr):
        num-=5*i
        if num%3==0:
            d=int(num/3)
            print(i+d)
            break
        else:
            num=d
    if num==d:
        if c==0:
          print(b)
        else:
            print(-1)