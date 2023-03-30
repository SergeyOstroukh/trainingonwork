import random


def solution(number):
    summ = 0
    if number < 0:
        return 0
    newList = []
    for i in range(number):
        newList.append(i)
        if i % 5 == 0 or i % 3 == 0 and i < number:
            summ += i
    return summ


num = 10
num1= int(num)
print(solution(num1))
