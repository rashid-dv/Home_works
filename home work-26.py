
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
class LoginWindow(Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.master.title('Login Window')
        self.master.geometry('300x100+700+20')
        self.master.iconbitmap(default = r'C:\PyCharm Community Edition 2022.3.1\foto\foto.ico')
        self.master.config(bg = '#4682b4')
        self.master.resizable(False, False)
        self.create_widgets()
    def create_widgets(self):
        self.var = IntVar()
        lbl_login = Label(text='Login:').grid(row=0)
        lbl_password = Label(text='Password:').grid(row=1)

        self.user_login = Entry(bd=3,selectbackground='orange')
        self.user_login.grid(row=0,column=1)

        self.user_password = Entry(bd=3,selectbackground='orange',show='*')
        self.user_password.bind('<Return>',self.login)
        self.user_password.grid(row=1, column=1)

        self.btn_login = ttk.Button(text='Login',command= self.login)
        self.btn_login.grid(row=2,column=2,columnspan=3)

        self.btn_quit = ttk.Button(text='Exit',command=self.quit)
        self.btn_quit.grid(row=3, column=2, columnspan=3)

        self.btn_check = ttk.Checkbutton(text='show',variable = self.var ,command=self.show_password)
        self.btn_check.grid(row=1, column=2)

    def login(self,event):
        login=self.user_login.get()
        password=self.user_password.get()

        if login == 'admin' and password == 'admin':
            self.master.withdraw()
            self.new_Info_Window = Toplevel(self.master)
            self.info_Window = InfoWindow(self.new_Info_Window)
        else:
            showinfo(title='Wrong data',message = 'Wrong password or login')

    def show_password(self):
        if self.var.get()==1:
            self.user_password['show']='*'
        else:
            self.user_password['show']=''

class InfoWindow(Frame):

    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.master.title('Login Window')
        self.master.geometry('700x750')
        self.master.resizable(False, False)
        self.create_widgit()

    def create_widgit(self):
        lbl = Label(self.master,text='you hacked my data',font = 'Arial 24 bold italic underline')
        lbl.grid(row=0,column=0)

if __name__ == '__main__':
    root = Tk()
    app = LoginWindow(root)
    app.mainloop()


