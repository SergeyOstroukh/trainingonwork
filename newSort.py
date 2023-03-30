def sorted(arr):
    if len(arr) <= 1:
        return arr
    else:
        firstItem = arr[0]
        smallItems = [i for i in arr if i < firstItem]
        biggerItems = [i for i in arr if i > firstItem]
        return sorted(smallItems) + [firstItem] + sorted(biggerItems)


array = [20,12,5,1,8,111,178,54,26]
print(sorted(array))