# Python program for Implementation of Insertion Sort

"""
Time Complexity: O(n^2)
Auxilary Spcae: O(1)
"""


def insetion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i-1

        while j>=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key

    print(arr)



if __name__ == "__main__":
    arr = [23,1,10,5,2]
    insetion_sort(arr)