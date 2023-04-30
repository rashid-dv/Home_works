


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
        self.master.iconbitmap(default=r'\PyCharm Community Edition 2022.3.1\foto\ico2.ico')
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

        self.tree = ttk.Treeview(self.master, columns=('1', '2'), height=10, show='headings')
        self.tree.column('1', width=365, anchor=CENTER)
        self.tree.column('2', width=100, anchor=CENTER)

        self.tree.heading('1', text='Наименование')
        self.tree.heading('2', text='Цена')
        self.tree.pack(side=TOP)

        self.scroll = ttk.Scrollbar(self.master, command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.scroll.set)
        self.scroll.place(x=650,y=100)

        self.add_product = ttk.Button(self.master, text='Добавить',command=lambda: Add_Product(Toplevel(self.master), tree=self.tree))
        self.add_product.place(x=150, y=200)
        self.edit_product= ttk.Button(self.master,text='Редактировать',command=self.edit).place(x=300,y=200)
        self.delete_product = ttk.Button(self.master,text='Удалить').place(x=450,y=200)
        self.save_product = ttk.Button(self.master,text='Сохранить').place(x=600,y=200)

    def add_product(self):
        self.add = Toplevel(self.master)
        self.add_product = Add_Product(self.add)

    def edit(self):
        self.edit = Toplevel(self.master)
        self.edit_product = Edit_Product(self.edit)



class Add_Product(Admin_window):
    def __init__(self,master=None, tree=None):
        super().__init__(master)
        self.master = master
        self.tree = tree  # store the tree widget as an instance variable

        self.master.title('Add product')
        self.master.geometry('400x200+600+150')
        self.master.iconbitmap(default=r'C:\PyCharm Community Edition 2022.3.1\foto\ico2.ico')
        self.master.resizable(False, False)

        name = ttk.Label(self.master, text='Название продукта:')
        name.place(x=50, y=50)
        price = ttk.Label(self.master, text='Цена:')
        price.place(x=50, y=110)

        self.product_name = ttk.Entry(self.master)
        self.product_name.place(x=200, y=50)
        self.product_price = ttk.Entry(self.master)
        self.product_price.place(x=200, y=110)

        self.btn_add = ttk.Button(self.master, text='Добавить',command=self.products)
        self.btn_add.place(x=200, y=150)

    def products(self):
        name = self.product_name.get()
        price = self.product_price.get()

        # insert values into Treeview
        self.tree.insert('', 1, values=(name, price))


class Edit_Product(Admin_window):
    def __init__(self,master=None,tree=None):
        super().__init__(master)
        self.master = master
        self.tree = tree
        self.master.title('Edit product')
        self.master.geometry('400x200+600+150')
        self.master.iconbitmap(default=r'C:\PyCharm Community Edition 2022.3.1\foto\ico2.ico')
        self.master.resizable(False, False)
        self.create_widgit()

    def create_widgit(self):
        self.btn_save = ttk.Button(self.master, text='Сохранить')
        self.btn_save.place(x=100, y=150)

if __name__ == '__main__':
    root = Tk()
    app = Home_window(root)
    app.mainloop()