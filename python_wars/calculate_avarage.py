"""
Write a function which calculates the average of the numbers in a given array.

Note: Empty arrays should return 0.
"""

def find_average(numbers):
    if len(numbers) == 0:
        return 0
    
    avg_val = sum(avg for avg in numbers) / len(numbers)

    return avg_val
    
print(find_average([1, 2, 3]))
