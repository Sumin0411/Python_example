# #1
# arr = list(map(int, input().split()))
# #3 1 5 2 4 대입
# print(min(arr))
# print(max(arr))

#2
arr = map(int, input().split())

my_max = 0
for a in arr:
    if my_max < a:
        my_max = a

print(my_max)