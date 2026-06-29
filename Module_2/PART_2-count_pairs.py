"""
Comparing algorithms for counting pairs whose sums equal a target
Algorithms:
    1. count_pairs_slow()
    2. count_pairs_fast()
The script benchmarks both implemantation using different input sizes
"""

import time
def count_pairs_slow(data:list[int], target:int) -> int:
    """
    Count the number of unique pairs whose sum equals the target.

    Time Complexity:
        O(n²)
    """
    count = 0
    for i in range(len(data)):
        for j in range(i):
            if data[i] + data[j] == target:
                count += 1
    return count

def count_pairs_fast(data, target):
    """
    Count the number of unique pairs whose sum equals the target
    using a set.

    Time Complexity:
        O(n)
    """
    count = 0
    seen = set() #numbers encourted so far
    for num in data:
        addend = target - num
        if addend in seen:
            count += 1
        seen.add(num)
    return count



def benchmark(func, data,target)->float:
    """
    Measure how long an algorithm takes to execute.

    Args:
        func: Function to benchmark.
        data: List of integers.
        target: Desired sum.

    Returns:
        Execution time in seconds.
    """
    start = time.time()
    result = func(data, target)
    end = time.time()
    return end - start


def main():
    """Run benchmarks for different input sizes."""

    TARGET = 100
    sizes = [1000, 5000, 10000, 20000]

    print("-" * 65)
    print(f"{'Size':>8} | {'Nested':>15} | {'Set':>15}")
    print("-" * 65)

    for size in sizes:
        data = list(range(size))

        slow_time = benchmark(count_pairs_slow, data, TARGET)
        fast_time = benchmark(count_pairs_fast, data, TARGET)

        print(
            f"{size:>8} | "
            f"{slow_time:>15.6f}s | "
            f"{fast_time:>15.6f}s"
        )


if __name__ == "__main__":
    main()