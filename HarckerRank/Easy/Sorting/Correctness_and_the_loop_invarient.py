def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        value = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > value:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = value


m = int(input().strip())
ar = [int(i) for i in input().strip().split()]
insertion_sort(ar)
print(" ".join(map(str,ar)))
