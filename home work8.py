#task1
string = int(input())
i = string[::-1]
if string == i:
  print("Eto polindrom")
else:
  print("eto ne polindrom")


#task2
digit = input()
i = digit[::-1]
if digit == i:
  print("Eto polindrom")
else:
  print("eto ne polindrom")


#task3
line=input()
counter = 0
for i in line:
    if i.isdigit():
        counter+=1
if counter:
    print(counter,'- kolichestvo cifr')
counter = 0
for i in line:
    if i.isalpha():
        counter+=1
if counter:
    print(counter,'- kolichestvo bukv')
    print(len(line),'- kolichestvo simvolov')


#task4
word = input('slovo:')
symbol = input('simvol:')
count = 0
for i in word:
    if i == symbol:
        count +=1
print('simvol -',symbol,'vstrechaetsya',count,'raz(a)')






