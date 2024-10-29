import tkinter
from tkinter import filedialog
import os

def change_settings():
    pass


def file_select():
  filename = filedialog.askopenfilename(initialdir='/', title='Выберите файл',
                                        filetypes=(("text files", "*.txt"), ("all files", "*.*")))
  text['text'] = text['text'] + '' + filename

window = tkinter.Tk()
window.title('Проводник')
window.geometry('350x350')
window.configure(bg='black')
window.resizable(False, False)
text = tkinter.Label(window,
                     text='Файл',
                     height=5,
                     width=50,
                     background='silver',
                     foreground='blue')
text.grid(column=1,
          row=1)
button_select = tkinter.Button(window,
                               width=50,
                               height=5,
                               text='Выбрать файл',
                               background='silver',
                               foreground='blue',
                               command=file_select)
button_select.grid(column=1,
                   row=2,)

settings_button = tkinter.Button(window,
                                 width=50,
                                 height=5,
                                 text='Настройки',
                                 background='silver',
                                 command=change_settings())
settings_button.grid(column=1,
                     row=3)
close_button = tkinter.Button(window,
                              width=50,
                              height=5,
                              text='Закрыть',
                              background='silver',
                              command=window.destroy)
close_button.grid(column=1,
                  row=4)

window.mainloop()

