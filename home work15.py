
#zip***
print(list(zip('abcdef', [1,2,3,4,5,6])))


#map***
def my_map(function,list_el):
    new_list = []
    for item in list_el:
        new_list.append(function(item))
    return new_list

list_el = [1,2,3,4,5,6,7,8,9]
print(my_map(lambda element: element*2,list_el))



#filter***
list_1 = [1,2,3,4,5,6,7,8,9,10]
print(list(filter(lambda element: element > 5, list_1)))

def my_filter(function,list_el):
    high_points = []
    for element in list_el:
        if function(element):
            high_points.append(element)
    return high_points

list_el = [15,23,96,84,45,37,88,49,71,18]
high_points = my_filter(lambda element: element > 50,list_el)
print(sorted(high_points))




#reduce***---
from functools import reduce
print(reduce(lambda a,b: a**b, [5],5))

def my_reduce(function,list_el,initial = 0):
    for element in list_el:
        initial = function(initial,element)
    return initial

list_el = [1,2,3,4,5,6,7,8,9,10]
print(my_reduce(lambda element1,element2: element1+element2,list_el))


# Генераторы

#Map
list_el = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
result = [element * 2 for initial in list_el for element in initial]
print(result)


#Filter
list_el = [[1,2,3,4,5],[6,7,8,9,10]]
result = [element for element in list_el if element[0] <= 5]
print(result)