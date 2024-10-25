
def binary_recursive(arr, low, high, target):

    if high >= low:

        mid = low + (high-low)//2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binary_recursive(arr, low, mid-1, target)
        else:
            return binary_recursive(arr, mid+1, high, target)
        
    else:
        return -1
    
if __name__ == "__main__":
    arr = [2,3,4,10,40,45,55,65,68,70,75,78,82,85,89,93,94,97]
    x = 97

    result = binary_recursive(arr, 0, len(arr)-1, x)

    print(f"The result index is at: {result}")