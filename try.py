
#
# import tkinter as tk
# from collections import namedtuple
#
# User = namedtuple("User", ["username", "password", "user_type"])
#
# class UserForm(tk.Toplevel):
#     def __init__(self, parent, user_type):
#         super().__init__(parent)
#         self.username = tk.StringVar()
#         self.password = tk.StringVar()
#         self.user_type = user_type
#
#         label = tk.Label(self, text="Создать пользователя " + user_type.lower())
#         entry_name = tk.Entry(self, textvariable=self.username)
#         entry_pass = tk.Entry(self, textvariable=self.password, show="*")
#         btn = tk.Button(self, text="Submit", command=self.destroy)
#         btn.grid(row=3, columnspan=2)
#
#         label.grid(row=0, columnspan=2)
#         tk.Label(self, text="Логин:").grid(row=1, column=0)
#         tk.Label(self, text="Пароль:").grid(row=2, column=0)
#         entry_name.grid(row=1, column=1)
#         entry_pass.grid(row=2, column=1)
#
#
#     def open(self):
#         self.grab_set()
#         self.wait_window()
#         username = self.username.get()
#         password = self.password.get()
#         return User(username, password, self.user_type)
#
#
# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         user_types = ("Админ", "Менеджер", "Клиент")
#         self.user_type = tk.StringVar()
#         self.user_type.set(user_types[0])
#
#         label = tk.Label(self, text="Пожалуйста, выберите роль пользователя")
#         radios = [tk.Radiobutton(self, text=t, value=t,
#                                  variable=self.user_type) for t in user_types]
#         btn = tk.Button(self, text="Создать", command=self.open_window)
#
#         label.pack(padx=10, pady=10)
#         for radio in radios:
#             radio.pack(padx=10, anchor=tk.W)
#         btn.pack(pady=10)
#
#     def open_window(self):
#         window = UserForm(self, self.user_type.get())
#         user = window.open()
#         print(user)
#
# if __name__ == "__main__":
#     app = App()
#     app.mainloop()

##############################################################################################################3

# import tkinter as tk
# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.btn = tk.Button(self, text="Открыть новое окно",
#                              command=self.open_window)
#         self.btn.pack(padx=50, pady=20)
#
#     def open_window(self):
#         about = About(self)
#         about.grab_set()
#
# class About(tk.Toplevel):
#     def __init__(self, parent):
#         super().__init__(parent)
#         self.label = tk.Label(self, text="Это всплывающее окно")
#         self.button = tk.Button(self, text="Закрыть", command=self.destroy)
#
#         self.label.pack(padx=20, pady=20)
#         self.button.pack(pady=5, ipadx=2, ipady=2)
#
#
#
# if __name__ == "__main__":
#     app = App()
#     app.mainloop()

###########################################################################################################









