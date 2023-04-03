
#Task1 - #Task2
# код находит как отдельные элементы так и элементы которые пишутся слитно - 'pine-apple'
tuple_fruits = 'pear', 'grape', 'apple', 'pine-apple', 'mango', 'limon', 'lime', 'apple' \
                    'watermelon', 'orange','apple','blue-berries'
print(tuple_fruits)
user = input('vvedite nazvaniye frukta:')
count = 0
for i in tuple_fruits:
    if user in i:
        count +=1

print(f'{user} встречается в кортеже - {count} раз(a)')




#TASK3 - не смог решить задачу с кортежом, но и со списком код некорректно работает
tuple_cars = ('BMW','Audi','Koenigsegg','Mclaren','Porshe','Lamborghini','BMW','Ford',
        'Maserati','BMW','Ford','Mercedes','Rolls-Royce','Tesla')
list_cars = list(tuple_cars)
print(list_cars)
user1 = input('Введите название производителя:')
user2 = input('Введите слово для замены')
for i in range(len(list_cars)):
    if i == user1:
        list_cars.insert(i,user2)
        print(f'Элементы под названием - {user1}, были заменены на {user2}')
        print(list_cars)
    else:
        print('ne naydeno')





#TASK4***
set_country = {'Nederland', 'Germany', 'France', 'Russia', 'Hungary','Turkey', 'Belgium', 'Italia', 'Spain'}
print(set_country)
while True:
    choice = int(input('Выберите операцию:'
                            '\n1. Добавить элемент'
                            '\n2. Удалить элемент'
                            '\n3. Найти элемент'
                            '\nВведите номер операции - \n'))

    if choice == 1:
        user = input('введите название страны:')
        set_country.add(user)
        print(f'{user} - добавлен(а) во вложение.')
        print(set_country)
    elif choice == 2:
        user = input('введите название страны:')
        set_country.discard(user)
        print(f'{user} - удален(а) из вложения.')
    elif choice == 3:
        user = input('введите название страны для поиска:')
        if user in set_country:
            print(f'{user} - находится во вложении')
        else:
            print(f'{user} - не найден(a) во вложении\n')
        continue





#TASK5***
set_city = {'Амстердам','Баку','Париж','Берлин','Будапешт','Москва'}
set_city2 = {'Москва','Баку','Стамбул','Париж','Анталия','Мюнхен'}
same = set_city.intersection(set_city2)# не выводит элементы из вложенного кортежа
print(same)
print(set_city.difference(set_city2))
print(set_city2.difference(set_city))
print(set_city.symmetric_difference(set_city2))





#TASK6***
dict_players = {
                'Леброн Джеймс':2.02, 'Стефен Карри':1.95, 'Майкл Джордан':1.98,
                'Дуэйн Уэйд':1.89,'Рассел Уэстбрук':1.99, 'Кайри Ирвинг':1.94,
                'Шакил О’Нил':2.08,'Кевин Дюрант':1.99, 'Коби Брайант':1.93,
                'Джеймс Харден':1.92
                }

def add_items():
    player = input('Введите имя и фамилию игрока:')
    dict_players[player] = [player]
    print(f'{player} был добавлен в словарь {dict_players[player]}')
def del_items():
    player = input('Введите имя и фамилию игрока для удаления:')
    if player in dict_players:
        del dict_players[player]
        print(f'{player} был удален из словаря')
    else:
        print(f'{player} - не найден с словаре!')
def find_items():
    player = input('Введите имя игрока для поиска')
    if player in dict_players:
        print(f'{player} был найден в словаре как {dict_players[player]}')
    else:
        print(f'{player} не был найден в словвре')
def change_items():
    player1 = input('Введите имя и фамилию старого игрока:')
    player2 = input('Введите имя и фамилию нового игрока:')
    if player1 in dict_players:
        dict_players[player2] = player2
        print(f'{player1} был заменен на {dict_players[player2]}')
    else:
        print(f'{player1} не был найден в слваре, давайте добавим:')
        add_items()
def print_dict():
    print(dict_players)
    # for key, value in dict_players.items():
    #     print(f'{key} - {value}')

