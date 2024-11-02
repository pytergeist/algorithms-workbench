def insertion_sort(arr, n):
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr


if __name__ == '__main__':
    arr = [3, 0, 9, 4, 8, 3, 0, 2]
    n = len(arr)
    sorted_arr = insertion_sort(arr, n)
    print(sorted_arr)