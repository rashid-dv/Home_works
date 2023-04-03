task1***
Аккаунт на github.com создан.


#task2***
print("“Don't compare yourself with anyone in this world… if you do so, you are insulting yourself.”"
      "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t   Bill Gates")


#task3***
def chetnoye_num(num_1,num_2):
    list_el = [i for i in range(num_1, num_2+1) if i %2 == 0]
    print(list_el)

chetnoye_num(int(input('num1:')),int(input('num2:')))


#task4***
def find_min(num1,num2,num3,num4,num5):
    min_num = num1
    if num2 < min_num:
        min_num = num2
    elif num3 < min_num:
        min_num = num3
    elif num4 < min_num:
        min_num = num4
    elif num5 < min_num:
        min_num = num5
    print(f'min.num iz 5-ti chisel - {min_num}')

find_min(int(input('num1:')),int(input('num2:')),int(input('num3:')),int(input('num4:')),int(input('num5:')))


#task5***
def nums_power(num1, num2):
    proizvedeniye = 1
    for i in range(num1,num2+1):
        proizvedeniye *= i
    return proizvedeniye

print(nums_power(int(input('vvedite nachalo diapazona:')),int(input('vvedite konec diapazona:'))))


#task6***
def kol_cifr(chislo):
    count = 0
    for i in range(len(chislo)):
        count+=1
    if count:
        print(f'kolichestvo cifr - {count}')

kol_cifr(input('vvedite chislo:'))


#task7***
while True:
    def polindrom(chislo):
        if chislo == chislo[::-1]:
            return True
        else:
            return False

    print(polindrom((input('vvedite chislo:'))))


#task8***
def sum_nums(num1,num2):
    summ = 0
    for i in range(num1,num2+1):
        summ += i
    print(f'Summa vsex chisel: {summ}')

sum_nums(int(input('nachalo diapazona:')),int(input('konec diapazona:')))
