N = int(input())
arr = []
# for _ in range(N):
#     arr.append(int(input()))
# arr.sort()
# print(*arr, sep="\n")

for i in range(N - 1):
    for j in range(N - 1 - i):
        if arr[j + 1] < arr[j]:
            arr[j], arr[j+1] = arr[j+1], arr[j]


print(*arr, sep="\n")