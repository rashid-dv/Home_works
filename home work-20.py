##task-1
# from pickle import dump,load
# my_file = r"C:\Users\FX505DT\Desktop\file.bin\my_bin.doc"
# cars = [
#     ['BMW','M5',2022],
#     ['Porcshe','911',2021],
#     ['Tesla','Model-S',2022]
#     ]
# with open(my_file,"rb") as file:
#     for j in range(len(cars)):
#         info = load(file)
#         print(info)

# with open(my_file,"wb") as file:
#     def find_change(list,search,change):
#         with open(my_file, "wb") as file:
#             search = input('slovo dlya poiska:')
#             change = input('slovo dlya zameni:')
#             with open(my_file,"wb") as file:
#                 for i in range(len(list)):
#                     if i == search:
#                         del search
#                         dump(change,file)
#                     else:
#                         print('incorrect input')
#
#         with open(my_file, "rb") as file:
#             for j in range(len(cars)):
#                 info = load(file)
#                 print(info)
















# def find_change(list,search,change):
#     user = input('slovo dlya poiska:')
#     user2 = input('slovo dlya zameni:')
#     with open(my_file,"wb") as file:
#         for i in list:
#             dump(i,file)
#     with open(my_file,"rb") as file:
#         for j in range(len(list)):
#             info = load(file)


# with open(my_file,'rb') as file:
#     temp = load(file)
#     slovo_nayti = input()
#     slobo_zamenit = input()
#     for i in range(len(my_file)):
#         if temp[i]==slovo_nayti:
#             del temp[i]
#     with open(my_file,'wb') as file:
#         dump(temp,file)
#
# with open(my_file,'rb') as file:
#     print(load(file))





#
# from pickle import dump,load
# cars = ['Tesla','BMW','Porsche']
# with open(r"C:\Users\FX505DT\Desktop\file.bin\my_bin.doc", "wb") as file:
#     dump(cars,file)
#
#
# with open(r"C:\Users\FX505DT\Desktop\file.bin\my_bin.doc", "rb") as file:
#     cars = load(file)
#     print(cars)


























