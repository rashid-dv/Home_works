#task1
i = int(input())
j = int(input())

print("prostie chisla diapazona:")
for num in range(i,j+1):
    if num > 1:
        for i in range(2,num):
            if (num%i)==0:
                break
        else:
            print(num)


#task2
a = int(input('num1:'))
b = int(input('num2:'))
a+=0
b+=0
for i in range(a,b):
    for j in range(a,b):
        print(i,'*',j,'=',i*j)


# #task3
a = int(input('num1:'))
for i in range(1,10):
    print(a*i)
b = int(input('num2:'))
for i in range(1,10):
    print(b*i)











