arr = [3, 1, 4, 5, 2]

def selection_sort(arr):
    n = len(arr) #리스트 길이 확인
    for i in range(n):  #리스트만큼 반복
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

        print(f'{i+1}번 째 정렬 후 = {arr}')
    return arr

print(selection_sort(arr))