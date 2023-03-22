import sys
first,last=map(int,(sys.stdin.readline().split()))
words={"0":"zero","1":"one","2":"two","3":"three","4":"four","5":"five","6":"six","7":"seven","8":"eight","9":"nine",}

arr=[]

for i in range(first,last+1):
    a=' '.join([words[j] for j in str(i)])
    arr.append([i,a])

arr.sort(key=lambda x:x[1])

for i in range(len(arr)):
    if i %10 ==0 and i != 0:
        print(sep="\n")

    print(arr[i][0],end=" ")