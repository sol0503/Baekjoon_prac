import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))
maxArr = [0]*n


# for i in range(0, n):
#     k = arr[i]
#     l = 0
#     for j in range(i, n):
#         m = arr[i]
#         l += arr[j]
#         k = max(l, k, m)
#     maxArr.append(k)
# print(max(maxArr))

maxArr[0] = arr[0]
for i in range(1, n):
    maxArr[i] = (max(arr[i]+maxArr[i-1], arr[i]))

print(max(maxArr))
# print(maxArr)
