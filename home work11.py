#task1
from random import randint
list_1 = [randint(-100,100),randint(-100,100), randint(-100,100),randint(-100,100),randint(-100,100)]
list_2 = [randint(-100,100),randint(-100,100), randint(-100,100),randint(-100,100),randint(-100,100)]
print(f'nash 1-y spisok = {list_1}')
print(f'nash 2-y spisok = {list_2}')
list_3 = list_1 + list_2
print(f'nash 3-y spisok = {list_3}')
list_4 = [min(list_3), max(list_3)]
print('min.num i max.num',list_4)
list_4 = []
for i in list_1:
    for j in list_2:
        if i not in list_2:
            if j not in list_1:
                list_4.append(i)
print('unikalniye elem.: ',set(list_4))
x = set(list_3)
print('spisok bez povtorov',x)
list_5 = []
for i in list_1:
    for j in list_2:
        if i in list_2:
            if j in list_1:
                list_5.append(i)
print('spisok s povtorami',list_5)



