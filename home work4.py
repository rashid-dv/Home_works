#task1
a = int(input("insert number:"))
if a == 1:
    print('Monday')
elif a == 2:
    print('Tuesday')
elif a == 3:
    print('Wednesday')
elif a == 4:
    print('Thursday')
elif a == 5:
    print('Friday')
elif a == 6:
    print('Saturday')
elif a == 7:
    print('Sunday')
else:
    print('incorrect number')


#task2
a = int(input("insert number:"))
if a == 1:
    print('January')
elif a == 2:
    print('February')
elif a == 3:
    print('March')
elif a == 4:
    print('Aprel')
elif a == 5:
    print('May')
elif a == 6:
    print('June')
elif a == 7:
    print('July')
elif a == 8:
    print('August')
elif a == 9:
    print('September')
elif a == 10:
    print('October')
elif a == 11:
    print('november')
elif a == 12:
    print('December')
else:
    print('incorrect number')

#task3
a = float(input("insert number:"))
if a>0:
    print('Number is positive')
elif a<0:
    print('Number is negative')
elif a==0:
    print('Number is equal to zero')
else:
    print('Incorrect number')

#task4
a = int(input("first number:"))
b = int(input("second number:"))
if a>b:
    print(b,a)
elif a<b:
    print(a,b)
elif a==b:
    print("Numbers are equal")
else:
    print('Incorrect number')