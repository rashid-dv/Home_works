#task1
text=input('vvedite text:')
counter = 0
a = text.capitalize()
print(a)
for i in text:
    if i.isdigit():
        counter+=1
if counter:
    print('количество цифр:',counter)
symbol = '!'
count = 0
for i in text:
    if i == symbol:
        count +=1
print('символ -',symbol,'- встречается',count,'раз(a)')
import string
znaki_punk = string.punctuation
print('знаки пунктуации встречаются -',len([j for j in text if j in znaki_punk]),'раз(a)')


# не смог сделать 2-ое задание без split. были проблемы с выводом ответа, получилось так
#task2
operation = input('vvedite operaciyu:')
new_list = operation.split(' ')

if new_list[1] == '+':
    result = float(new_list[0]) + float(new_list[2])
    print(f'{new_list[0]} + {new_list[2]} = {result}')
elif new_list[1] == '-':
    result = float(new_list[0]) - float(new_list[2])
    print(f'{new_list[0]} - {new_list[2]} = {result}')
elif new_list[1] == '*':
    result = float(new_list[0]) * float(new_list[2])
    print(f'{new_list[0]} * {new_list[2]} = {result}')
elif new_list[1] == '/':
    result = float(new_list[0]) / float(new_list[2])
    print(f'{new_list[0]} / {new_list[2]} = {result}')




