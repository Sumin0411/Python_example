def insertion_sort(arr):
    new_arr = [arr[0]]
    print(f"1번째 정렬된 리스트 = {new_arr}")
    for i in range(1, len(arr)):
        j = 0
        while j < i and new_arr[j] < arr[i]:
            j += 1
        new_arr.insert(j, arr[i])
        print(f"{i + 1}번째 정렬된 리스트 = {new_arr}")
    return new_arr

arr = [3, 1, 4, 5, 2]
print("최종 정렬된 리스트 = ", insertion_sort(arr))