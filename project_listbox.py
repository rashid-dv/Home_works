
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

        if login == '' and password == '':
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

        lbl_petrol = ttk.Label(self.master,text='Petrol',anchor=CENTER,bootstyle="inverse-danger",font=('Times New Roman',20))
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

        lbl_petrol = ttk.Label(self.master,text='Product',anchor=CENTER,bootstyle="inverse-success",font=('Times New Roman',20))
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

        btn_user = ttk.Button(self.master,text='   Заправиться   ',bootstyle="danger",command=self.user_window)
        btn_user.place(height=100,width=150,x=500, y=550)

        btn_user = ttk.Button(self.master,text='   Магазин   ',bootstyle="success")
        btn_user.place(height=100,width=150,x=250, y=550)

    def user_window(self):
        self.petrol = Toplevel(self.master)
        self.userWindow = Petrol(self.petrol)


class Petrol(Admin_window):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title('Добро пожаловать!')
        self.master.geometry('900x750+600+20')
        self.master.iconbitmap(default=r'C:\PyCharm Community Edition 2022.3.1\foto\ico2.ico')
        self.master.resizable(False, False)
        self.create_widgit()
    def create_widgit(self):
        self.img2 = Image.open(r'C:\PyCharm Community Edition 2022.3.1\foto\station.jpg')
        self.resized_img = self.img2.resize((900, 750))
        self.new_img = ImageTk.PhotoImage(self.resized_img)
        lbl = Label(self.master,image=self.new_img)
        lbl.place(x=0, y=0)


if __name__ == '__main__':
    root = Tk()
    app = Home_window(root)
    app.mainloop()
