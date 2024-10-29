import tkinter
from tkinter import filedialog
import os


def file_select():
  filename = filedialog.askopenfilename(initialdir='/', title='Выберите файл',
                                        filetypes=(('Текстовый файл', '.txt', 
                                                    'Все файлы', '*')))
  text['text'] = text['text'] + '' + filename

window = tkinter.Tk()
window.title('Проводник')
window.geometry('350x350')
window.configure(bg='black')
window.resizable(False, False)
text = tkinter.Label(window, text='Файл', height=5, width=65, background='silver',
                     foreground='blue')
text.grid(column=1, row=1)
button_select = tkinter.Button(window, width=5, height=3, text='Выбрать файл',
                               background='silver', foreground='blue',
                               command=file_select)
button_select.grid(column=1, row=2, pady=5)
window.mainloop()
