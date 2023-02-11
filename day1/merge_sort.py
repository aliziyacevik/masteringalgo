import sys

def merge(arr, start, middle, end):
    n = middle - start + 1
    m = end - middle

    left  = [0 for _ in range(n)]
    right = [0 for _ in range(m)]

    i, j = 0, 0
    while i < n:
        left[i] = arr[start + i]
        i += 1
    while j < m:
        right[j] = arr[middle + j + 1]
        j += 1 
    
    

    i, j = 0, 0
    k = start
    while i < n and j < m:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < n:
        arr[k] = left[i]
        i += 1
        k += 1
        
    while j < m:
        arr[k] = right[j]
        j += 1
        k += 1

def merge_sort(arr, start, end):
    if start < end:
        middle = (end + start) // 2
        merge_sort(arr, start, middle)
        merge_sort(arr, middle + 1, end)
        merge(arr, start, middle, end)

arr = [4, 1, 3, 2]
merge_sort(arr, 0, 3)
print(arr)


