import random

wather = int(input('Введите количество теплых дней: '))
newDay = []
for i in range(int(wather)):
    newDay.append(random.randint(-15,15))
print(newDay)
count = 0
count2 = 0
j = 0
while j < len(newDay):
    if newDay[j] < 0:
        count += 1
        j += 1
    elif newDay[j] > 0:
        count2 +=1
        j+=1
print(count,count2)

