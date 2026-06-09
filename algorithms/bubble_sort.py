def bubble_sort(arr):
    arr = arr[:]
    n = len(arr)
    steps = []

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            is_swap = arr[j] > arr[j + 1]
            if is_swap:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
            steps.append({
                "array": arr[:],
                "comparing": [j, j + 1],
                "swapped": is_swap
            })
        if not swapped:
            break

    return steps
