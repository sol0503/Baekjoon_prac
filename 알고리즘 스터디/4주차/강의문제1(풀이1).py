a, b = map(int, input().split())
arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))

for i in range(1, a):
    for j in range(i, 0, -1):
        if arr_a[j] < arr_a[j-1]:
            arr_a[j], arr_a[j-1] = arr_a[j-1], arr_a[j]
        else:
            break

for i in range(1, a):
    for j in range(i, 0, -1):
        if arr_b[j] < arr_b[j-1]:
            arr_b[j], arr_b[j-1] = arr_b[j-1], arr_b[j]
        else:
            break


for i in range(0, b):
    arr_a[i], arr_b[a-1-i] = arr_b[a-1-i], arr_a[i]

count = 0
for i in arr_a:
    count += i

print(count)
#이걸로하면 arr_a[i]가 arr_b[a-1-i]보다 클경우에도 바꿔야하므로 옳지않다.