
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

