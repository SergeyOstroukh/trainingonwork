import random

arrLen = int(input('Введите размер массива: '))
array = [random.randint(1, 10) for i in range(arrLen)]
count = 0
for i in range(1, len(array)-1):
    if array[i] > array[i - 1] and array[i] > array[i + 1]:
        count += 1

print(array)
print(count)


