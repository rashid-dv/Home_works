
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

        lbl_petrol = ttk.Label(self.master,text='    Petrol   ',bootstyle='warning',font=('Times New Roman',20))
        lbl_petrol.place(x=45,y=20)

        self.petrol_entry = Entry(self.master,bd=2,selectbackground='orange')
        self.petrol_entry.place(x=45,y=60)

        self.petrol_listbox = Listbox(self.master,exportselection=0,bd=2,selectmode=MULTIPLE)

        self.petrol_listbox.place(x=45,y=85)

        self.add_petrol = ttk.Button(self.master,text="Добавить",bootstyle="default", command=self.add_petrol).place(x=175,y=60)
        self.del_petrol = ttk.Button(self.master,text="Удалить",bootstyle="danger", command=self.delete_petrol).place(x=175,y=225)
        self.save_petrol = ttk.Button(self.master,text="Сохранить",bootstyle="success", command=self.save_petrol).place(x=175,y=140)

        lbl_products = ttk.Label(self.master,text='  Products ',bootstyle='inverse',font=('Times New Roman',20))
        lbl_products.place(x=335,y=20)

        self.product_entry = Entry(self.master,bd=2,selectbackground='orange')
        self.product_entry.place(x=335,y=60)

        self.product_listbox = Listbox(self.master,exportselection=0,bd=2,selectmode=MULTIPLE)
        self.product_listbox.place(x=335,y=85)

        self.add_product = ttk.Button(self.master,text="Добавить",bootstyle="default", command=self.add_product).place(x=465,y=60)
        self.del_product = ttk.Button(self.master,text="Удалить",bootstyle="danger", command=self.delete_product).place(x=465,y=225)
        self.save_product = ttk.Button(self.master, text="Сохранить",bootstyle="success", command=self.save_product).place(x=465, y=150)


    def delete_petrol(self):#----------Функция в listbox работает, но в файл изменения передать не получается
            index_el = self.petrol_listbox.curselection()
            self.petrol_listbox.delete(index_el[0])

    def add_petrol(self):#--------В файл добавляется элемент из listbox и элемент который написан в entry
        with open(r'C:\Users\FX505DT\Desktop\save_func\project.txt', 'a') as file:
            self.new_petrol_list = self.petrol_entry.get()
            self.petrol_listbox.insert(0, self.new_petrol_list)
            file.write(self.new_petrol_list)

    def save_petrol(self):
        with open(r'C:\Users\FX505DT\Desktop\save_func\project.txt','a') as file:
            file.write(self.new_petrol_list)

    def delete_product(self):
        selection = self.product_listbox.curselection()
        self.product_listbox.delete(selection[0])

    def add_product(self):
        self.new_product_list = self.product_entry.get()
        self.product_listbox.insert(0, self.new_product_list)

    def save_product(self):
        pass

if __name__ == '__main__':
    root = Tk()
    app = Home_window(root)
    app.mainloop()
