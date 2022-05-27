from tkinter import *
from tkinter.filedialog import asksaveasfile, askopenfile
from tkinter.messagebox import showerror
 
from tkinter import messagebox
 
root = Tk()
root.title('Наш блокнот :)')
 
root.minsize(width=500,height=400)
root.maxsize(width=500,height=400)
 
FILE_NAME = None
 
def new_file():
    global FILE_NAME
    FILE_NAME='Без названия'
    text.delete('1.0',END)
 
def save_file():
    data=text.get('1.0',END)
    out = open(FILE_NAME,'w')
    out.write(data)
    out.close()

def save_as():
    out = asksaveasfile(mode="w",defaultextension='txt')
    data=text.get('1.0',END)
    try:
        out.write(data.rscript())
    except:
        showerror(little="Ошибка",message='Ошибка сохранения файла')
def open_file():
    global FILE_NAME
    inp=askopenfile(mode='r')
    if inp is None:
        return
    FILE_NAME=inp.name
    data=inp.read()
    text.delete('1.0',END)
    text.insert('1.0',data)

def info():
    messagebox.showinfo('Информация','Блокнот разработан Шульським Назаром')
 
text = Text(root,width=400,height=400,wrap='word')
scrollb = Scrollbar(root,orient=VERTICAL,command=text.yview)
scrollb.pack(side='right', fill='y')
text.configure(yscrollcommand=scrollb.set)
 
text.pack()
 
menuBar = Menu(root)
fileMenu = Menu(menuBar)
fileMenu.add_command(label='Новый файл',command=new_file)
fileMenu.add_command(label='Сохранить',command=save_file)
 
menuBar.add_cascade(label='Файл',menu=fileMenu)
 
root.config(menu=menuBar)
root.mainloop()