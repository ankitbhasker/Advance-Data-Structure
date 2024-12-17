import random

def randomized_qs(arr):
    """Sorts an array using the randomized quick sort algorithm."""
    if len(arr) <= 1:
        return arr
    
    # Randomly select a pivot
    pivot_index = random.randint(0, len(arr) - 1)
    pivot_element = arr[pivot_index]
    
    # print("The pivot index is %s and pivot elements is %s" %( pivot_index, pivot))
    
    # Partitioning step
    less_than_pivot = [x for x in arr if x < pivot_element]
    equal_to_pivot = [x for x in arr if x == pivot_element]
    greater_than_pivot = [x for x in arr if x > pivot_element]

    # Recursively sort the partitions and concatenate
    return (randomized_qs(less_than_pivot) +  equal_to_pivot + randomized_qs(greater_than_pivot))

def main():
    # User input for the array
    input_array = input("Enter an array of integers separated by spaces: ")
    
    # Convert the input string to a list of integers
    arr = list(map(int, input_array.split()))
    
    print("Original array:", arr)
    sorted_arr = randomized_qs(arr)
    print("Sorted array:", sorted_arr)

if __name__ == "__main__":
    main()
