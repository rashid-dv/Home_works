a = int(input('num1:'))
b = int(input('num2:'))
stepen1 = int(input('stepen1:'))
stepen2 = int(input('stepen2:'))

for i in range(a,b+1):
    for j in range(stepen1,stepen2+1):
        print(f'Number {i} in power {j} = {i**j}')



#task2
from random import randint
start = 0
end = 100
popitki = []
i = randint(start, end)
print('Число загадано!')
while True:
    a = int(input('Введи число:'))
    if a < i:
        print('Неверно. Загаданное число больше')
    elif a > i:
        print('Неверно. Загаданное число меньше')
    elif a == i:
        print('Вы отгадали число!')
        choice = int(input('Если хотите начать игру сначала, нажмите 1, если нет нажмите 0'))
        if choice == 1:
            i = randint(start,end)
            continue
        elif choice == 0:
            print("Конец игры")
            break