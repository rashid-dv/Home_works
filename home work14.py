#task1***
def nums_power(x,y):
    return x**y

print(nums_power(int(input('vvedite chislo:')),int(input('vvedite power:'))))

#Вариант с lambda:
print((lambda x,y: x**y)(int(input('vvedite chislo:')),
                         int(input('vvedite power:'))))



#task2***
def fibonacci(chislo):
    if chislo == 0:
        return 0
    elif chislo == 1:
        return 1
    else:
        return fibonacci(chislo-1)+fibonacci(chislo-2)

print(fibonacci(int(input('vvediye chislo:'))))





#task3***

def kvadrat(dlina, symbol, full):
   for i in range(dlina):
       for j in range(dlina):
           if full or i == 0 or j == 0 or i == dlina - 1 or j == dlina - 1:
               print(symbol, end=' ')
           else:
               print(' ', end=' ')
       print()

kvadrat(5, '*', True)
print('----------------')
kvadrat(5, '*', False)




#task4 -                   ne smoq reshit etu zadachu
from random import randint
while True:
    def find_num(game, player):
        game = randint(1, 100)
        print('game started!')
        player = int(input('vvedi chislo:'))
        if player < game:
            print('moe chislo bolshe')
        elif player > game:
            print('moe chislo menshe')
        else:
            print(f'ti pobedil')



# task5***
from random import randint
list_el = [[randint(1,10) for j in range(5)] for i in range(5)]
for i in range(5):
    for j in range(5):
        print(list_el[i][j], end=' ')
    print()
power = 1
for i in list_el:
    for j in i:
        power *= j

print(f'power vsex elementov: {power}')


#task6***
from random import randint
list_el = [[randint(1,10) for j in range(5)] for i in range(5)]
for i in range(5):
    for j in range(5):
        print(list_el[i][j], end=' ')
    print()
summ = 0
for i in list_el:
    for j in i:
        summ += j

print(f'summ vsex elementov: {summ}')










# def sum_nums(num1,num2):
#     summ = 0
#     for i in range(num1,num2+1):
#         summ += i
#     print(f'Summa vsex chisel: {summ}')
#
# sum_nums(int(input('nachalo diapazona:')),int(input('konec diapazona:')))














