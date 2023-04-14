
from tkinter import *

root = Tk()
root.geometry('700x750+700+20')
root.resizable(False,False)
root.config(width=700,height=750,bg='White')
root.title('Registration form')
root.iconbitmap(default=r'C:\PyCharm Community Edition 2022.3.1\foto\foto.ico')

def save_button():
    text_name = entry_name.get()
    text_surname = entry_surname.get()
    text_data = entry_data.get()
    text_phone = entry_phone.get()
    lbl_name['text'] = 'Ad:' + text_name
    lbl_surname['text'] = 'Soyad:' + text_surname
    lbl_data['text'] = 'Dogum tarixi:' + text_data
    lbl_phone['text'] = 'Telefon:' + text_phone

lbl_anket = Label(text='Anket:')
lbl_anket.config(fg='Black',bg='White',font=('Times New Roman',22,'bold'))
lbl_anket.pack(side='top',anchor='center')

lbl_name = Label(text='Ad:')
lbl_name.config(fg='Black',bg='White',font=('Times New Roman',18,'bold'))
lbl_name.place(x=70,y=70)
entry_name = Entry(selectbackground='orange')
entry_name.place(x=40,y=120)

lbl_surname = Label(text='Soyad:')
lbl_surname.config(fg='Black',bg='White',font=('Times New Roman',18,'bold'))
lbl_surname.place(x=60,y=250)
entry_surname = Entry(selectbackground='orange')
entry_surname.place(x=40,y=300)

lbl_data = Label(text='Dogum tarixi:')
lbl_data.config(fg='Black',bg='White',font=('Times New Roman',18,'bold'))
lbl_data.place(x=430,y=70)
entry_data = Entry(selectbackground='orange')
entry_data.place(x=440,y=120)

lbl_phone = Label(text='Telefon:')
lbl_phone.config(fg='Black',bg='White',font=('Times New Roman',18,'bold'))
lbl_phone.place(x=460,y=250)
entry_phone = Entry(selectbackground='orange')
entry_phone.place(x=450,y=300)

btn = Button(root,text='   SAVE   ',state=ACTIVE,command=save_button)
btn.config(fg='Black',bg='White',font=('Times New Roman',24,'bold'))
btn.place(x=260,y=400)

root.mainloop()
