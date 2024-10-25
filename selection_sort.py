# Python program for the implementation of Selection Sort.

"""
Time Complexity: O(n^2), as there are two nested loops.
Auxilary Space: O(1), as the only extra memory used is temporary variables.
"""

def selection_sort(arr):
    n = len(arr)

    for i in range(n-1):

        # Assume the current index holds the min position
        min_idx = i

        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:

                # Update the min_idx if a smaller item is found.
                min_idx = j

        # Move minimum element to its correct position
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    print(f"The sprted array is: {arr}")



if __name__ == "__main__":
    arr = [12,45,3,76,48,95,3,5,7,2,76]
    selection_sort(arr)
