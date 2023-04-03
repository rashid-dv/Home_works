#task1***
while True:
    a = input('vvedite chislo:')
    num = 0
    for i in range(len(a)):
        num += int(a[i]) * (2**(len(a) - i - 1))
        print(num)
    print('chislo v 10-oy SS;',num)



#task2***
a = float(input('введите количество метров:'))
print('Выберите операцию:',  'мили - 1,',  'дюймы - 2,',  'ярды - 3,')
b = float(input())
if b == 1:
    print(a * 0.000621371)
if b == 2:
    print(a * 39.3701)
if b == 3:
    print(a * 1.09361)



#task3***
a,b = int(input('num1:')), int(input('num2:'))
if a == b:
   print('chisla ravni:',a,'=',b)
else:
   print(min(a,b))
   print(max(a,b))



#task4***
dlina = int(input('vvedite dlinu:'))
symbol = input('vvedite simvol:')
for i in range(dlina):
    print(symbol)



#task5***
while True:
    a = int(input('vvedite chislo:'))
    if a > 0:
        print('Number is positive')
    elif a < 0:
        print('Number is negative')
    elif a == 0:
        print('Number is equal to zero')
    for i in range(a):
        if a == 7:
            print('Good bye!')
            exit()



#task6***
line = input('vvedite text')
count = 0
for i in range(1, len(line)):
    if line[i - 1] == line[i]:
        count += 1
print('количество одинаковых соседних символов:',count)



#task7***
list_1 = input('vvodite elementi podryad:')
new_list = list_1.split(' ')
list_1 = [int(x) for x in list_1]
count = sum(1 for i in range(1,len(list_1)) if list_1[i] == list_1[i-1])
print(f'Kolichestvo odinakovix sosednix elementov: {count}')



#task8***
a = int(input('vvedite chislo:'))
b = ''
while a > 0:
    b = str(a % 2) + b
    a = a // 2

print(b)



#task9***
list_el = input('vvodite elementi podryad:')
new_list = list_el.split(' ')
list_el = [int(x) for x in list_el]
count = sum(1 for i in range(1,len(list_el)) if list_el[i] == list_el[i-1])
print(f'Kolichestvo odinakovix sosednix elementov: {count}')



#task10 - ne smoq reshit etu zadachu
from random import randint
list_el = [randint(0,10) for i in range(10)]
count = 0
print(*list_el)
for i in range(0,len(list_el)-1):
    for j in range(i+1,len(list_el)-1):
        if list_el[i] == list_el[j]:
            count +=1
print(f'Индексы повторяющихся элементов:{list_el.index(list_el[j])}')



#task11***
# Пункт 1.6 - Не смог написать условие для нахождения суммы простых чисел.

from random import randint
m = int(input("vvedite kol.strok: "))
n = int(input("vvedite kol. stolbcov: "))
vloj_spisok = [[randint(-100, 100) for j in range(n)] for i in range(m)]
print(vloj_spisok)
summ = 0
for i in range(len(vloj_spisok)):
    for j in range(len(vloj_spisok[i])):
        summ += vloj_spisok[i][j]
print(f'Summa vsex chisel: {summ}')

summ = 0
for i in range(len(vloj_spisok)):
    for j in range(len(vloj_spisok[i])):
        if vloj_spisok[i][j]>0:
            summ += vloj_spisok[i][j]
print(f'Summa poloj. chisel: {summ}')

summ = 0
for i in range(len(vloj_spisok)):
    for j in range(len(vloj_spisok[i])):
        if vloj_spisok[i][j]<0:
            summ += vloj_spisok[i][j]
print(f'Summa otric. chisel: {summ}')

summ = 0
for i in range(len(vloj_spisok)):
    for j in range(len(vloj_spisok[i])):
        if vloj_spisok[i][j]%2==0:
            summ += vloj_spisok[i][j]
print(f'Summa chetnix. chisel: {summ}')

summ = 0
for i in range(len(vloj_spisok)):
    for j in range(len(vloj_spisok[i])):
        if vloj_spisok[i][j]%2!=0:
            summ += vloj_spisok[i][j]
print(f'Summa nechetnix. chisel: {summ}')



