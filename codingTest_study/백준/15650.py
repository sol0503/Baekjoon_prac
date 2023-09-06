# n, m = map(int, input().split())
# arr = []


# def print_lst():
#     for i in arr:
#         print(i, end=" ")
#     print()

# def choose(num):
#     if num == m + 1:
#         print_lst()

#     for i in range(1, n + 1):
#         if len(arr) >= 1 and arr[-1] >= i:
#             continue

#         arr.append(i)
#         choose(num + 1)
#         arr.pop()


# choose(1)

n,m = list(map(int,input().split()))
s = []
def dfs(start):
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(start,n+1):
        if i not in s:
            s.append(i)
            dfs(i+1)
            s.pop()
dfs(1)
