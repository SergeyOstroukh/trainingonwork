
import random
monets = int(input('Введите количество монет: '))
# newArr = list()
newArr = []
for i in range(int(monets)):
    newArr.append(random.randint(0, 1))
countEagle = 0
countReshka = 0
j=0
while j < len(newArr):
    if newArr[j] == 0:
        countEagle += 1
        j+=1
    else:
        countReshka += 1
        j+=1
print(newArr)
if countEagle <= countReshka:
    print(f'Необходимо перевернуть {countEagle} монет')
else:
    print(f'Необходимо перевернуть {countReshka} монет')

