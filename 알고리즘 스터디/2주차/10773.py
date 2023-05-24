num = int(input())
arr = []
for i in range(0, num):
    a = int(input())
    if a == 0:
        arr.pop()
    else:
        arr.append(a)

print(sum(arr))
