
#task1/task4***
def deleniye():
    try:
        num_1 = float(input('num1:'))
        num_2 = float(input('num2:'))
        result = (num_1 / num_2)
        print(f'{num_1}/{num_2} = {result}')
    except ZeroDivisionError as e:
        print('Нельзя делить на - 0\n',e)
    except ValueError as e:
        print('Нельзя использовать - type(str),\nДанные об ошибке:',e)
    except TypeError as e:
        print('Неверный тип данных\nДанные об ошибке:',e)

deleniye()

#task2***
from math import sqrt
def koren():
    try:
        num = int(input('vvedite chislo:'))
        result = sqrt(num)
        print(f'koren chisla {num} = {result}')
    except ValueError as e:
        print('Нельзя брать корень у отрицательного числа,\nДанные об ошибке:',e)

koren()

#task-3 ***
try:
    car = input('proizvoditel:')
    model = input('model:')
    year = int(input('year:'))
    list_el = [car,model,year]
    print(list_el)
    index = int(input('vvedite index:'))
    print(f'element pod indexom {index} = {list_el[index]}')
except IndexError as e:
    print('Выход за пределы индексации\n',e)
except ValueError as e:
    print('Не корректный ввод:\тДанные об ошибке:',e)


#task-5***
try:
    book = 'Бойцойский клуб'
    year = int(input('year:'))
    info = book,year
    print(info)
    index = int(input('index:'))
    print(f'element pod indexom {index} = {book[index]}')
except IndexError as e:
        print('Выход за пределы индексации\n',e)
except ValueError as e:
        print('Не корректный ввод:\тДанные об ошибке:',e)

#task-6***
try:
    car = 'BMW'
    print(int(car))
except ValueError as e:
    print('данные об ошибке:',e)


########################################################################################


#task-1
def print_num():
    try:
        list_el = [int(input('vvodite elementi:'))]
        list_el2 = []
        for i in range(len(list_el)):
            if i != 0:
                list_el2.append(i)
            elif i == 0:
                break
        print(list_el2)
        if 0 not in list_el:
            raise Exception('v spiske net - 0')
    except Exception as e:
        print(e)

print_num()


#task-2
def age():
    while True:
        try:
            user = int(input('age:'))
            if user <= 0:
                raise Exception('incorrect input!')
        except BaseException as e:
            print(e)
age()




#task-3
try:
    list_el = [1,2,3,4,5,6,7,'h',9]
    summ = 0
    for i in list_el:
        summ += i
    print(summ)
except TypeError as e:
    print('Svedeniya o oshibke -',e)



#task-4
def change():
    try:
        user = input('name:')
        print(int(user))
    except ValueError as e:
        print(e)

change()



#task-5
from math import sqrt
def koren():
    try:
        num = int(input('vvedite chislo:'))
        result = sqrt(num)
        print(f'koren chisla {num} = {result}')
        if result < 0:
            raise Exception('chislo otricacelnoye')
    except Exception as e:
            print('Данные об ошибке:', e)

koren()















