
#task1
while True:

    id_nums = ['+90', '+1', '+994', '+7', '+42']
    nums = [24416339, 904004, 2563, 55745, 156904004]

    choice = int(input('\nВыберите операцию:'
                       '\n1. Отсортировать по идентификационным кодам;'
                       '\n2. Отсортировать по номерам телефона; '
                       '\n3. Вывести список пользователей с кодами и телефонами;'
                       '\n4. Выход.'
                       '\nВведите номер операции - :\n'))


    if choice == 1:
        def buble_sort(id_nums):
            for i in range(len(id_nums)):
                for j in range(len(id_nums)-i-1):
                    if id_nums[j] > id_nums[j+1]:
                        id_nums[j], id_nums[j+1] = id_nums[j+1], id_nums[j]
        buble_sort(id_nums)
        print(f'Номера отсортированы по кодам - {id_nums}')

    elif choice == 2:
        def buble_sort(nums):
            for i in range(len(nums)):
                for j in range(len(nums)-i-1):
                    if nums[j] > nums[j+1]:
                        nums[j], nums[j+1] = nums[j+1], nums[j]
        buble_sort(nums)
        print(f'Номера отсортированы - {nums}')

    elif choice == 3:
        for i in range(len(id_nums)):
            print(id_nums[i],nums[i])


    elif choice == 4:
        print('Вы вышли из программы')
        break
    else:
        print('Выберите операцию:')






# #task2
while True:
    name_of_books = ['Код Давинчи', 'Инферно', 'Цифровая крепость', 'Война миров', 'Темная башня',
                     'Бегущий человек', 'Страна радости', '451 градус по Фаренгейту', 'Бойцовский клуб']

    age_of_books = [2003, 2013, 1998, 1897, 2004, 1982, 2013, 1953, 1996]

    choice = int(input('\nВыберите операцию:'
                       '\n1. Отсортировать по названию книг'
                       '\n2. Отсортировать по годам выпуска'
                       '\n3. Вывести список книг с названиями и годами выпуска'
                       '\n4. Выход.'
                       '\nВведите номер операции - :\n'))

    if choice == 1:
        def buble_sort(name_of_books):
            for i in range(len(name_of_books)):
                for j in range(len(name_of_books)-i-1):
                    if name_of_books[j] > name_of_books[j+1]:
                        name_of_books[j], name_of_books[j+1] = name_of_books[j+1], name_of_books[j]
        buble_sort(name_of_books)
        print(f'Книги отсортированы по названию - {name_of_books}')

    elif choice == 2:
        def bubble_sort(age_of_books):
            length = len(age_of_books)
            for i in range(length):
                for j in range(length-i-1):
                    if age_of_books[j] > age_of_books[j+1]:
                        age_of_books[j], age_of_books[j+1] = age_of_books[j+1], age_of_books[j]

        bubble_sort(age_of_books)
        print(f'Книги отсортированы по годам - {age_of_books}')

    elif choice == 3:
        for i in range(len(name_of_books)):
            print(name_of_books[i],age_of_books[i])
    elif choice == 4:
        print('Вы вышли из программы')
        break




















# def bubble_sort(age_of_books):
#     length= len(age_of_books)
#     for i in range(length):
#         for j in range(length-i-1):
#             if age_of_books[j]>age_of_books[j+1]:
#                 age_of_books[j],age_of_books[j+1]=age_of_books[j+1],age_of_books[j]
# bubble_sort(age_of_books)
# print(age_of_books)









































