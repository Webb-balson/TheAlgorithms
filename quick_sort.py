def partition(arr, low, high):

    p = arr[low]
    i = low + 1
    j = high

    while True:

        while i<=j and arr[i]<=p:
            i += 1

        while i<=j and arr[j]>=p:
            j -= 1

        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break

    arr[low], arr[j] = arr[j], arr[low]

    return j

def quick_sort(arr, low, high):

    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot-1)
        quick_sort(arr,pivot+1,high)


if __name__ == "__main__":
    arr = [4,3,1,2,5,9,7,10,6]
    low = 0
    high = len(arr)

    quick_sort(arr, low, high-1)
    print(f"The sorted array is: {arr}")
