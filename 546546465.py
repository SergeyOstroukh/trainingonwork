# def deleteItems (arr1,arr2):
#     newArr =[]
#     for i in arr1:
#             if i in arr2:
#                 i+1
#             else:
#                 newArr.append(i)
#     return newArr
#
# array1 = [1,5,8,7,5,6,4]
# array2 = [2,3,3,5,4]
# print(deleteItems(array1,array2))


# возвести каждую в квадрат и сложить все в строку

def square_digits(number):
    numNum = str(number)
    resultStr = []
    resStr = ''
    for i in numNum:
        resultStr = int(i)*int(i)
        resStr += str(resultStr)

    return resStr


num = 2345
print(square_digits((num)))

# i2 = '|'.join(i.split())