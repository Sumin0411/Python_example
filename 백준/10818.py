N = int(input())
array = list(map(int, input().split()))
# print(min(array), max(array))
array.sort()
print(array[0], array[-1])