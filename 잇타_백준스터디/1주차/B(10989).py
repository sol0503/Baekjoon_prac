# import sys
# num=int(sys.stdin.readline())
# arr=[0]*1001

# for i in range(0,num):
#     k=int(sys.stdin.readline())
#     arr[i]=k

# for j in range(0,num):
#   if arr[j]!=0:
#     for _ in range(arr[j]):
#       print(j)
#   # print(min(arr))
#   # arr.remove(min(arr))
  
import sys
n = int(sys.stdin.readline())
num_lst = [0]*10001

for i in range(n) :
    num = int(sys.stdin.readline())
    num_lst[num] += 1

for i in range(10001) :
    if num_lst[i] != 0 :
        for j in range(num_lst[i]) :
            print(i)