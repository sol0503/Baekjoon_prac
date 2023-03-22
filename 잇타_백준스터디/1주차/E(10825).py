import sys
num = int(sys.stdin.readline())
arr=[]
for i in range(num):
    [name,kor,eng,math]=map(str,input().split())
    arr.append([name,int(kor),int(eng),int(math)])

arr=sorted(arr,key=lambda x :(-x[1],x[2],-x[3],x[0]))

for name in arr:
    print(name[0])