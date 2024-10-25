def binary(arr, low, high, target):
    while low <= high:

        mid = low+(high-low)//2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1




if __name__ == "__main__":
    arr = [2,3,10,14,40]
    x = 14

    result = binary(arr, 0, len(arr)-1, x)
    print(f"The Element is at index: {result}")