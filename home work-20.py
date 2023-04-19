##task-1
from pickle import dump,load
doc_file = r'C:\Users\FX505DT\Desktop\file.bin\file.doc'

list_el = ['BMW','Porcshe','Tesla']
with open(doc_file,"wb") as file:
    dump(list_el,file)

with open(doc_file,'rb') as file:
    temp = load(file)
    print(temp)
    search = input('vvedite slovo dlya poiska:')
    change = input('vvedite slovo dlya zameni:')
    def find(list_el,search,change):
        with open(doc_file,"rb") as file:
            x = load(file)
        for i in range(len(list_el)):
            if x[i] == search:
                x[i] = change
        with open(doc_file,"wb") as file:
            dump(x,file)
    find(list_el,search,change)

with open(doc_file,'rb') as file:
    print(load(file))



##task-2
from pickle import dump,load
doc_file = r'C:\Users\FX505DT\Desktop\my_bin.docx'

text = ('BMW','2022','Porcshe','2021','Tesla','2020')
with open(doc_file,"wb") as file:
    dump(text,file)

with open(doc_file,"rb") as file:
    r = load(file)
    print(r)

digits = [int(i) for i in text if i.isdigit()]
print(f'Количество чисел в тексте: {len(digits)}')

words = [str(i) for i in text if i.isalpha()]
print(f'Количество слов в тексте: {len(words)}')



##task-3
from pickle import dump,load
f = r'C:\Users\FX505DT\Desktop\file.bin\file.doc'

dict_el = {'BMW':'M5','Rolls-Royce':'Ghost','Porshe':'911'}
with open(f,"wb") as file:
    dump(dict_el,file)

with open(f,"rb") as file:
    r = load(file)
    def print_dict():
        for key, value in dict_el.items():
            print(f'{value}')

    print_dict()






#task-4
###---------------------------- все функции работают, но изменения не сохраняются после выхода из программы (не смог решить эту проблему)
from pickle import dump,load
f_place = r'C:\Users\FX505DT\Desktop\file.bin\file.doc'

dict_users = {
    'Петрова Елена Сергеевна ':{
		'telephone': '+994556987711',
		'email':'elena.petrova@inbox.ru',
		'должность':'Генеральный менеджер',
		'Номер кабинета':'101'
	},
	'Морозов Андрей Николаевич':{
		'telephone': '+79045563696',
		'email':'morozov@gmail.com',
		'должность':'Менеджер по продажам',
		'Номер кабинета':'106'
	},
    'Щербакова Валерия Петровна':{
		'telephone': '+79651238123',
		'email':'sherbakova@gmail.com',
		'должность':'Заместитель отдела кадров',
		'Номер кабинета':'103'
	},
    'Степанов Павел Андреевич':{
		'telephone': '+71296348525',
		'email':'stepanov@gmail.com',
		'должность':'начальник системы безопасности',
		'Номер кабинета':'104'
	},
    'Белова Мария Николаевна':{
		'telephone': '+75548219637',
		'email':'belova@gmail.com',
		'должность':'Тестировщик',
		'Номер кабинета':'104'
	}
}

def add_items():
    with open(f_place, "wb") as file:
        r = dump(dict_users, file)
    user = (input('введите ФИО:'),input('телефон:'),input('email:'),input('должность:'))
    dict_users[user] = [user]
    print(f'{user} добавлен в словарь')
    return r

def del_items():
    with open(f_place, "rb") as file:
        r = load(file)
        user = input('Введите ФИО для удаления:')
        if user in dict_users:
            dict_users.pop(user)
            print(f'{user} - удален из словаря')
        else:
            print(f'{user} - не найден в словаре!')
    with open(f_place, "wb") as file:
        dump(dict_users, file)
    return r

def find_items():
    with open(f_place, "rb") as file:
        load(file)
        user = input('Введите ФИО для поиска:')
        if user == dict_users:
            print(f'{user} найден как: {dict_users[user]}')
        else:
            print(f'{user} не найден в словаре')

def change_items():
    with open(f_place,"wb") as file:
        r = dump(dict_users, file)
    user = input('Введите ФИО бывшего сотрудника:')
    user2 = input('Введите ФИО нового сотрудника:')
    if user in dict_users:
        dict_users[user2] = user2
        print(f'{user} - заменен на {dict_users[user2]}')
    else:
        print(f'{user} не найден в слoваре, давайте добавим:')
    return r


def print_dict():

    with open(f_place,"rb") as file:
        load(file)
    for key,value in dict_users.items():
        print(f'{key} - {value}')


def exit():
    with open(f_place,"wb") as file:
        r = dump(dict_users, file)
    return r

def main():
    while True:
        choice = int(input('Выберите операцию:'
                           '\n1. Добавить сотрудника'
                           '\n2. Удалить сотрудника'
                           '\n3. Найти сотрудника'
                           '\n4. Заменить сотрудника'
                           '\n5. Вывести весь словарь'
                           '\n6. Выйти из программы'
                           '\nВведите номер операции - :'))
        if choice == 1:
            add_items()
        elif choice == 2:
            del_items()
        elif choice == 3:
            find_items()
        elif choice == 4:
            change_items()
        elif choice == 5:
            print_dict()
        else:
            print('Данные сохранены, Bye')
            break
main()