def main():
    while True:
        choice = int(input('Выберите операцию:'
                       '\n1. Добавить элемент'
                       '\n2. Удалить элемент'
                       '\n3. Найти элемент'
                       '\n4. Заменить элемент'
                       '\n5. Вывести весь словарь'
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
            print('Bye')
            break
main()





#TASK7***
dict_users = {
    'Петрова Елена Сергеевна ':{
		'telephone': +994556987711,
		'email':'elena.petrova@inbox.ru',
		'должность':'Генеральный менеджер',
		'Номер кабинета':101
	},
	'Морозов Андрей Николаевич':{
		'telephone': +79045563696,
		'email':'morozov@gmail.com',
		'должность':'Менеджер по продажам',
		'Номер кабинета':106
	},
    'Щербакова Валерия Петровна':{
		'telephone': +79651238123,
		'email':'sherbakova@gmail.com',
		'должность':'Заместитель отдела кадров',
		'Номер кабинета':103
	},
    'Степанов Павел Андреевич':{
		'telephone': +71296348525,
		'email':'stepanov@gmail.com',
		'должность':'начальник системы безопасности',
		'Номер кабинета':104
	},
    'Белова Мария Николаевна':{
		'telephone': +75548219637,
		'email':'belova@gmail.com',
		'должность':'Тестировщик',
		'Номер кабинета':104
	}
}

def add_items():
    user = (input('введите ФИО:'),input('должность:'),int(input('telephone:')))
    dict_users[user] = [user]
    print(f'{user} добавлен в словарь {dict_users[user]}')
def del_items():
    user = input('Введите ФИО для удаления:')
    if user in dict_users:
        del dict_users[user]
        print(f'{user} - удален из словаря')
    else:
        print(f'{user} - не найден в словаре!')
def find_items():
    user = input('Введите ФИО поиска')
    if user in dict_users:
        print(f'{user} найден как: {dict_users[user]}')
    else:
        print(f'{user} не найден в словаре')
def change_items():
    user = input('Введите ФИО бывшего сотрудника:')
    user2 = input('Введите ФИО нового сотрудника:')
    if user in dict_users:
        dict_users[user2] = user2
        print(f'{user} - заменен на {dict_users[user2]}')
    else:
        print(f'{user} не найден в слoваре, давайте добавим:')
        add_items()
def print_dict():
    for key,value in dict_users.items():
        print(f'{key} - {value}')
def main():
    while True:
        choice = int(input('Выберите операцию:'
                       '\n1. Добавить сотрудника'
                       '\n2. Удалить сотрудника'
                       '\n3. Найти сотрудника'
                       '\n4. Заменить сотрудника'
                       '\n5. Вывести весь словарь'
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
            print('Bye')
            break
main()






#TASK8***
dict_books = {
	'Дэн Браун':{
			'Код Давинчи':{
				'жанр':'роман/детектив',
				'год':2003,
				'страниц':590
			},

			'Инферно':{
				'жанр':'роман/детектив',
				'год':2013,
				'страниц':620
			},

			'Цифровая крепость':{
				'жанр':'детектив/триллер',
				'год':1998,
				'страниц':570
			}},
	'Стивер Кинг':{
			'Темная башня':{
				'жанр':'фантастика/триллер',
				'год':2004,
				'страниц':705

			},
			'Бегущий человек':{
				'жанр':'триллер',
				'год':1982,
				'страниц':420
			},
			'Страна радости':{
				'жанр':'триллер/детектив',
				'год':2013,
				'страниц':450
			}},
	'Чак Палак':{
			'Бойцовский клуб':{
				'жанр':'триллер',
				'год':1996,
				'страниц':400
			}}}
print(dict_books)

def add_items():
    user = int(input('Введите название книги:'))
    dict_books[user] = [user]
    print(f'{user} добавлен в словарь {dict_books[user]}')
def del_items():
    user = input('Введите название книги для удаления:')
    if user in dict_books:
        del dict_books[user]
        print(f'{user} - удален из словаря')
    else:
        print(f'{user} - не найден с словаре!')
def find_items():
    user = input('Введите имя и фамилию автора для поиска')
    if user in dict_books:
        print(f'автор: {user}, книги: {dict_books[user]}')
    else:
        print(f'{user} не найден в словаре')
def change_items():
    user = input('Введите название старой книги:')
    user2 = input('Введите название новой книги:')
    if user in dict_books:
        dict_books[user2] = user2
        print(f'{user} - заменен на {dict_books[user2]}')
    else:
        print(f'{user} не найден в слoваре, давайте добавим:')
        add_items()
def print_dict():
    for key,value in dict_books.items():
            print(f'{key} - {value}')
def main():
    while True:
        choice = int(input('\nВыберите операцию:'
                       '\n1. Добавить книгу'
                       '\n2. Удалить книгу'
                       '\n3. Найти книгу'
                       '\n4. Заменить книгу'
                       '\n5. Вывести весь словарь-'
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
            print('Bye')
            break
main()