
from tkinter import *
root = Tk()
root.geometry('700x750+700+20')
root.resizable(False,False)
root.config(width=700,height=750,bg='#CDCDC9')
root.title('Registration Form')
root.iconbitmap(default=r'C:\PyCharm Community Edition 2022.3.1\foto\foto.ico')
var = IntVar()
var2 = IntVar()

lbl = Label(text='Registration form')
lbl.config(fg='Black',bg='#CDCDC9',font=('Times New Roman',26,'bold','underline'))
lbl.place(x=200,y=70)

lbl_fullname = Label(text='FullName:')
lbl_fullname.config(fg='Black',bg='#CDCDC9',font=('Times New Roman',18))
lbl_fullname.place(x=150,y=200)
entry_fullname = Entry(selectbackground='orange')
entry_fullname.place(x=290,y=208)

lbl_email = Label(text='Email:')
lbl_email.config(fg='Black',bg='#CDCDC9',font=('Times New Roman',18))
lbl_email.place(x=170,y=270)
entry_email = Entry(selectbackground='orange')
entry_email.place(x=290,y=275)

lbl_gender = Label(text='Gender:')
lbl_gender.config(fg='Black',bg='#CDCDC9',font=('Times New Roman',18))
lbl_gender.place(x=160,y=340)

lbl_age = Label(text='Age:')
lbl_age.config(fg='Black',bg='#CDCDC9',font=('Times New Roman',18))
lbl_age.place(x=170,y=410)
entry_age = Entry(selectbackground='orange')
entry_age.place(x=290,y=415)

def click_checkbutton():
    print(var.get())
    if var.get() == 1:
        btn.config(state = ACTIVE)
    else:
        btn['state'] = DISABLED
check = Checkbutton(text = 'Male',bg='#CDCDC9', variable= var, command=click_checkbutton)
check.place(x=280,y=345)

def click_checkbutton2():
    print(var2.get())
    if var2.get() == 1:
        btn.config(state = ACTIVE)
    else:
        btn['state'] = DISABLED
check = Checkbutton(text = 'Female',bg='#CDCDC9', variable= var2, command=click_checkbutton2)
check.place(x=340,y=345)


def save_button():
    name = entry_fullname.get()
    email = entry_email.get()
    age = entry_age.get()
    if var.get() == 1:
        print(f'Fullname:{name}, Email-{email}, Gender - Male, Age:{age}')
    else:
        print(f'Fullname:{name}, Email-{email}, Gender - Female, Age:{age}')


btn = Button(root,text='        Submit        ',state=ACTIVE,command=save_button)
btn.config(fg='White',bg='Red',font=('Times New Roman',24,'bold'))
btn.place(x=220,y=600)

root.mainloop()













###---------------------- Okno s vxodom
# from tkinter import *
# from tkinter import ttk
# from tkinter.messagebox import *
# class LoginWindow(Frame):
#     def __init__(self,master=None):
#         super().__init__(master)
#         self.master = master
#         self.master.title('Login Window')
#         self.master.iconbitmap(default = r'C:\PyCharm Community Edition 2022.3.1\foto\foto.ico')
#         self.master.config(bg = '#db6825')
#         self.master.resizable(False, False)
#         self.create_widgets()
#
#     def create_widgets(self):
#         lbl_login = Label(text='Login:').grid(row=0)
#         lbl_password = Label(text='Password:').grid(row=1)
#
#         self.user_login = Entry(bd=3)
#         self.user_login.grid(row=0,column=1)
#         self.user_password = Entry(bd=3,show='*')
#         self.user_password.grid(row=1, column=1)
#
#         self.btn_login = ttk.Button(text='Login:',command= self.login)
#         self.btn_login.grid(row=2,column=2,columnspan=3)
#
#         self.btn_quit = ttk.Button(text='Exit',command=self.quit)
#         self.btn_quit.grid(row=3, column=2, columnspan=3)
#
#     def login(self):
#         login=self.user_login.get()
#         password=self.user_password.get()
#
#         if login == 'Lego' and password == '12345':
#             self.master.withdraw()
#             self.new_Info_Window = Toplevel(self.master)
#             self.info_Window = InfoWindow(self.new_Info_Window)
#         else:
#             showinfo(title='wrong data',message = 'wrong password or login')
#
# class InfoWindow(Frame):
#
#     def __init__(self,master=None):
#         super().__init__(master)
#         self.master = master
#         self.master.title('Login Window')
#         self.master.geometry('700x750')
#         self.master.resizable(False, False)
#         self.create_widgit()
#
#     def create_widgit(self):
#         lbl = Label(self.master,text='you hacked my data',font = 'Arial 38 bold italic underline')
#         lbl.grid(row=0,column=0)
#
# if __name__ == '__main__':
#     root = Tk()
#     app = LoginWindow(root)
#     app.mainloop()

