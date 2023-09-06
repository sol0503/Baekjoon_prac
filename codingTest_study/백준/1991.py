import sys


def dfs_pr(i):
    print(i, end="")
    for k in arr:
        if k[0] == i:
            if k[1] != ".":
                dfs_pr(k[1])
            if k[2] != ".":
                dfs_pr(k[2])


def dfs_in(i):
    for k in arr:
        if k[0] == i:
            if k[1] != ".":
                dfs_in(k[1])
            print(i, end="")
            if k[2] != ".":
                dfs_in(k[2])


def dfs_post(i):
    for k in arr:
        if k[0] == i:
            if k[1] != ".":
                dfs_post(k[1])
            if k[2] != ".":
                dfs_post(k[2])
            print(i, end="")


input = sys.stdin.readline


n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(str, input().split())))

dfs_pr("A")
print()
dfs_in("A")
print()
dfs_post("A")
