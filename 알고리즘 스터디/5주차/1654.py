a, b = map(int, input().split())
arr = []
for i in range(0, a):
    c = int(input())
    arr.append(c)


start = 1
end = max(arr)


while start <= end:
    total = 0
    mid = (start+end)//2

    for i in arr:
        total += i//mid

    if total >= b:
        start = mid+1
    else:
        end = mid-1

print(end)
