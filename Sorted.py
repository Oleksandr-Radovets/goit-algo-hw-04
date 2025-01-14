import random
import timeit

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def generate_random_data(size):
    return [random.randint(0, 10000) for _ in range(size)]

def benchmark_sorting_algorithms():
    sizes = [100, 1000, 5000, 10000]
    algorithms = {
        "Insertion Sort": insertion_sort,
        "Merge Sort": merge_sort,
        "Timsort (sorted)": sorted
    }

    for size in sizes:
        print(f"\nArray size: {size}")
        data = generate_random_data(size)

        for name, func in algorithms.items():
            test_data = data.copy()
            time = timeit.timeit(lambda: func(test_data), number=1)
            print(f"{name}: {time:.5f} seconds")

if __name__ == "__main__":
    benchmark_sorting_algorithms()