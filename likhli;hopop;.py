# Numbers = [[1,2,3,4,5,6,7,8,9,10],
#           [11,12,13,14,15,16,17,18,19,20]]
#
# Result = []
# for list in Numbers:
#    Squares = [i ** 2 for i in list if i % 2 == 0]
#    Result.extend(Squares)
# print(Result)
import random

array = int(input('Введите размер массива: '))
num = int(input('Введите число которое хотим проверить: '))
newArr = [random.randint(1,30) for i in range(array)]
# for i in range(array):
#     newArr.append(random.randint(0,100))
curren_count = newArr[0]
for j in newArr:
    if j == 0:
        j += 1
    else:
        if abs(num - j) < abs(num - curren_count):
            curren_count = j
print(newArr)
print(f'ввели: {num}')
print(f'получили {curren_count}')

