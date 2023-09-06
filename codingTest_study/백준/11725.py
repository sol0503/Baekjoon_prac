import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def dfs(m):
    for i in arr[m]:
        # print(i)
        # print(arr1)
        if arr1[i] == 0:
            arr1[i] = m
            dfs(i)


n = int(input())
arr1 = [0]*(n+1)


arr = [[]for _ in range(n+1)]

for i in range(n-1):
    lis = list(map(int, input().split()))
    arr[lis[0]].append(lis[1])
    arr[lis[1]].append(lis[0])

dfs(1)
for i in range(2, n+1):
    print(arr1[i])
# print(arr)
# print(arr1)
