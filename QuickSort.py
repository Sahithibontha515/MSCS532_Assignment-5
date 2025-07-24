import random
import time
import tracemalloc

import sys
sys.setrecursionlimit(20000)

''' Function that uses deterministic quick sort '''
def sort_elements_using_quicksort(elements):
    if len(elements) <= 1:
        return elements
    
   
    pivot = elements[0]

    less_pivot_elements = []
    greater_pivot_elements = []
    equal_pivot_elements = []

    # group the elements based on the pivot elements
    for num in elements:
        if num < pivot:
            less_pivot_elements.append(num)
        elif num > pivot:
            greater_pivot_elements.append(num)
        else:
            equal_pivot_elements.append(num)
    
    # recursively sort the elements
    return sort_elements_using_quicksort(less_pivot_elements) + equal_pivot_elements + sort_elements_using_quicksort(greater_pivot_elements)


def sort_elements_using_randomized_quicksort(elements):
    if len(elements) <= 1:
        return elements
    
    pivot = elements[random.randint(0, len(elements) - 1)]

    less_pivot_elements = []
    greater_pivot_elements = []
    equal_pivot_elements = []

    # group the elements based on the pivot elements
    for num in elements:
        if num < pivot:
            less_pivot_elements.append(num)
        elif num > pivot:
            greater_pivot_elements.append(num)
        else:
            equal_pivot_elements.append(num)
    
    # recursively sort the elements
    return sort_elements_using_randomized_quicksort(less_pivot_elements) + equal_pivot_elements + sort_elements_using_randomized_quicksort(greater_pivot_elements)



def evaluate_sort(name,arr, sort_fn):
    tracemalloc.start()
    start_time = time.perf_counter()
    
   
    sorted_result = sort_fn(arr)

    end_time = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return {
        "is_sorted": sorted_result == sorted(arr),
        "time_taken": end_time - start_time,
        "memory_used": peak
    }

def run_comparison(algorithm_name, sort_function, datasets):
    print(f"\n--- {algorithm_name} ---")
    for name, data in datasets.items():
        result = evaluate_sort(algorithm_name, data.copy(), sort_function)
        print(f"{name}")
        print(f"  Sorted Correctly : {result['is_sorted']}")
        print(f"  Time Taken       : {result['time_taken']:.6f} seconds")

# Main execution
if __name__ == "__main__":
    dataset_size = 10000  # Adjust this value for larger tests
    print("Data Set Size:", dataset_size)

    datasets = {
        "sorted_dataset": list(range(dataset_size)),
        "reverse_dataset": list(range(dataset_size - 1, -1, -1)),
        "random_dataset": random.sample(range(1, dataset_size * 2), dataset_size),
        "repeated_dataset": [random.choice([1, 2, 3, 4, 5]) for _ in range(dataset_size)]
    }

    run_comparison("Deterministic Quicksort", sort_elements_using_quicksort, datasets)
    run_comparison("Randomized Quicksort", sort_elements_using_randomized_quicksort, datasets)


