
from tkinter import *

from tkinter.messagebox import *
from PIL import Image, ImageTk
from ttkbootstrap.constants import *
import ttkbootstrap as ttk
class Home_window(Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.master.title('Petrol Station')
        self.master.geometry('700x700+800+50')
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

        img2 = Image.open(r'C:\PyCharm Community Edition 2022.3.1\foto\label.png')
        self.resized_img = img2.resize((500,80))
        self.new_img2 = ImageTk.PhotoImage(self.resized_img)
        lbl = Label(self.master,image=self.new_img2)
        lbl.place(x=0,y=20)

        self.var = IntVar()
        lbl_login = ttk.Label(text='   Login:   \nPassword:',bootstyle='inverse-danger',font=('Times New Roman',16))
        lbl_login.place(x=10,y=250)

        self.entry_login = Entry(bd=2,bg='red', selectbackground='orange')
        self.entry_login.place(x=105,y=250)
        self.entry_password = Entry(bd=2,selectbackground='orange',show='*')
        self.entry_password.place(x=105,y=275)

        btn_login = ttk.Button(text='   Login   ',bootstyle="success",command=self.login)
        btn_login.place(x=95,y=300)
        btn_quit = ttk.Button(text='     Exit     ',bootstyle="warning",command=quit)
        btn_quit.place(x=170,y=300)

        btn_check = ttk.Checkbutton(text='show',bootstyle="danger",variable = self.var,command=self.show_password)
        btn_check.place(x=235,y=280)

        btn_user = ttk.Button(text='   Покупатель   ',bootstyle="danger",command=self.user_window)
        btn_user.place(height=100,width=150,x=500, y=550)

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

        if login == 'admin' and password == 'admin':
            self.new_Info_Window = Toplevel(self.master)
            self.info_Window = Admin_window(self.new_Info_Window)
        else:
            showinfo(title='Wrong data',message = 'Wrong password or login')


########################################################################################################################
class Admin_window(Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.master.title('Admin window')
        self.master.geometry('800x700+700+50')
        self.master.iconbitmap(default=r'C:\PyCharm Community Edition 2022.3.1\foto\ico2.ico')
        self.master.resizable(False, False)
        self.create_widgit()

    def create_widgit(self):
        img_2 = Image.open(r'C:\PyCharm Community Edition 2022.3.1\foto\user_page.jpg')
        self.resized_img = img_2.resize((800, 700))
        self.new_img = ImageTk.PhotoImage(self.resized_img)
        lbl = Label(self.master,image=self.new_img)
        lbl.place(x=0,y=0)

        img2 = Image.open(r'C:\PyCharm Community Edition 2022.3.1\foto\label.png')
        self.resized_img = img2.resize((700,85))
        self.new_img2 = ImageTk.PhotoImage(self.resized_img)
        lbl = Label(self.master,image=self.new_img2)
        lbl.place(x=0,y=50)

        lbl_petrol = ttk.Label(self.master,text='Petrol',anchor=CENTER,bootstyle="danger",font=('Times New Roman',20))
        lbl_petrol.place(height=50,width=128,x=100,y=310)
        lbl_petrol = ttk.Label(self.master,text='Name:\nPrice:',font=('Times New Roman',14))
        lbl_petrol.place(height=50,width=50,x=50,y=350)

        self.petrol_name_entry = Entry(self.master,bd=2,selectbackground='orange')
        self.petrol_name_entry.place(x=100,y=350)
        self.petrol_price_entry = Entry(self.master,bd=2,selectbackground='orange')
        self.petrol_price_entry.place(x=100,y=375)

        self.petrol_listbox = Listbox(self.master,exportselection=0,bd=2,selectmode=MULTIPLE)
        self.petrol_listbox.place(x=100,y=400)

        self.add_petrol = ttk.Button(self.master,text="Добавить",bootstyle="default",command=self.add_petrol)
        self.add_petrol.place(height=50,width=90,x=230,y=350)
        self.save_petrol = ttk.Button(self.master,text="Сохранить",bootstyle="success",command=self.save_petrol)
        self.save_petrol.place(height=50,width=90,x=230,y=400)
        self.del_petrol = ttk.Button(self.master,text="Удалить",bootstyle="danger",command=self.delete_petrol)
        self.del_petrol.place(height=50,width=90,x=230,y=450)

        lbl_petrol = ttk.Label(self.master,text='Store',anchor=CENTER,bootstyle="inverse-success",font=('Times New Roman',20))
        lbl_petrol.place(height=50,width=128,x=500,y=300)
        lbl_petrol = ttk.Label(self.master,text='Name:\nPrice:',font=('Times New Roman',14))
        lbl_petrol.place(height=50,width=50,x=450,y=350)

        self.product_name_entry = Entry(self.master,bd=2,selectbackground='orange')
        self.product_name_entry.place(x=500,y=350)
        self.product_price_entry = Entry(self.master,bd=2,selectbackground='orange')
        self.product_price_entry.place(x=500,y=375)

        self.product_listbox = Listbox(self.master,exportselection=0,bd=2,selectmode=MULTIPLE)
        self.product_listbox.place(x=500,y=400)

        self.add_product = ttk.Button(self.master,text="Добавить",bootstyle="default",command=self.add_product)
        self.add_product.place(height=50,width=90,x=630,y=350)
        self.save_product = ttk.Button(self.master,text="Сохранить",bootstyle="success",command=self.save_product)
        self.save_product.place(height=50,width=90,x=630,y=400)
        self.del_product = ttk.Button(self.master, text="Удалить",bootstyle="danger",command=self.delete_product)
        self.del_product.place(height=50,width=90,x=630, y=450)
    def delete_petrol(self):
        index_el = self.petrol_listbox.curselection()
        self.petrol_listbox.delete(index_el[0])
    def add_petrol(self):
        self.petrol_dict = {}
        self.petrol_dict[self.petrol_name_entry] = self.petrol_price_entry
        self.new_petrol_list = self.petrol_name_entry.get()+'-'+self.petrol_price_entry.get()
        self.petrol_listbox.insert(0,self.new_petrol_list)
    def save_petrol(self):
        with open(r'C:\Users\FX505DT\Desktop\info\file.info.txt','w') as file:
            for item in self.petrol_listbox.get(0,END):
                file.write(item+'\n')
    def delete_product(self):
        index_el = self.product_listbox.curselection()
        self.product_listbox.delete(index_el[0])
    def add_product(self):
        product_dict = {}
        product_dict[self.product_name_entry] = self.product_price_entry
        self.new_product_list = self.product_name_entry.get() + ' - ' + self.product_price_entry.get()
        self.product_listbox.insert(0, self.new_product_list)
    def save_product(self):
        with open(r'C:\Users\FX505DT\Desktop\info\file.info.txt','w') as file:
            for item in self.product_listbox.get(0,END):
                file.write(item+'\n')

########################################################################################################################
class UserWindow(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title('Добро пожаловать!')
        self.master.geometry('900x750+600+20')
        self.master.iconbitmap(default=r'C:\PyCharm Community Edition 2022.3.1\foto\ico2.ico')
        self.master.resizable(False, False)
        self.create_widgit()
    def create_widgit(self):
        self.img2 = Image.open(r'C:\PyCharm Community Edition 2022.3.1\foto\user_page.jpg')
        self.resized_img = self.img2.resize((900, 750))
        self.new_img = ImageTk.PhotoImage(self.resized_img)
        lbl = Label(self.master,image=self.new_img)
        lbl.place(x=0, y=0)

        img2 = Image.open(r'C:\PyCharm Community Edition 2022.3.1\foto\label.png')
        self.resized_img = img2.resize((800,100))
        self.new_img2 = ImageTk.PhotoImage(self.resized_img)
        lbl = Label(self.master,image=self.new_img2)
        lbl.place(x=0,y=50)

        btn_user = ttk.Button(self.master,text='Пройти в Кафе',bootstyle="success",command=self.cafe_window)
        btn_user.place(height=100,width=130,x=150, y=550)

        btn_user = ttk.Button(self.master,text='   Заправиться   ',bootstyle="danger",command=self.user_window)
        btn_user.place(height=100,width=150,x=550, y=550)

    def user_window(self):
        self.petrol = Toplevel(self.master)
        self.userWindow = Petrol(self.petrol)

    def cafe_window(self):
        self.cafe = Toplevel(self.master)
        self.cafeWindow = Cafe(self.cafe)

########################################################################################################################
class Petrol(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title('Добро пожаловать!')
        self.master.geometry('1000x600+500+50')
        self.master.iconbitmap(default=r'C:\PyCharm Community Edition 2022.3.1\foto\ico2.ico')
        self.master.resizable(False, False)
        self.master.config(bg='black')
        self.create_widgit()
    def create_widgit(self):
        self.img2 = Image.open(r'C:\PyCharm Community Edition 2022.3.1\foto\zapravka.jpg')
        self.resized_img = self.img2.resize((1100, 600))
        self.new_img = ImageTk.PhotoImage(self.resized_img)
        lbl = Label(self.master,image=self.new_img)
        lbl.place(x=0, y=0)
        self.val1 = IntVar()
        self.val2 = IntVar()

        self.pokupatel = ttk.Label(self.master, anchor=NW, text='Visitor\nВаш баланс:',bootstyle='inverse-danger', font=('Algerian', 18))
        self.pokupatel.place(height=100, width=350, x=20, y=20)

        self.lbl_cash = ttk.Label(self.master,textvariable=self.val1)
        self.lbl_cash.place(x=180,y=50)
        self.scale_cash = ttk.Scale(self.master,orient=HORIZONTAL, length=200, from_=0, to=2000,variable=self.val1)
        self.scale_cash.place(x=100,y=90)

        self.petrol_choice = ttk.Label(self.master,anchor=N,text='Выберите топливо:',bootstyle='inverse-danger',font=('Algerian',18))
        self.petrol_choice.place(height=100,width=230,x=20,y=300)

        self.sum_petrol = ttk.Label(self.master,anchor=N,text='Введите количество:',bootstyle='inverse-danger',font=('Algerian',18))
        self.sum_petrol.place(height=100,width=270,x=280,y=300)

        self.lbl_kol = ttk.Label(self.master,textvariable=self.val2)
        self.lbl_kol.place(x=440,y=375)
        self.scale = ttk.Scale(self.master,orient=HORIZONTAL, length=200, from_=0, to=300,variable=self.val2)
        self.scale.place(x=310,y=350)

        self.btn_buy = ttk.Button(self.master,text='Оплатить',bootstyle="success-outline",command=self.buy)
        self.btn_buy.place(height=50,width=130,x=200, y=470)

        self.petrols = ['АИ - 92: 0.90-azn','АИ - 95: 1.50-azn','АИ - 98: 1.60-azn','Dizel: 0.60-azn']
        self.price = [0.90,1.50,1.60]
        self.combobox = ttk.Combobox(self.master,values=self.petrols,bootstyle="default-danger",state=READONLY)
        self.combobox.place(height=30,width=200,x=30,y=350)

    def buy(self):
        if self.combobox.get() == self.petrols[0]:
            self.result = self.scale.get() * self.price[0]

        elif self.combobox.get() == self.petrols[1]:
            self.result = self.scale.get() * self.price[1]

        elif self.combobox.get() == self.petrols[2]:
            self.result = self.scale.get() * self.price[2]

        else:
            self.result = self.scale.get() * self.price[3]

        print(self.result)


class Cafe(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title('Добро пожаловать!')
        self.master.geometry('1000x750+400+50')
        self.master.iconbitmap(default=r'C:\PyCharm Community Edition 2022.3.1\foto\ico2.ico')
        self.master.resizable(False, False)
        self.master.config(bg='black')
        self.create_widgit()
    def create_widgit(self):
        self.img2 = Image.open(r'C:\PyCharm Community Edition 2022.3.1\foto\cafe.jpg')
        self.resized_img = self.img2.resize((1000, 700))
        self.new_img = ImageTk.PhotoImage(self.resized_img)
        lbl = Label(self.master,image=self.new_img)
        lbl.place(x=0, y=0)
        val = IntVar()

        self.lbl_drink = ttk.Label(self.master,text='Drinks',anchor=CENTER,bootstyle='default',font=('Algerian',18))
        self.lbl_drink.place(height=50,width=220,x=0,y=110)
        self.lbl_food = ttk.Label(self.master,text='Food',anchor=CENTER,bootstyle='default',font=('Algerian',18))
        self.lbl_food.place(height=50,width=220,x=800,y=110)

        self.dr_list = ['Latte - 6.0_azn','Cappuchino - 7.20_azn','Carramel Macchiato - 8.50_azn','Black coffee - 5.30_azn']
        self.dr_price = [6.0,7.20,8.50,5.30]
        self.drinks = ttk.Combobox(self.master,values=self.dr_list,state=READONLY)
        self.drinks.place(height=30,width=280,x=20,y=200)

        self.fd_list = ['Sandwich - 10.8_azn','Chocolate Cake - 6.70_azn','Strawberry Mousse - 8.20_azn','Pizza Mix - 17.0_azn']
        self.fd_price = [10.8,6.70,8.20,17.0]
        self.food = ttk.Combobox(self.master,values=self.fd_list,state=READONLY)
        self.food.place(height=30,width=280,x=700,y=200)

        self.btn_drinks = ttk.Button(self.master,text='Оплатить',bootstyle="success-outline",command=self.buy_drink)
        self.btn_drinks.place(height=80,width=180,x=70, y=250)

        self.btn_food = ttk.Button(self.master,text='Оплатить',bootstyle="success-outline",command=self.buy_food)
        self.btn_food.place(height=80,width=180,x=740, y=250)

        self.lbl_drink = ttk.Label(self.master,text='Visitor',anchor=N,bootstyle='inverse-secondary',font=('Algerian',18))
        self.lbl_drink.place(height=100,width=300,x=350,y=530)

        self.scale_money = ttk.Scale(self.master,orient=HORIZONTAL, length=200, from_=0.0, to=100.0,variable=val)
        self.scale_money.place(x=410,y=600)
        self.lbl_balance = ttk.Label(self.master,text='Количество средств:',bootstyle='inverse-secondary',font=('Algerian',12))
        self.lbl_balance.place(x=360,y=570)
        self.lbl_money = ttk.Label(self.master,textvariable=val)
        self.lbl_money.place(x=530,y=573)

    def buy_drink(self):
        if self.drinks.get() == self.dr_list[0]:
            self.result = self.scale_money.get() - self.dr_price[0]

        elif self.drinks.get() == self.dr_list[1]:
            self.result = self.scale_money.get() - self.dr_price[1]

        elif self.drinks.get() == self.dr_list[2]:
            self.result = self.scale_money.get() - self.dr_price[2]

        else:
            self.result = self.scale_money.get() - self.dr_price[3]
        print(self.result)

    def buy_food(self):
        if self.food.get() == self.fd_list[0]:
            self.result = self.scale_money.get() - self.fd_price[0]

        elif self.food.get() == self.fd_list[1]:
            self.result = self.scale_money.get() - self.fd_price[1]

        elif self.food.get() == self.fd_list[2]:
            self.result = self.scale_money.get() - self.fd_price[2]

        else:
            self.result = self.scale_money.get() - self.fd_price[3]
        print(self.result)




if __name__ == '__main__':
    root = Tk()
    app = Home_window(root)
    app.mainloop()
