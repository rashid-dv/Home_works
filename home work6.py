#task1
a = int(input())
b = int(input())
i = a+b
for i in range(a,b):
    if i%7==0:
        print(i)

#task2
a=int(input("Первое число: "))
b=int(input("Второе число: "))
i=a,b
start = a
stop = b
step = a
print("Все числа диапазона",list(range(start,stop,step)))
for i in range(a,b):
    if i%7==0:
        print("Все числа кратные 7:",i)
for i in reversed(range(a,b)):
    print(i)
for i in range(a,b):
   if i%5==0:
        print("Количество чисел, кратных 5:",i)

#task3
a=int(input('num1:'))
b=int(input('num2:'))
i = a,b
for i in range(a,b):
    if i%3==0:
        print('Fizz')
    elif i%5==0:
        print('Buzz')
    elif i%3==0 and i%5==0:
        print('Fizz Buzz')
    if i%3!=0 and i%5!=0:
        print(i)