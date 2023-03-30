import random

arr = int(input('Введите размер первого массива: '))
arrlen = [random.randint(1,10) for i in range(arr)]
arr2 = int(input('Введите размер второго массива: '))
arrlen2 = [random.randint(1,10) for i in range(arr2)]
newArr = []
for i in arrlen:
    if i in arrlen2:
        newArr.append(i)
print(arrlen)
print(arrlen2)
print(newArr)

