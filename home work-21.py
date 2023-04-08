#task-1
class City:
    def __init__(self,country,city_name, region, people, postcode, phone_code):
        self.country = country
        self.city_name = city_name
        self.region = region
        self.people = people
        self.postcode = postcode
        self.phone_code = phone_code
        self.list_el = [self.country,self.city_name,self.region,self.people,self.postcode,self.phone_code]

    def print_el(self):
        print(self.list_el)


city = City('Baku','Azerbaycan','Absheron',2.2,'AZ1000',+994)
city.print_el()



#task-2
class Drob:
    def __init__(self,chislitel,znamenatel):
        self.chislitel = chislitel
        self.znamenatel = znamenatel
        self.list_el = [chislitel,znamenatel]
    def print_el(self):
        print(self.list_el)
    def slojeniye(self):
        result = self.chislitel + self.znamenatel
        print(f'Сумма сложения: {result}')
    def vichitaniye(self):
        result = self.chislitel - self.znamenatel
        print(f'Сумма вычитания: {result}')
    def umnojeniye(self):
        result = self.chislitel * self.znamenatel
        print(f'Сумма умножения: {result}')

    def deleniye(self):
        result =  self.chislitel / self.znamenatel
        print(f'Сумма деления: {result}')


drob = Drob(chislitel = float(input('vvedite chislitel:')),
            znamenatel = float(input('vvedite znaminatel:')))
drob.print_el()
drob.slojeniye()
drob.vichitaniye()
drob.umnojeniye()
drob.deleniye()


#task-3
class Nums:
    def __init__(self,num1,num2,num3,num4):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
        self.num4 = num4
        self.list_el = [num1,num2,num3,num4]

    def find_max(self):
        max_num = max(self.list_el)
        print(f'max num iz 4-x chisel = {max_num}')

    def find_min(self):
        min_num = min(self.list_el)
        print(f'min num iz 4-x chisel = {min_num}')
    def sred_arif(self):
        summ = self.num1 + self.num2 + self.num3 + self.num4
        sred_arif = summ / len(self.list_el)
        print(f'sred.arif. 4-x chisel = {sred_arif}')

nums = Nums(num1 = float(input('num1:')),num2 = float(input('num2:')),
            num3 = float(input('num3:')),num4 = float(input('num4:')))

nums.find_max()
nums.find_min()
nums.sred_arif()


#task-4
class Geo_figure:
    def operation(self):
        while True:
            choice = int(input('\nВыберите операцию:'
                               '\n1. Вычислить площадь треугольника'
                               '\n2. Вычислить площадь прямоугольника'
                               '\n3. Вычислить площадь квадрата'
                               '\nВведите номер операции - :'))
            if choice == 1:
                print(self.find_treuqolnik())
            elif choice == 2:
                print(self.find_pramouqolnik())
            elif choice == 3:
                print(self.find_kvadrat())
            else:
                print('Bye')
                break

    def find_treuqolnik(self):
        from math import sqrt
        a = float(input("Введите сторону a:"))
        b = float(input('Введите сторону b:'))
        c = float(input('Введите сторонуc c:'))
        p = (a + b + c) / 2
        s = sqrt(p * (p - a) * (p - b) * (p - c))
        print(f'Площадь треугольника: {s}')

    def find_pramouqolnik(self):
        a = float(input('Введите длину:'))
        b = float(input('Введите ширину b:'))
        s = a * b
        print(f'Площадь прямоугольника: {s}')

    def find_kvadrat(self):
        a = float(input('Введите длину строны:'))
        s = a * 4
        print(f'Площадь квадрата: {s}')

geo_figure = Geo_figure()
geo_figure.operation()




