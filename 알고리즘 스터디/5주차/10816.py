from bisect import bisect_left, bisect_right

a = int(input())
arr_a = list(map(int, input().split()))
b = int(input())
arr_b = list(map(int, input().split()))

arr_a.sort()


def count_by_range(arr, left_value, right_value):
    right_index = bisect_right(arr, right_value)
    left_index = bisect_left(arr, left_value)
    return right_index-left_index


arr_c = []
for i in arr_b:
    count = count_by_range(arr_a, i, i)
    arr_c.append(count)

for i in arr_c:
    print(i, end=" ")
