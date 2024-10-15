#سكشن 5
def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i
        print(f" {i + 1}:")
        print(f"  {arr}:")

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
array = [64, 25, 12, 22, 11]
sorted_array = selection_sort(array)
print( sorted_array)
