#task1
a = int(input('chislo1:'))
b = int(input('chislo2:'))
c = int(input('chislo3:'))
s = print(('otvet='),(a + b + c)/3)
print('maximalnoe slaqaemoe=',c)
print(c>a and b<c)

#task2
a = int(input('zarplata='))
b = int(input('kredit='))
c = int(input('kommunalka='))
print('ostatok=',a-(b+c))

#task3
a=int(input('diaqonal1 ='))
h=int(input('diaqonal2 ='))
s = a*h/2
print('Ploshad romba =',s)

#task4
a=float(input('sdavshie ='))
b=float(input('doljniki ='))
print('percent sdavshix=',(a+b)*a/100)
print('percent doljnikov=',(a+b)*b/100)
print(a>b)