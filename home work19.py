
#task1***
with open("C:/Users/FX505DT/Desktop/my_first_file/my_file.txt","r") as file:
    x = file.read()
    print(f"Содержимое файла: {x}")
with open ("C:/Users/FX505DT/Desktop/my_first_file/my_file.txt","wt") as file:
    y = x.replace("world","IT")
    file.write(y)
print(f"Содержимое файла c изменениями: {x}")

#task2***
with open("C:/Users/FX505DT/Desktop/info/file_info","r") as file:
    print(file.read())

def find_str(text):
    text = text.title()
    count = 0
    for i in text:
        if i.isupper():
            count += 1
    return count

with open("C:/Users/FX505DT/Desktop/info/file_info","r") as file:
    text = file.read()
    print(find_str(text))


#task3***
with open("C:/Users/FX505DT/Desktop/my_first_file/my_file.txt","r") as file:
    stroka = file.read()
print(stroka[::-1])

def foo():






#task4 - ne smoq reshit




