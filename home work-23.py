
#task-1
from functools import singledispatchmethod
class Car:
    def __init__(self,manufacturer,model,year,engine,color,price):
        self.__manufacturer = manufacturer
        self.__model = model
        self.__year = year
        self.__engine = engine
        self.__color = color
        self.__price = price

    def print_info(self):
        return self.__manufacturer,self.__model,self.__year,\
            self.__engine,self.__color,self.__price

    # @singledispatchmethod
    def set_manufacture(self,value):
        self.__manufacturer = value

    def get_manufacture(self):
        return self.__manufacturer

    def set_model(self,value):
        self.__model = value

    def get_model(self):
        return self.__model

    def set_year(self,value):
        self.__year = value

    def get_year(self):
        return self.__year

    @singledispatchmethod
    def set_engine(self,value):
        self.__manufacturer = value

    @set_engine.register
    def _(self,value:int):
        if value >= 4:
            print(f'{value} - Нормально!)')
        else:
            print(f'{value} - Слабенько!')

    @set_engine.register
    def _(self, value: float):
        if value >= 4.0:
            print(f'{value} - Нормально!)')
        else:
            print(f'{value} - Слабенько!')

    @set_engine.register
    def _(self,value:bool):
        if value == True:
            print('Двигатель заведен')
        else:
            print('Двигатель выключен')

    def get_engine(self):
        return self.__engine

    def set_color(self,value):
        self.__manufacturer = value

    def get_color(self):
        return self.__color

    def set_price(self,value):
        self.__price = value

    def get_price(self):
        return self.__price

car = Car('BMW','M5(Competion)',2022,4.4,'Monte-Carlo','120.000$')
print(car.print_info())
car.set_engine(5)



#task-2
from pickle import dump, load
class Shape:

    def __init__(self,visota,shirina):
        self.visota = visota
        self.shirina = shirina
class Square(Shape):
    def _init_(self,visota,shirina):
        super().__init__(visota,shirina)
    def show_square(self):
        print(self.visota,self.shirina)
    def save_square(self):
        doc_file = r'C:\Users\FX505DT\Desktop\file.bin\file.doc'
        with open(doc_file, "wb") as file:
            dump(self.visota,file)
            dump(self.shirina,file)
    def load_square(self):
        doc_file = r'C:\Users\FX505DT\Desktop\file.bin\file.doc'
        with open(doc_file,'rb') as file:
            r = load(file)
            return r

class Rectangle(Shape):
    def __init__(self,visota,shirina):
        super().__init__(visota,shirina)
    def show_rectangle(self):
        print(self.visota,self.shirina)

    def save_rectangle(self):
        doc_file = r'C:\Users\FX505DT\Desktop\file.bin\file.doc'
        with open(doc_file, "wb") as file:
            dump(self.visota,file)
            dump(self.shirina,file)

    def load_rectangle(self):
        doc_file = r'C:\Users\FX505DT\Desktop\file.bin\file.doc'
        with open(doc_file,'rb') as file:
            r = load(file)
            return r

shape = Shape((10,10),(5,20))
square = Square(10,10)
rectangle = Rectangle(5,20)
square.show_square()
rectangle.show_rectangle()
square.save_square()
rectangle.save_rectangle()




#task-3
class Flat:
    def __init__(self,value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return self.value != other.value

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

    def __le__(self,other):
        return self.value <= other.value

    def __ge__(self,other):
        return self.value >= other.value

class First_flat(Flat):
    def ploshad(self,value):
        self.value = value

class Second_flat(Flat):
    def ploshad(self, value):
        self.value = value

first = Flat(100)
print(first.value)

second = Second_flat(150)
print(second.value)

print(first==second)
print(first!=second)
print(first<second)
print(first>second)
print(first<=second)
print(first>=second)



#task-4
class Passport:
    def __init__(self,name,surname,date_of_birth,adress):
        self.name = name
        self.surname = surname
        self.date_of_birth = date_of_birth
        self.adress = adress

    def print_info(self):
        return self.name,self.surname,self.date_of_birth,self.adress


class ForeignPassport(Passport):
    def __init__(self,name,surname,date_of_birth,adress,pass_code,visa):
        super().__init__(name,surname,date_of_birth,adress)
        self.pass_code = pass_code
        self.visa = visa

    def print_info(self):
        return self.name,self.surname,self.date_of_birth,self.pass_code,self.visa,self.adress


passport = Passport('Edward','Snowden','21.06.1983','Russia,Moscow')
print(passport.print_info())
foreignPassport = ForeignPassport('Edward','Snowden','21.06.1983','AM20050','Schengen','Russia,Moscow')
print(foreignPassport.print_info())



#task-5
class Employer:
    def print(self):
        print('This is Employer class.')

class President(Employer):
    def print(self):
        print('This is President class.')

class Manager(Employer):
    def print(self):
        print('This is Manager class.')

class Worker(Employer):
    def print(self):
        print('This is Worker class.')

employer = Employer()
employer.print()
president = President()
president.print()
manager = Manager()
manager.print()
worker = Worker()
worker.print()


