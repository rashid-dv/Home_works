
#task3***
from random import randint
list_1 = [randint(-100,100),randint(-100,100), randint(-100,100),randint(-100,100),randint(-100,100)]
list_1.sort()
print(f'nash spisok = {list_1}')
list_2 = [i for i in list_1 if i<0]
print('otricacelniye:',list_2)
list_2 = [i for i in list_1 if i>0]
print('polojitelniye:',list_2)
list_3 = [min(list_1), max(list_1)]
print('min.num i max.num',list_3)
count = str(list_1).count('0')
print(count)


#task4***
list_1 = input('vvedite elementi:')
symbol = input('chislo:')
count = 0
for i in list_1:
    if i == symbol:
        count +=1
print('chislo -',symbol,'vstrechaetsya',count,'raz(a)')


#task5***
list_elements = [int(input('num1:')), int(input('num2:')), int(input('num3:')), int(input('num4:')), int(input('num5:'))]
print(list_elements)
summ=0
summ_elem = sum(list_elements)
print(f'{summ_elem} - summa elementov')
list_elements = summ_elem/len(list_elements)
print('sredne.arif.:',list_elements)


#task6***
spisok = [int(input('num1:')), int(input('num2:')), int(input('num3:')), int(input('num4:')), int(input('num5:'))]
proiz_elem = 1
for i in spisok:
    if i % 3 == 0:
        proiz_elem *= i
print('proizvedeniye elem.',proiz_elem)


#task7***
from random import randint
list_1 = [randint(-100,100),randint(-100,100), randint(-100,100),randint(-100,100),randint(-100,100)]
list_1.sort()
print(f'nash spisok = {list_1}')
list_2 = [min(list_1), max(list_1)]
print('min.num i max.num',list_2)
power = 1
for i in list_1:
    if i > min(list_1) and i < max(list_1):
        power *= i
print(power)


#task8***
from random import randint
list_el = [randint(-100,100),randint(-100,100), randint(-100,100),randint(-100,100),randint(-100,100)]
print(list_el)
summ = 0
for i in range(0,len(list_el)):
    if list_el[i]>0:
        summ+=list_el[i]
        print(f'{summ} - summa poloj')

