import sys




def insertion_sort(arr):
    length_of_array = len(arr)
    
    for i in range(1, length_of_array):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j-=1
        arr[j + 1] = key

    return arr
        

def insertion_sort_descending(arr):
    length_of_array = len(arr)
    
    for i in range(1, length_of_array):
        key = arr[i]
        j = i - 1
        while j >= 0 and key > arr[j]:
            arr[j + 1] = arr[j]
            j-=1
        arr[j + 1] = key

    return arr

    


test = [5, 3, 2, 6]
print(insertion_sort(test))
print(insertion_sort_descending(test))


