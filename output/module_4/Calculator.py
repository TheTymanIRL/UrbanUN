import tkinter as tk


def get_values():
    number1 = int(number1_entry.get())
    number2 = int(number2_entry.get())
    return number1, number2


def insert_values(value):
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, value)


def add():
    number1, number2 = get_values()
    res = number2 + number1
    insert_values(res)


def split():
    number1, number2 = get_values()
    res = number1 / number2
    insert_values(res)


def sub():
    number1, number2 = get_values()
    res = number1 - number2
    insert_values(res)


def mul():
    number1, number2 = get_values()
    res = number2 * number1
    insert_values(res)



window = tk.Tk()
window.title('Калькулятор')
window.geometry("350x350")
window.resizable(False, False)

button_add = tk.Button(window, text='+', width=3, height=3, command=add)
button_add.place(x=90, y=100)

button_sub = tk.Button(window, text='-', width=3, height=3, command=sub)
button_sub.place(x=140, y=100)

button_split = tk.Button(window, text='/', width=3, height=3, command=split)
button_split.place(x=190, y=100)

button_mul = tk.Button(window, text='*', width=3, height=3, command=mul)
button_mul.place(x=240, y=100)

number1_entry = tk.Entry(window, width=30)
number1_entry.place(x=90, y=60)

number1 = tk.Label(window, text='Введите первое число:')
number1.place(x=90, y=35)

number2_entry = tk.Entry(window, width=30)
number2_entry.place(x=90, y=190)

number2 = tk.Label(window, text='Введите второе число:')
number2.place(x=90, y=165)

answer_entry = tk.Entry(window, width=30)
answer_entry.place(x=90, y=250)

answer = tk.Label(window, text='Результат:')
answer.place(x=90, y=225)

window.mainloop()
