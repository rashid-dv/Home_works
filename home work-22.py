#task-1
class BankAccount:
    def __init__(self,balance):
        self.__balance = balance

    def time(self,value):
        if value >= 365:
            return self.__balance * 1.5
        else:
            return self.__balance

    def deposit(self,value):
        return self.__balance + value

    def withdraw(self,value):
        return self.__balance - value

operation = BankAccount(2000)
print(operation.time(364))
print(operation.deposit(500))
print(operation.withdraw(700))



#task-2
class Employee:
    def __init__(self,salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

employee = Employee(1500)
print(employee.get_salary())



#task-3
class Student:
    def __init__(self,grade):
        self.__grade = grade

    def get_grade(self):
        return self.__grade

    def add_grade(self, value):
        self.__grade = value

student = Student(12)
print(student.get_grade())
student.add_grade(6)
print(student.get_grade())



#task-4
class Car:
    def __init__(self,brand,model,year):
        self.__brand = brand
        self.__model = model
        self.__year = year

    def get_car_info(self):
        print(self.__brand,self.__model,self.__year)

car = Car('Porsche','911',2021)
car.get_car_info()



#task-5
class Game:
    def __init__(self,score):
        self.__score = score

    def get_score(self):
        return self.__score

    def update_score(self,value):
        self.__score = value

game = Game(20)
print(game.get_score())
game.update_score(15)
print(game.get_score())