from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
from PIL import Image, ImageTk
from ttkbootstrap.constants import *
class Home_window(Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.master.title('Petrol Station')
        self.master.geometry('700x700+600+50')
        self.master.iconbitmap(default = r'C:\PyCharm Community Edition 2022.3.1\foto\foto.ico')
        self.master.config(bg = 'black')
        self.master.resizable(False, False)
        self.create_widgets()

    def create_widgets(self):
        img = Image.open(r'C:\PyCharm Community Edition 2022.3.1\foto\home_page.jpg')
        self.resized_img = img.resize((700, 700))
        self.new_img = ImageTk.PhotoImage(self.resized_img)
        lbl = Label(self.master,image=self.new_img)
        lbl.place(x=0,y=0)

        self.var = IntVar()
        lbl_login = ttk.Label(text='   Login:   \nPassword:',bootstyle='inverse-danger',font=('Times New Roman',16))
        lbl_login.place(x=10,y=25)

        self.entry_login = Entry(bd=2,bg='red', selectbackground='orange')
        self.entry_login.place(x=105,y=25)

        self.entry_password = Entry(bd=2,selectbackground='orange',show='*')
        self.entry_password.place(x=105,y=55)

        btn_login = ttk.Button(text='   Login   ',bootstyle="success",command=self.login)
        btn_login.place(x=95,y=85)

        btn_quit = ttk.Button(text='     Exit     ',bootstyle="warning",command=quit)
        btn_quit.place(x=170,y=85)

        btn_check = ttk.Checkbutton(text='show',bootstyle="danger",variable = self.var,command=self.show_password)
        btn_check.place(x=235,y=60)

        btn_user = ttk.Button(text='   Покупатель   ',bootstyle="primary",command=self.user_window)
        btn_user.place(height=100,width=150,x=500, y=610)

    def user_window(self):
        self.master.withdraw()
        self.user = Toplevel(self.master)
        self.userWindow = UserWindow(self.user)

    def show_password(self):
        if self.var.get() == 1:
            self.entry_password['show'] = '*'
        else:
           self.entry_password['show'] = ''
    def login(self):
        login=self.entry_login.get()
        password=self.entry_password.get()

        if login == '' and password == '':
            self.master.withdraw()
            self.new_Info_Window = Toplevel(self.master)
            self.info_Window = Admin_window(self.new_Info_Window)
        else:
            showinfo(title='Wrong data',message = 'Wrong password or login')



########################################################################################################################

class UserWindow(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title('Добро пожаловать!')
        self.master.geometry('900x750+600+50')
        self.master.iconbitmap(default=r'C:\PyCharm Community Edition 2022.3.1\foto\ico2.ico')
        self.master.resizable(False, False)
        self.create_widgit()
    def create_widgit(self):
        self.img2 = Image.open(r'C:\PyCharm Community Edition 2022.3.1\foto\user_page.jpg')
        self.resized_img = self.img2.resize((900, 750))
        self.new_img = ImageTk.PhotoImage(self.resized_img)
        lbl = Label(self.master,image=self.new_img)
        lbl.place(x=0, y=0)



########################################################################################################################

class Admin_window(Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.master.title('Admin window')
        self.master.geometry('800x700+600+50')
        self.master.iconbitmap(default=r'C:\PyCharm Community Edition 2022.3.1\foto\ico2.ico')
        self.master.resizable(False, False)
        self.create_widgit()

    def create_widgit(self):
        img_2 = Image.open(r'C:\PyCharm Community Edition 2022.3.1\foto\home_page.jpg')
        self.resized_img = img_2.resize((800, 700))
        self.new_img = ImageTk.PhotoImage(self.resized_img)
        lbl = Label(self.master,image=self.new_img)
        lbl.place(x=0,y=0)

        self.tree = ttk.Treeview(self.master, columns=('1', '2', '3', '4'), height=10, show='headings')
        self.tree.column('1', width=30, anchor=CENTER)
        self.tree.column('2', width=365, anchor=CENTER)
        self.tree.column('3', width=150, anchor=CENTER)
        self.tree.column('4', width=100, anchor=CENTER)
        self.tree.heading('1', text='№')
        self.tree.heading('2', text='Наименование')
        self.tree.heading('3', text='Категория')
        self.tree.heading('4', text='Цена')
        self.tree.pack(side=TOP)

        self.scroll = ttk.Scrollbar(self.master, command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.scroll.set)
        self.scroll.pack(side=LEFT)

        self.add_product = ttk.Button(self.master,text='Добавить товар ',command=self.add_window).place(x=150,y=200)
        self.edit_product= ttk.Button(self.master,text='Редактировать').place(x=300,y=200)
        self.delete_product = ttk.Button(self.master,text='Удалить').place(x=450,y=200)
        self.save_product = ttk.Button(self.master,text='Сохранить').place(x=600,y=200)

    def add_window(self):
        self.master.withdraw()
        self.add = Toplevel(self.master)
        self.add_product = Add_Product(self.add)


    #     lbl_petrol = ttk.Label(self.master,text='    Petrol   ',bootstyle='warning',font=('Times New Roman',20))
    #     lbl_petrol.place(x=45,y=20)
    #
    #     self.petrol_entry = Entry(self.master,bd=2,selectbackground='orange')
    #     self.petrol_entry.place(x=45,y=60)
    #
    #     self.petrol_listbox = Listbox(self.master,exportselection=0,bd=2,selectmode=MULTIPLE)
    #
    #     self.petrol_listbox.place(x=45,y=85)
    #
    #     self.add_petrol = ttk.Button(self.master,text="Добавить",bootstyle="default", command=self.add_petrol).place(x=175,y=60)
    #     self.del_petrol = ttk.Button(self.master,text="Удалить",bootstyle="danger", command=self.delete_petrol).place(x=175,y=225)
    #     self.save_petrol = ttk.Button(self.master,text="Сохранить",bootstyle="success", command=self.save_petrol).place(x=175,y=140)
    #
    #     lbl_products = ttk.Label(self.master,text='  Products ',bootstyle='inverse',font=('Times New Roman',20))
    #     lbl_products.place(x=335,y=20)
    #
    #     self.product_entry = Entry(self.master,bd=2,selectbackground='orange')
    #     self.product_entry.place(x=335,y=60)
    #
    #     self.product_listbox = Listbox(self.master,exportselection=0,bd=2,selectmode=MULTIPLE)
    #     self.product_listbox.place(x=335,y=85)
    #
    #     self.add_product = ttk.Button(self.master,text="Добавить",bootstyle="default", command=self.add_product).place(x=465,y=60)
    #     self.del_product = ttk.Button(self.master,text="Удалить",bootstyle="danger", command=self.delete_product).place(x=465,y=225)
    #     self.save_product = ttk.Button(self.master, text="Сохранить",bootstyle="success", command=self.save_product).place(x=465, y=150)
    #
    #
    # def delete_petrol(self):#----------Функция в listbox работает, но в файл изменения передать не получается
    #         index_el = self.petrol_listbox.curselection()
    #         self.petrol_listbox.delete(index_el[0])
    #
    # def add_petrol(self):#--------В файл добавляется элемент из listbox и элемент который написан в entry
    #     with open(r'C:\Users\FX505DT\Desktop\save_func\project.txt', 'a') as file:
    #         self.new_petrol_list = self.petrol_entry.get()
    #         self.petrol_listbox.insert(0, self.new_petrol_list)
    #         file.write(self.new_petrol_list)
    #
    # def save_petrol(self):
    #     with open(r'C:\Users\FX505DT\Desktop\save_func\project.txt','a') as file:
    #         file.write(self.new_petrol_list)
    #
    # def delete_product(self):
    #     selection = self.product_listbox.curselection()
    #     self.product_listbox.delete(selection[0])
    #
    # def add_product(self):
    #     self.new_product_list = self.product_entry.get()
    #     self.product_listbox.insert(0, self.new_product_list)
    #
    # def save_product(self):
    #     pass

class Add_Product(Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.master.title('Add product')
        self.master.geometry('800x700+600+50')
        self.master.iconbitmap(default=r'C:\PyCharm Community Edition 2022.3.1\foto\ico2.ico')
        self.master.resizable(False, False)
        self.create_widgit()

    def create_widgit(self):
        img_2 = Image.open(r'C:\PyCharm Community Edition 2022.3.1\foto\home_page.jpg')
        self.resized_img = img_2.resize((800, 700))
        self.new_img = ImageTk.PhotoImage(self.resized_img)
        lbl = Label(self.master,image=self.new_img)
        lbl.place(x=0,y=0)








if __name__ == '__main__':
    root = Tk()
    app = Home_window(root)
    app.mainloop()








# spin = Spinbox( 'указать окно!' , from_=0, to=100, width=5)
# spin.grid(column=0, row=0)




# from tkinter import *
# from tkinter import ttk
# from tkinter.messagebox import *
# from PIL import Image, ImageTk
# class Home_window(Frame):
#     def __init__(self,master=None):
#         super().__init__(master)
#         self.master = master
#         self.master.title('Login Window')
#         self.master.geometry('700x750+800+20')
#         self.master.iconbitmap(default = r'C:\PyCharm Community Edition 2022.3.1\foto\foto.ico')
#         self.master.config(bg = 'white')
#         self.master.resizable(False, False)
#         self.create_widgets()
#
#     def create_widgets(self):
#         self.img = Image.open(r'C:\PyCharm Community Edition 2022.3.1\foto\foto2.png')
#         self.resized_img = self.img.resize((700, 750))
#         self.new_img = ImageTk.PhotoImage(self.resized_img)
#         self.lbl = Label(self.master,image=self.new_img)
#         self.lbl.grid(row=0, column=0)
#
#         self.var = IntVar()
#         self.lbl_login = Label(text='   Login:   \nPassword:',fg='white',bg='grey',font=('Times New Roman',16))
#         self.lbl_login.place(x=10,y=10)
#
#         self.entry_login = Entry(bd=2, selectbackground='orange')
#         self.entry_login.place(x=105,y=15)
#
#         self.entry_password = Entry(bd=2,selectbackground='orange',show='*')
#         self.entry_password.place(x=105,y=40)
#
#         self.btn_login = ttk.Button(text='   Login   ',command=self.login)
#         self.btn_login.place(x=130,y=65)
#
#         self.btn_quit = ttk.Button(text='     Exit    ',command=quit)
#         self.btn_quit.place(x=130,y=95)
#
#         self.btn_check = ttk.Checkbutton(text='show',variable = self.var,command=self.show_password)
#         self.btn_check.place(x=233,y=40)
#
#         self.btn_user = Button(root,text='Покупатель',width=12, height=3,state=ACTIVE)
#         self.btn_user.config(fg='White',bg='red',font=('Algerian',20,'bold'))
#         self.btn_user.place(x=440,y=610)
#
#     def show_password(self):
#         if self.var.get() == 1:
#             self.entry_password['show'] = '*'
#         else:
#            self.entry_password['show'] = ''
#     def login(self):
#         login=self.entry_login.get()
#         password=self.entry_password.get()
#
#         if login == 'a' and password == 'a':
#             self.master.withdraw()
#             self.new_Info_Window = Toplevel(self.master)
#             self.info_Window = Admin_window(self.new_Info_Window)
#         else:
#             showinfo(title='Wrong data',message = 'Wrong password or login')
#
# class Admin_window(Frame):
#     def __init__(self,master=None):
#         super().__init__(master)
#         self.master = master
#         self.master.title('Admin window')
#         self.master.geometry('900x700+600+50')
#         self.master.resizable(False, False)
#         self.create_widgit()
#
#     def create_widgit(self):
#         self.img_2 = Image.open(r'C:\PyCharm Community Edition 2022.3.1\foto\foto3.jpg')
#         self.resized_img = self.img_2.resize((900, 700))
#         self.new_img = ImageTk.PhotoImage(self.resized_img)
#         self.lbl = Label(self.master,image=self.new_img)
#         self.lbl.grid(row=0, column=0)
#
#         self.lbl_petrol = Label(self.master,text='    Petrol   ',fg='black',bg='orange',font=('Times New Roman',20))
#         self.lbl_petrol.place(x=30,y=20)
#
#         self.petrol_entry = Entry(self.master,bd=2,selectbackground='orange')
#         self.petrol_entry.place(x=30,y=60)
#
#         self.petrol_list = Listbox(self.master,bd=2,selectmode=MULTIPLE)
#         self.petrol_list.place(x=30,y=85)
#
#         self.add_petrol = ttk.Button(self.master,text="Добавить", command=self.add_petrol).place(x=160,y=60)
#         self.del_petrol = ttk.Button(self.master,text="Удалить", command=self.delete_petrol).place(x=160,y=225)
#
#         self.lbl_products = Label(self.master,text='  Products ',fg='black',bg='green',font=('Times New Roman',20))
#         self.lbl_products.place(x=350,y=20)
#
#         self.product_entry = Entry(self.master,bd=2,selectbackground='orange')
#         self.product_entry.place(x=350,y=60)
#
#         self.product_list = Listbox(self.master,bd=2,selectmode=MULTIPLE)
#         self.product_list.place(x=350,y=85)
#
#         self.add_product = ttk.Button(self.master,text="Добавить", command=self.add_product).place(x=480,y=60)
#         self.del_product = ttk.Button(self.master,text="Удалить", command=self.delete_product).place(x=480,y=225)
#
#     def delete_petrol(self):
#         selection = self.petrol_list.curselection()
#         self.petrol_list.delete(selection[0])
#
#     def add_petrol(self):
#         self.new_petrol_list = self.petrol_entry.get()
#         self.petrol_list.insert(0, self.new_petrol_list)
#
#     def delete_product(self):
#         selection = self.product_list.curselection()
#         self.product_list.delete(selection[0])
#
#     def add_product(self):
#         self.new_product_list = self.product_entry.get()
#         self.product_list.insert(0, self.new_product_list)
#
#
# if __name__ == '__main__':
#     root = Tk()
#     app = Home_window(root)
#     app.mainloop()