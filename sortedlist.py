arrList = [6,55,7,8,15,66,22,12,44,34,19]
def sorted(arr):
    if  len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        smallArr = [i for i in arr if i < pivot]
        biggerArr = [i for i in arr if i > pivot]
        return sorted(smallArr) + [pivot] + sorted(biggerArr)
print(sorted(arrList))

