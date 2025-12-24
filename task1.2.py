arrays = [
    [1, 2, 3],
    [4, 5, 6, 7],
    [10, 20]
]

for arr in arrays:
    total = sum(arr)
    average = total / len(arr)
    print("array:", arr)
    print("sum:", total)
    print("average:", average)
import math