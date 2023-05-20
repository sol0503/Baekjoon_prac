a = int(input())
arr = list(map(int, input().split()))

arr.sort()
sum = 0
arr1 = []
for i in arr:
    sum += i
    arr1.append(sum)

count = 0
for i in arr1:
    count += i
print(count)
